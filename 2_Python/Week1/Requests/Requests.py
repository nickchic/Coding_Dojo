#this grabs my latest reddit comment and prints it as text.
import requests
req = requests.get('http://www.reddit.com/user/nickchic/overview/.json')
req.text
data = req.json()
print data['data']['children'][0]['data']['body']
