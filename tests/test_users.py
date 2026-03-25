from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_read_users_with_users(client, user, token):

    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(
        '/users/', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_create_user(client, token):
    response = client.post(
        '/users/',
        json={
            'username': 'ana',
            'email': 'ana@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'ana',
        'email': 'ana@example.com',
        'id': 2,
    }


def test_update_user(client, user, token):
    response = client.put(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'ana',
            'email': 'ana@example.com',
            'password': 'ana',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'ana',
        'email': 'ana@example.com',
    }


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
