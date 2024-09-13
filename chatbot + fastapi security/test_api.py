import requests
import threading
import time
if __name__ == '__main__':
    def make_request(url):
        try:
            response = requests.get(url)
            # Assuming the response is JSON and contains an 'answer' key
            data = response.json()
            print(f"Response from {url}: {response.status_code} ::: {data['answer']}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {url}: {e}")
        except KeyError:
            print(f"Key 'answer' not found in the response from {url}")
        except ValueError:
            print(f"Invalid JSON response from {url}: {response.text}")

    # List of URLs to make requests to
    urls = [
        "http://127.0.0.1:8000/chatbot/tell me ranking of Afghanistan",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Bolivia",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Bosnia",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Botswana",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Suriname",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Swaziland",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Sweden",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Switzerland",
        "http://127.0.0.1:8000/chatbot/tell me details of Syria",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Tajikistan",
        "http://127.0.0.1:8000/chatbot/tell me details of Tanzania",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Afghanistan",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Bolivia",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Bosnia",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Botswana",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Suriname",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Swaziland",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Sweden",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Switzerland",
        "http://127.0.0.1:8000/chatbot/tell me details of Syria",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Tajikistan",
        "http://127.0.0.1:8000/chatbot/tell me details of Tanzania",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Afghanistan",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Bolivia",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Bosnia",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Botswana",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Suriname",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Swaziland",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Sweden",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Switzerland",
        "http://127.0.0.1:8000/chatbot/tell me details of Syria",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Tajikistan",
        "http://127.0.0.1:8000/chatbot/tell me details of Tanzania",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Afghanistan",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Bolivia",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Bosnia",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Botswana",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Suriname",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Swaziland",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Sweden",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Switzerland",
        "http://127.0.0.1:8000/chatbot/tell me details of Syria",
        "http://127.0.0.1:8000/chatbot/tell me ranking of Tajikistan",
        "http://127.0.0.1:8000/chatbot/tell me details of Tanzania"
    ]

    # Create and start threads for each URL
    threads = []
    start = time.time()
    for url in urls:                
        thread = threading.Thread(target=make_request, args=(url,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    end = time.time()
    final = end - start
    print(f"All requests completed. time = {final}")

