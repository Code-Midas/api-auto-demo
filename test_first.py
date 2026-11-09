import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_returns_200():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_post_contains_expected_fields():
    response = requests.get(f"{BASE_URL}/posts/1")
    body = response.json()
    assert "id" in body
    assert body["id"] == 1
    assert "title" in body