"""
This module handles every request that is related to the User object.

It has the following functions

- signup
- login
- verify_email
- reset_password
- get_user
- get_current_user
- update_user
- get_users
- delete_user
"""

# imports

import requests
import json

from .meta import HOST_URL, HEADERS


def signup(data: dict):
    """
    Registers a new User instance.

    :data => a dict object containing the values for various fields to be stored on the database.

    Additional fields can be passed to the data.
    :return => Response for the API request
    """

    endpoint = f"{HOST_URL}/parse/users"

    response = requests.post(endpoint, headers=HEADERS, data=json.dumps(data))

    return response.json()


def login(username: str, password: str):
    """
    Logs an already registered user into the application.

    :username => username of the registered user during registration.
    :password => password of the registered user during registration
    :return => Response for the API request
    """

    endpoint = f"{HOST_URL}/parse/login"

    data = {
        "username": username,
        "password": password
    }

    response = requests.post(endpoint, headers=HEADERS, data=json.dumps(data))

    return response.json()


def verify_email(email: str):
    """
    Verify a users email after registration.
    :email => Email of the user to be verified.
    """

    endpoint = f"{HOST_URL}/parse/verificationEmailRequest"

    data = {"email": email}

    response = requests.post(endpoint, headers=HEADERS, data=json.dumps(data))

    return response.json()


def reset_password(email: str):
    """
    Initiate password reset for users who have emails associated with their account.
    """

    endpoint = f"{HOST_URL}/parse/requestPasswordReset"

    data = {"email": email}

    response = requests.post(endpoint, headers=HEADERS, data=json.dumps(data))

    return response.json()


def get_user(user_id: str):
    """
    Returns detail about the user with the given user_id.
    """

    endpoint = f"{HOST_URL}/parse/users/{user_id}"

    response = requests.get(endpoint, headers=HEADERS)

    return response.json()


def get_current_user(session_token: str):
    """
    Returns the current logged in user. The user with the provided session token will be returned.
    """

    endpoint = f"{HOST_URL}/parse/users/me"

    HEADERS["X-Parse-Session-Token"] = session_token

    response = requests.get(endpoint, headers=HEADERS)

    # delete the session token from the headers once the request is completed

    del HEADERS["X-Parse-Session-Token"]

    return response.json()


def update_user(user_id: str, session_token: str, data: dict):
    """
    Updates the user with the provided id.
    Returns the updated data.
    """

    endpoint = f"{HOST_URL}/parse/users/{user_id}"

    HEADERS["X-Parse-Session-Token"] = session_token

    requests.put(endpoint, headers=HEADERS, data=json.dumps(data))

    # delete the session token from the headers once the request is completed

    del HEADERS["X-Parse-Session-Token"]

    response = get_user(user_id=user_id)

    return response


def get_users():
    """
    Returns all the users in the database.
    """

    endpoint = f"{HOST_URL}/parse/users/"

    response = requests.get(endpoint, headers=HEADERS)

    return response.json()


def delete_user(user_id: str, session_token: str):
    """
    Deletes a user from the database.
    """

    endpoint = f"{HOST_URL}/parse/users/{user_id}"

    HEADERS["X-Parse-Session-Token"] = session_token

    response = requests.delete(endpoint, headers=HEADERS)

    # delete the session token from the headers once the request is completed

    del HEADERS["X-Parse-Session-Token"]

    return response.json()
