# imports

import os


HOST_URL = "https://parseapi.back4app.com"; # main endpoint for all requests

# Request headers for all requests.

HEADERS = {
    "Content-Type": "application/json",
    "X-Parse-Revocable-Session": "1",
    "X-Parse-Application-Id": os.environ.get("PARSER_APPLICATION_ID"),
    "X-Parse-Master-Key": os.environ.get("PARSER_MASTER_KEY"),
}


