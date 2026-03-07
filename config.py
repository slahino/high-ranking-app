from datetime import datetime
import os

VOTE_END_DATE = datetime(2026, 3, 10, 14, 0, 0)

VOTE_START_DATE = datetime(2026, 3, 10, 8, 0, 0)

BASE_URL = "https://vote-condorcet-belevedere.onrender.com"
RESEND_API_KEY = os.environ.get("RESEND_API_KEY")