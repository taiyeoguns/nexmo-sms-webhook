from app import app

from dotenv import load_dotenv
import os

#load dotenv
load_dotenv('.env')

app.run(debug=bool(os.getenv('DEBUG')))