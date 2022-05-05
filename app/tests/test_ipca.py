# import requests
#
#
# def test_show_all_ipcas(app):
#     response = requests.get("http://localhost:5000/ipca")
#     assert response.status_code == 200
#
#
# def test_show_all_ipcas_json(app):
#     response = requests.get("http://localhost:5000/ipca")
#     assert response.headers["Content-Type"] == "application/json"
import pytest

from app.app import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_show_all_ipcas_status_code_200(client):
    response = client.get("/ipca/")
    assert response.status_code == 200


def test_show_all_ipcas_is_json(client):
    response = client.get("/ipca/")
    assert response.headers["Content-Type"] == "application/json"


def test_show_all_ipcas_last_year_status_code_200(client):
    response = client.get("/ipca/year/")
    assert response.status_code == 200


def test_show_all_ipcas_last_year_is_json(client):
    response = client.get("/ipca/year/")
    assert response.headers["Content-Type"] == "application/json"

