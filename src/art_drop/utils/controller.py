"""
controller.py
by HundredVisionsguy
Does all the work behind the scenes.

For Error handling with requests, refer to the following article:
https://medium.com/@PythonWithPurpose/
python-api-error-handling-handle-errors-like-a-pro-a0da2899bf71

NOTE: I stored it in the Programming 3 folder in classes
"""

import json
import logging
import pathlib
import requests as re

COLLECTIONS_BASE_API = "https://api.artic.edu/api/v1/"


def make_api_call(base_url: str, endpoint="", query="") -> str:
    """makes an api call to url and returns data or error message
    
    Args:
        base_url: the API url to call
        endpoint: the endpoint (if provided) with a trailing slash
        query: the search term (if provided)
    
    Returns:
        str: the text of the returned data OR an error message if present
    """
    # make sure endpoint has trailing slash
    if endpoint and endpoint.strip()[-1] != "/":
        endpoint += "/"

    url = base_url + endpoint
    if query:
        url += "search?q=" + query
    
    try:
        response = re.get(url, timeout=5)

        # Raises an error for 4xx and 5xx status codes
        response.raise_for_status()
        if response.ok:
            return response.text
    except re.exceptions.ConnectionError:
        return "❌ ERROR: Connection failed — check your internet or the URL"
    except re.exceptions.Timeout:
        return "⏰ ERROR: Request timed out — the server is too slow"
    except re.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code == 401:
            return "🔐 ERROR: Unauthorized — check your API key"
        elif status_code == 404:
            return "🔍 ERROR: Not found — check the endpoint URL"
        elif status_code == 429:
            return " ERROR:  Rate limited — slow down your requests"
        elif status_code >= 500:
            return "💥 ERROR:  Server error — try again later"
        else:
            return f"ERROR: HTTP Error {status_code}"
    except re.exceptions.RequestException as e:
        return f"❌ ERROR:  Unexpected error: {e}"


def store_data(data: str, filename: str) -> str:
    """store data as file type
    
    Args:
        data: the data you want to store in a file
        filename: the name of the file you want to store
    
    Returns:
        str: success or failure if a string (might change later)
    """
    # get filename & store it in the data folder
    file_path = pathlib.Path(f"data/{filename}")

    # try to write to the file
    try:
        with file_path.open(mode="w") as file:
            file.write(data)
        return "Success!"
    except OSError as error:
        logging.error("Writing to file %s failed due to: %s",
                      file_path,
                      error)


def get_data(filename: str) -> str:
    """pull the data from the filename"""
    file_path = pathlib.Path(f"data/{filename}")

    with file_path.open(mode="r") as file:
        contents = file.read()
        print(type(contents))
    return contents
              

def artist_search(artist: str) -> str:
    """returns search info on artist"""
    raw_results = make_api_call(COLLECTIONS_BASE_API, "artists/", artist)

    # I recommend you store the results if successful (in raw form)

    # Clean up the results (using another function)
    
    return raw_results


if __name__ == "__main__":
    # Build URL for API call
    collections_base_api = "https://api.artic.edu/api/v1/"
    endpoint = "artworks"
    search_term = "manet"
    result = make_api_call(collections_base_api, endpoint, search_term)
    if "ERROR" in result:
        print(result)
        
        # Pull up from data a previous json file
        data = get_data("api_result.json")
    else:
        # Try and store data
        outcome = store_data(result, "api_result.json")
        print(outcome)
    data = get_data("api_result.json")
    print(data)