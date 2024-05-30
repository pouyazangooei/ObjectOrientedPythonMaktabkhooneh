import requests
from abc import ABC, abstractmethod

# Abstract class Joke
class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass

# Class A which gets joke from JokeAPI
class A(Joke):
    def get_random_joke(self):
        response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
        if response.status_code == 200:
            joke = response.json().get("joke")
            return joke
        else:
            return "Failed to fetch joke"

# Class B which gets joke from Official Joke API
class B(Joke):
    def get_random_joke(self):
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            joke = f'{joke_data["setup"]} - {joke_data["punchline"]}'
            return joke
        else:
            return "Failed to fetch joke"

# Class C which gets joke from JokeAPI
class C(Joke):
    def get_random_joke(self):
        response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        if response.status_code == 200:
            joke = response.json().get("joke")
            return joke
        else:
            return "Failed to fetch joke"

# Main function to test the classes
if __name__ == "__main__":
    joke_sources = [A(), B(), C()]
    
    for idx, source in enumerate(joke_sources, start=1):
        print(f"Joke from source {idx}: {source.get_random_joke()}")
