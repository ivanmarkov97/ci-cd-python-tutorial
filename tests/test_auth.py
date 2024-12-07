#  test 1 - test get /auth

from flask import session


def test_auth_login(client):
    response = client.get("/auth/")
    assert response.status_code == 200
    response_text = response.text
    assert "login" in response_text
    assert "password" in response_text
    assert "Log in" in response_text


def test_auth_login_success(client):
    response = client.post(
        "/auth/",
        data={"login": "my-login", "password": "my-password"},
        headers={"Content-Type": "multipart/form-data"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.history[0].status_code == 302
    assert response.request.path == "/"


def test_auth_login_session(client):
    with client:
        _ = client.post(
            "/auth/",
            data={"login": "my-login", "password": "my-password"},
            headers={"Content-Type": "multipart/form-data"},
            follow_redirects=True,
        )

        assert "user_id" in session
        assert "role" in session
