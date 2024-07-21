#!/usr/bin/python3

import requests

def distance_matrix(client, origins, destinations, mode="driving", language=None, units=None):
    """
    This function calculates the distance between origins and destinations using the Google Distance Matrix API.

    Args:
    origins: List of origin addresses or coordinates.
    destinations: List of destination addresses or coordinates.
    mode: Travel mode for which to calculate distance (driving, bicycling, transit, etc.). Defaults to "driving".

    Returns:
    A dictionary containing the distance matrix results or an error message.
    """
    # Build the request URL
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    api_key = "YOUR_API_KEY"

    # Add parameters to the request
    params = {
        "origins": "|".join(origins),
        "destinations": "|".join(destinations),
        "mode": mode,
        "language": language,
        "units": units,
        "key": api_key,
    }
    # Send the request and handle response
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract distance and duration information
        results = []
        for row in data['rows']:
            for element in row['elements']:
                distance_text = element['distance']['text']
                distance_value = element['distance']['value']
                duration_text = element['duration']['text']
                duration_value = element['duration']['value']
                results.append({
                    'distance_text': distance_text,
                    'distance_value': distance_value,
                    'duration_text': duration_text,
                    'duration_value': duration_value
                })
        return results
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
