import requests

response_anagram = requests.post('http://127.0.0.1:8000/api/anagram/', data={'first_word': 'word', 'second_word': 'dwor'})
print(response_anagram.json())
print(response_anagram.status_code)


response_not_anagram = requests.post(
    'http://127.0.0.1:8000/api/anagram/', data={'first_word': 'word', 'second_word': 'anagram'}
)
print(response_not_anagram.json())
print(response_not_anagram.status_code)
