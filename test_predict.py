import requests

url = 'http://127.0.0.1:5000/predict'
data = [1807, 1, 2.8, 0, 1, 0, 27, 0.9, 186, 3, 4, 1270, 1366, 2396, 17, 10, 10, 0, 1, 1]

response = requests.post(url, json=data)
print("Response Text:", response.text)