import os
import uvicorn
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader, CSVLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_cohere.llms import Cohere
from fastapi import FastAPI, Path, Depends, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from langchain_community.embeddings.text2vec import Text2vecEmbeddings
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

os.environ["COHERE_API_KEY"] = 'lnmN6K5rRKfsqeebjnJLX8e3Ebz6MPtO4yztOSKE'

app = FastAPI()

class Token(BaseModel):
    access_token: str
    token_type: str

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

def load_data(file):
    loader = CSVLoader(file_path=file)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    splitdocs = text_splitter.split_documents(data)
    return splitdocs

def load_data_from_web(url):
    loader = WebBaseLoader(url)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=200)
    splitdocs = text_splitter.split_documents(data)
    return splitdocs

def create_vector(docs):
    embedding = Text2vecEmbeddings()
    vectorStore = FAISS.from_documents(docs, embedding)
    return vectorStore

def create_chain(vectorStore):
    llm = Cohere(
        cohere_api_key="lnmN6K5rRKfsqeebjnJLX8e3Ebz6MPtO4yztOSKE",
        temperature=0.1,
    )
    prompt = ChatPromptTemplate.from_template("""
    Answer the user query.WITH RESPECT to the SOURCE document. and do comparisons with respect to {context}. IF you cannot find the answer say "I dont know"
    context:{context}
    user:{input}
    """)
    chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt,
    )
    retriver = vectorStore.as_retriever()
    retriver_chain = create_retrieval_chain(
        retriver,
        chain
    )
    return retriver_chain

def generate_token(username, password):
    
    if username == "admin" and password == "password":
        return Token(access_token="access_token", token_type="bearer")
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/token")
async def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    return generate_token(form_data.username, form_data.password)


@app.get("/chatbot/{ask}")
async def chat(ask: str = Path(description="Ask a question from the Chatbot"), token: str = Depends(oauth_scheme)):
    response = chain.invoke({
        "input": ask
    })
    return {"answer": response['answer'], "source": response}


if __name__ == '__main__':
    documents = load_data(r'C:\Users\HP\Downloads\2019.csv')
    vector = create_vector(documents)
    chain = create_chain(vector)
    uvicorn.run(app, host="0.0.0.0", port=8000)