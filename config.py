import os


class Config(object):
    API_HASH = os.environ.get("API_HASH","9830058")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6624482904:AAFqqYY1tKNWojNu4OOZeINKClKKsKtQuuI")
    TELEGRAM_API = os.environ("TELEGRAM_API","908e8bff7c8f6ecd5d0ab989f78134fc")
    OWNER = os.environ.get("OWNER", "6616684260")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "NoMoreFiles")
    PASSWORD = os.environ.get("PASSWORD", "tomen")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Nons:Nons@cluster0.eeydztb.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1001923809898")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
