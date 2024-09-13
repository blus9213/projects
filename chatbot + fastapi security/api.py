
import os

os.environ["COHERE_API_KEY"] ='lnmN6K5rRKfsqeebjnJLX8e3Ebz6MPtO4yztOSKE'

from fastapi import FastAPI
from langchain.prompts.chat import ChatPromptTemplate
from langchain_cohere.llms import Cohere
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings.text2vec import Text2vecEmbeddings
from langchain.chains.retrieval import create_retrieval_chain


app = FastAPI()


def loader_web(url):
  loader = WebBaseLoader(url)
  data = loader.load()
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
  splitdocs= text_splitter.split_documents(data)

  return splitdocs

def create_vector(docs):
  embedding = CohereEmbeddings( model="embed-english-light-v3.0")
  vectorStore = FAISS.from_documents(docs,embedding)
  return vectorStore


def create_chain(vectorStore):
  llm = Cohere(
    model="command-xlarge-nightly",
    cohere_api_key="lnmN6K5rRKfsqeebjnJLX8e3Ebz6MPtO4yztOSKE",
    temperature= 0.4,
  )
  prompt=ChatPromptTemplate.from_template("""
  Answer the user query.
  context:{context}
  user:{input}
    """)
  chain= create_stuff_documents_chain(
    llm=llm,
    prompt=prompt,
    )
  retriver = vectorStore.as_retriever()
  retriver_chain = create_retrieval_chain(
      retriver,
      chain
  )
  return retriver_chain

docA=loader_web('https://www.empireonline.com/movies/features/best-movies-2/')
vectorStore = create_vector(docA)
chain = create_chain(vectorStore)

st = str(input("ask"))

response = chain.invoke({
    "input": st 
    })
print(response['answer'])


    