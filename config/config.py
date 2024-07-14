from dotenv import load_dotenv
import os

load_dotenv()

PORT = os.environ.get("PORT")
AUTH_SERVICE = os.environ.get("AUTH_SERVICE")
VOCAB_SERVICE = os.environ.get("VOCAB_SERVICE")
GROUP_SERVICE = os.environ.get("GROUP_SERVICE")
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS")
