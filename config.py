from datetime import datetime
import os

VOTE_END_DATE = datetime(2026, 3, 25, 18, 0, 0)

BASE_URL = os.environ.get("BASE_URL")
RESEND_API_KEY = os.environ.get("RESEND_API_KEY")