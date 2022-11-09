"""
This program implements translation from english to french and vice versa
using IBM Watson Language Translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """Implements translation from english to french"""
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Implements translation from french to english"""
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()['translations'][0]['translation']
    return english_text
