import requests

# Create the API URL
url = f"http://api.weatherapi.com/v1/forecast.json?key=f59a323ce8ad472a9dd213908231908&q=Montreal"

# Send a GET request to the API
response = requests.get(url)


def get_current_temp():
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data["current"]["temp_c"]
    else:
        return "Failed to retrieve weather information"
