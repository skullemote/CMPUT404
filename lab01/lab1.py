import requests
#print(requests.__version__)
resp = requests.get("https://raw.githubusercontent.com/skullemote/CMPUT404/main/lab01/lab1.py")
print(resp.text)