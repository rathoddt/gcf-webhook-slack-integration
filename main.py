import requests
from requests.structures import CaseInsensitiveDict

def hello_http(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
i        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    print("Github Webhook Received")
    #url = "Slack channel url"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = '{"text":"Github code commited"}'
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)

