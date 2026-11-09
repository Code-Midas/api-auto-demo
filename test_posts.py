import pytest

@pytest.mark.parametrize("post_data", [
    {"title": "Test 1", "body": "Body 1", "userId": 1},
    {"title": "Test 2", "body": "Body 2", "userId": 2},
])
def test_create_post(api_session, base_url, post_data):
    response = api_session.post(f"{base_url}/posts", json=post_data)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["title"] == post_data["title"]
    assert response_json["body"] == post_data["body"]
    assert response_json["userId"] == post_data["userId"]