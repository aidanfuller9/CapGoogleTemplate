import os

def getSecrets():
    secrets = {
        'MONGO_HOST':'mongodb+srv://aidanfuller9:aidancapstonestie@cluster0.sbhgbvv.mongodb.net/AIDANWEBSITE?retryWrites=true&w=majority',
        'MONGO_DB_NAME':'AIDANWEBSITE',
        'GOOGLE_CLIENT_ID': '1063142894012-t4rvcpgt8ho9mtpkf7g8iv15jk9dlebg.apps.googleusercontent.com',
        'GOOGLE_CLIENT_SECRET':'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',
        'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration"
        }
    return secrets