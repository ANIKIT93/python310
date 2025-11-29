import requests


def fetch_data_from_api(endpoint, params=None, headers=None):
    """
    Fetch data from a given API endpoint.

    Args:
        endpoint (str): The API endpoint URL.
        params (dict, optional): Query parameters for the API request.
        headers (dict, optional): Headers for the API request.

    Returns:
        dict: The JSON response from the API.
    """
    try:
        response = requests.get(endpoint, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def post_data_to_api(endpoint, data=None, headers=None):
    """
    Post data to a given API endpoint.

    Args:
        endpoint (str): The API endpoint URL.
        data (dict, optional): The data to be sent in the POST request.
        headers (dict, optional): Headers for the API request.
    
    Returns:
        dict: The JSON response from the API.
    """
    try:
        response = requests.post(endpoint, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        print "Yes"
        return None