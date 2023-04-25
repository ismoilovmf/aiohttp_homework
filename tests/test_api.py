import os
import time

import requests

API_URL = os.getenv("API_URL", 'http://127.0.0.1:8080')


def test_hello():
    resp = requests.get(f'{API_URL}/hello')
    assert resp.status_code == 200
    assert resp.json() == {
        'hello': 'world'
    }


def test_get_user(create_user):
    resp = requests.get(f'{API_URL}/users/{create_user["id"]}')    # 'http://127.0.0.1:8080/users/5'
    assert resp.status_code == 200
    assert create_user['email'] == resp.json()['email']


def test_create_user():
    user_data = {
            'email': f'test_email_{time.time()}@gmail.com',
            'password': '12345678'
        }
    resp = requests.post(f'{API_URL}/users', json=user_data)
    assert resp.status_code == 200
    assert resp.json()['email'] == user_data['email']


def test_delete_user(create_user):
    user = create_user
    resp = requests.delete(f'{API_URL}/users/{user["id"]}')
    assert resp.status_code == 200
    assert resp.json()['status'] == 'deleted'


def test_get_adv(create_adv):
    response = requests.get(f'{API_URL}/advs/{create_adv["id"]}')
    assert response.status_code == 200
    assert create_adv['id'] == response.json()['id']


def test_create_adv(create_adv):
    data = {
        'title': 'test_title',
        'description': 'test_description',
        'user_id': create_adv['id'],
    }
    response = requests.post(f'{API_URL}/advs', json=data)
    assert response.status_code == 200
    assert response.json()['title'] == data['title']


def test_delete_adv(create_adv):
    response = requests.delete(f'{API_URL}/advs/{create_adv["id"]}')
    assert response.status_code == 200
    assert response.json()['status'] == 'deleted'