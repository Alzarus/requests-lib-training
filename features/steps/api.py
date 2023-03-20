from behave import *
import requests
import os

response = None

# url = os.getenv('URL')
url = "https://jsonplaceholder.typicode.com/posts/"

# https://jsonplaceholder.typicode.com/guide/
headers = {
    'Content-type': 'application/json; charset=UTF-8',
}

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}


@given('I get random data')
def step_impl(context):
    try:
        global response
        response = requests.request("GET", url)
    except:
        raise NotImplementedError


@then('I assert the success status code')
def step_impl(context):
    global response
    assert response.status_code == 200
