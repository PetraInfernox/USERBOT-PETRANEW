import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "6415149714").split()))

API_ID = int(os.getenv("API_ID", "25751782"))

API_HASH = os.getenv("API_HASH", "b76b8aa78b8f242eb9d25678d48cb199")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8051694317:AAG9TJLMW_ciz_mcxgU4i0d2gDU3g5Iz2EY")

OWNER_ID = int(os.getenv("OWNER_ID", "6415149714"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://PetraInfernox:Petra088@cluster0.9bqw9vu.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002331639417"))
