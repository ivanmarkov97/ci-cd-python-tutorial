from flask import session


def test_auth_login(client):
    response = client.get("/auth/")
    assert response.status_code == 200
    assert "login" in response.text
    assert "password" in response.text
    assert "Log in" in response.text


def test_auth_success_redirect(client):
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
    assert "Hello world" in response.text


def test_auth_success_session(client):
    with client:
        _ = client.post(
            "/auth/",
            data={"login": "my-login", "password": "my-password"},
            headers={"Content-Type": "multipart/form-data"},
            follow_redirects=True,
        )
        assert "user_id" in session
        assert "role" in session
