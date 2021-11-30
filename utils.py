import time
import logging
import requests

class WebsiteDownException(Exception):
	pass

def ping_website(address, timeout = 20):
	try:
		response = requests.head(address, timeout = timeout)
		if response.status_code >= 400:
			logging.warning("Le site %s retourne un status_code = %s" % (address, response.status_code))
			raise WebsiteDownException()
	except requests.exceptions.RequestException:
		logging.warning("Timeout expiré pour le site %s" % address)
		print("Timeout expiré pour le site %s" % address)
		raise WebsiteDownException()


def notify_owner(address):
	logging.info("Notification du propriétaire du site %s " % address)
	time.sleep(0.5)

def check_website(address):
	try:
		ping_website(address)
	except WebsiteDownException:
		notify_owner(address)