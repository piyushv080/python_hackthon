print('Piyush Verma')
import requests

# install requests module using pip

response = requests.get("http://api.open-notify.org/astros.json")
my_response = response.json()

print(my_response)
print(type(my_response))
