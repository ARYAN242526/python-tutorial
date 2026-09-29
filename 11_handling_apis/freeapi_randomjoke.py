import requests

def fetch_random_joke_freepai():
    url = " https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        random_joke = data["data"]
        joke_content = random_joke["content"]
        return joke_content
    else:
        raise Exception("Failed to fetch random joke")

def main():
    try:
        joke_content = fetch_random_joke_freepai()
        print(f"Joke content: {joke_content}") 
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
