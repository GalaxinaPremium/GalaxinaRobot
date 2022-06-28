# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Galaxina_Bot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 11074927  # integer value, dont use ""
    API_HASH = "9e7366e2f9faa01ae581f80adc429065"
    TOKEN = "2062211332:AAHvwYpVZZxOtgldZS-CWe0yA7Tf95LEkzg"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1282754256  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "AdityaHalder"
    SUPPORT_CHAT = "GalaxinaSupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001602975376
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001602975376
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://bxwkmxni:EOlujTSV-GNDHSK8PMTkjL21Yx-IXgh7@kesavan.db.elephantsql.com/bxwkmxni"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "z5w0J5UfQU_g9y4_o0Z5YjbF2bZ4ltekVSihsB4DS9MJNPtt7ztyWMJkw_TPPdLo"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@adityadiscus"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = None
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = None
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = None
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = None
    WOLVES = None
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "D60NS2STEZQJR9KX"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "XYRWERF4VR6I"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "https://wall.alphacoders.com/api2.0/get.php?method=wallpaper_info&id=865098"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
