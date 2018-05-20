# Nexmo SMS Webhook

Simple callback service to receive SMS from [Nexmo](https://www.nexmo.com/) number and then send an email with it's content.

Built with Python, Flask and Mailgun API.

## Requirements

- Python 3
- [Nexmo number](https://dashboard.nexmo.com/buy-numbers) with SMS feature
- [Mailgun](https://www.mailgun.com) account

## Installation

### Clone Project

```sh
git clone https://github.com/taiyeoguns/nexmo-sms-webhook.git nexmo-sms-webhook
```

### Install Requirements

With a [virtualenv](https://virtualenv.pypa.io/) already set-up, install the requirements with pip:

```sh
pip install -r requirements.txt
```

### Add details in `.env` file

Create `.env` file from example file and maintain necessary details in it e.g. Mailgun API Key,  domain, email address to send to etc

```sh
cp .env.example .env
```

### Start the server

Start the Flask web server by running:

```sh
python run.py
```

Server should usually be started at `http://localhost:5000`

### Expose for external access

Use a tool like [ngrok](https://ngrok.com/) to make the local server available to the internet:

```sh
ngrok http 5000
```

This will expose a link such as: `https://r4nd0m1d.ngrok.io` that can be used in Nexmo Webhook URL configuration.