import yaml
import requests
import string
import random
from neo4j_driver import HelloWorldExample

class LinkedConnectionsGraphView:
	def __init__(self):
		with open("credentials.yaml") as file:
			credentials = yaml.load(file, Loader=yaml.FullLoader)
			self.client_id = credentials['CLIENT_ID']
			self.client_secret = credentials['CLIENT_SECRET']
			self.auth_code = credentials['AUTH_CODE']
			self.access_token_url = credentials['ACCESS_TOKEN_URL']
			self.redirect_uri = credentials['REDIRECT_URI']
			self.authoriztaion_url = credentials['AUTHORIZATION_URL']
			self.linkedin_my_details_api = credentials['LINKED_IN_MY_DETAILS']
			

	def linkedin_auth(self):
		letters = string.ascii_lowercase
		CSRF_TOKEN = ''.join(random.choice(letters) for i in range(24))
		auth_params = {
			   'response_type': 'code',
			   'client_id': self.client_id,
			   'redirect_uri': self.redirect_uri,
			   'state': CSRF_TOKEN,
			   'scope': 'r_liteprofile,r_emailaddress'}
		response = requests.get(self.authoriztaion_url,params = auth_params)
		print(response.url)

	def get_access_token(self):
		data = {
			'grant_type': 'authorization_code',
			'code': self.auth_code,
			'redirect_uri': self.redirect_uri,
			'client_id': self.cliend_id,
			'client_secret': self.client_secret
		}
		response = requests.post(self.access_token_url, data=data, timeout=60)
		response = response.json()
		print(response)
		
		access_token = response['access_token']
		print ("Access Token:", access_token)
		print ("Expires in (seconds):", response['expires_in'])
		return access_token

	def get_my_details():
		access_token = self.get_access_token()
		params = {'oauth2_access_token': access_token}      
		response = requests.get(self.linkedin_my_details_api, params = params) 


		


if __name__ == "__main__":
	linkedin_graph_view = LinkedConnectionsGraphView()
	# linkedin_graph_view.linkedin_auth()
	linkedin_graph_view.get_my_details()
	neo4j_driver = Neo4jDriver()

