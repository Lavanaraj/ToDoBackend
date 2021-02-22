import json
from to_do_api import *
import unittest

def test_login():
    response = app.test_client().post(
        '/login',
        data=json.dumps({
                "username":"Lavanaraj_2",
                "password":"9hKBX2jpJGw"
            }),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['result'] !=" "

    response = app.test_client().post(
        '/login',
        data=json.dumps({
                "username":"Lavanaraj_4",
                "password":"9hKBX2jpJGwqw"
            }),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['result'] =="Wrong password"

def test_save_new_node():
    response = app.test_client().post(
        '/save_new_node',
        data=json.dumps({
                "note":"Hi lavan note 08"
            }),
        content_type='application/json',
        headers={"content_type":'application/json',
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkxhdmFuYXJhal8xIiwiZXhwIjoxNjMzOTU4NDE0fQ.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8-IqZI4"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['message'] =="Note Saved Successfully!!!"

    response = app.test_client().post(
        '/save_new_node',
        data=json.dumps({
                "note":"Hi lavan note 08"
            }),
        content_type='application/json',
        headers={"content_type":'application/json',
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkxhdmFuYXJhal8xIiwiZXhwIjoxNjMzOTU4NDE0fQ.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['message'] =="Invalid JWT Token"

def test_update_note():
    response = app.test_client().post(
        '/update_note',
        data=json.dumps({
                "note":"Hi updated!!!!",
                "note_id":"60330d20163fbeae3828f0fd"
            }),
        content_type='application/json',
        headers={"content_type":'application/json',
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkxhdmFuYXJhal8xIiwiZXhwIjoxNjMzOTU4NDE0fQ.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8-IqZI4"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['message'] =="Note Update Successfully!!!"

    response = app.test_client().post(
        '/update_note',
        data=json.dumps({
                "note":"Hi updated!!!!",
                "note_id":"60330d20163fbeae3828f0fd"
            }),
        content_type='application/json',
        headers={"content_type":'application/json',
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkxhdmFuYXJhal8xIiwiZXhwIjoxNjMzOTU4NDE0fQ.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['message'] =="Invalid JWT Token"

def test_delete_note():
    response = app.test_client().post(
        '/delete_note',
        data=json.dumps({
                "note":"Hi updated!!!!",
                "note_id":"60330d20163fbeae3828f0fd"
            }),
        content_type='application/json',
        headers={"content_type":'application/json',
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkxhdmFuYXJhal8xIiwiZXhwIjoxNjMzOTU4NDE0fQ.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8-IqZI4"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['message'] =="Note Successfully Deleted!!!"

    response = app.test_client().post(
        '/delete_note',
        data=json.dumps({
            "note": "Hi updated!!!!",
            "note_id": "60330d20163fbeae3828f0f"
        }),
        content_type='application/json',
        headers={"content_type": 'application/json',
                 "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8-IqZI4"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['message'] == "Invalid JWT Token"


def test_change_archive():
    response = app.test_client().post(
        '/change_archive',
        data=json.dumps({
                "note_id":"60330d20163fbeae3828f0fd"
            }),
        content_type='application/json',
        headers={"content_type":'application/json',
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkxhdmFuYXJhal8xIiwiZXhwIjoxNjMzOTU4NDE0fQ.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8-IqZI4"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['message'] =="Note Archive Update Successfully!!!"

    response = app.test_client().post(
        '/change_archive',
        data=json.dumps({
            "note_id": "60330d20163fbeae3828f0fd"
        }),
        content_type='application/json',
        headers={"content_type": 'application/json',
                 "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8-IqZI4"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['message'] == "Invalid JWT Token"

def test_get_all_archived_nodes():
    response = app.test_client().get(
        '/get_all_archived_nodes',
        headers={"content_type":'application/json',
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkxhdmFuYXJhal8xIiwiZXhwIjoxNjMzOTU4NDE0fQ.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8-IqZI4"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['all_archived_notes'] ==[
                                    {
                                        "archive": True,
                                        "note": "Hi lavan note 08",
                                        "note_id": "6033121734725ec2438dd94d"
                                    }
                                ]

    response = app.test_client().get(
        '/get_all_archived_nodes',
        headers={"content_type": 'application/json',
                 "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8-IqZI4"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['message'] == "Invalid JWT Token"

def test_get_all_unarchived_nodes():
    response = app.test_client().get(
        '/get_all_unarchived_nodes',
        headers={"content_type":'application/json',
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkxhdmFuYXJhal8yIiwiZXhwIjoxNjMzOTYyMDg4fQ.hgI4Bi11vOgEYMzhOovClnjTuHwj0l5FPl-DneE2d74"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['all_unarchived_notes'] == [
                {
                    "archive": False,
                    "note": "Hi lavanaraj_2 note 01",
                    "note_id": "603342660efc2fef934faba8"
                }
            ]

    response = app.test_client().get(
        '/get_all_unarchived_nodes',
        headers={"content_type": 'application/json',
                 "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8-IqZI4"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['message'] == "Invalid JWT Token"


def test_get_all_nodes():
    response = app.test_client().post(
        '/get_all_nodes',
        headers={"content_type":'application/json',
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkxhdmFuYXJhal8yIiwiZXhwIjoxNjMzOTYyMDg4fQ.hgI4Bi11vOgEYMzhOovClnjTuHwj0l5FPl-DneE2d74"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code ==200
    assert data['message'] ==[
                {
                    "archive": True,
                    "note": "Hi lavanaraj_2 note 08",
                    "note_id": "6033422b0efc2fef934faba7"
                },
                {
                    "archive": False,
                    "note": "Hi lavanaraj_2 note 01",
                    "note_id": "603342660efc2fef934faba8"
                }
            ]

    response = app.test_client().get(
        '/get_all_nodes',
        headers={"content_type": 'application/json',
                 "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.q8Hley9Zk7fviU_xm2GCuAMmPkRsevWnY__H8-IqZI4"},
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['message'] == "Invalid JWT Token"
