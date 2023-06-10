import requests
import requests_mock

# Create a requests_mock instance
mock = requests_mock.Mocker()

# Define the mock response
mock_response = {
    "status": "success",
    "message": "Mocked response"
}

# Register the mock response for the URL
url = "https://example.com/api/endpoint"
mock.get(url, json=mock_response)

# Start the mocking
with mock:
    # Make the GET request (which will be intercepted by the mock)
    response = requests.get(url)

# Check the response
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"GET request failed with status code: {response.status_code}")
