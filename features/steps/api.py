from behave import *
import requests

response = None

url = "https://httpbin.org/get"

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
