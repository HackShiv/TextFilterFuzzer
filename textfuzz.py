import requests
import concurrent.futures
from colorama import Fore, Style

session = requests.Session()

def make_request(url, word, filter_texts):
    try:
        response = session.get(f"{url}/{word}", timeout=5)
        if all(filter_text not in response.text for filter_text in filter_texts):
            print(f"{url}/{word} -", Fore.CYAN + str(response.status_code) + Style.RESET_ALL)
    except requests.RequestException as e:
        print(f"Error making request for {url}/{word}: {e}")

def fuzz_url(url, wordlist, filter_texts):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(make_request, url, word, filter_texts) for word in wordlist]
        for future in concurrent.futures.as_completed(futures):
            future.result()

def main():
    url = input("Enter the URL: ")
    wordlist_path = input("Enter the path to the wordlist file: ")
    filter_text_input = input("Enter the filter text separated by comma (e.g., 'Not Found,406 Not Acceptable'): ")
    filter_texts = [filter_text.strip() for filter_text in filter_text_input.split(",")]

    with open(wordlist_path, 'r') as file:
        words = file.read().split()

    fuzz_url(url, words, filter_texts)

if __name__ == "__main__":
    main()
