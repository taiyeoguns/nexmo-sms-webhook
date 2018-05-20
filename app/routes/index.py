from app import app
from flask import Flask, request
import os
import requests


@app.route('/', methods=['GET'])
def root():
    """ retrieves response data from nexmo and sends email """

    if 'msisdn' in request.args:

    	sender = request.args['msisdn']
    	msg_id = request.args['messageId']
    	received = request.args['message-timestamp']
    	text = request.args['text']

    
    	# build request components
    	url = 'https://api.mailgun.net/v3/{0}/messages'.format(os.getenv('MAILGUN_DOMAIN'))
    	auth = ('api', os.getenv('MAILGUN_API_KEY'))
    	data = {
    		'from':	os.getenv('FROM_EMAIL'),
    		'to': os.getenv('TO_EMAIL'),
    		'subject': 'SMS from Nexmo',
    		'text': 'From: {0} | Received: {1} | Message: {2}'.format(sender, received, text),
    		'html': 'From: {0} <br />Received: {1}<br />Message: {2}'.format(sender, received, text)
    	}

    	# make request
    	send_req = requests.post(url, auth=auth, data=data)
    
    # return 200 status code to Nexmo
    return ('', 200)