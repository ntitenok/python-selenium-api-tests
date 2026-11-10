import requests

URL = 'https://demoqa.com/BookStore'
ENDPOINT = '/v1/Book'
isbn = 9781449325862
params = {
    'ISBN': isbn
    }


def test_get_book():
    response = requests.get(URL + ENDPOINT, params=params)
    assert response.status_code == 200
    assert response.json()['isbn'] == str(isbn)
    print(response.json()['title'])
    print(response.headers)