# Imports
from watson_developer_cloud import AlchemyLanguageV1
from dotenv import load_dotenv, find_dotenv
import json
import os

# Load .env
load_dotenv(find_dotenv())

alchemy_language = AlchemyLanguageV1(api_key=os.environ.get("ALCHEMY_SERVICE_KEY"))

# URL to pass
url = 'https://developer.ibm.com/watson/blog/2015/11/03/price-reduction-for-watson-personality-insights/'

# API Test
combined_operations = ['page-image', 'entity', 'keyword', 'title', 'author', 'taxonomy', 'concept', 'doc-emotion']

print(json.dumps(alchemy_language.combined(url=url, extract=combined_operations), indent=2))

