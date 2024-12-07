from pytest import fixture

from app import create_app


@fixture
def app():
    application = create_app()
    application.config.update({"TESTING": True})
    yield application  # return


@fixture
def client(app):
    return app.test_client()
