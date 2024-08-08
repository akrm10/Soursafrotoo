from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = "21209802" 
    API_HASH = "eed1c8387c6ee80009527e07d9d58cc0"
    # the name to display in your alive message
    ALIVE_NAME = "عقيد"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "https://t.me/t_t_t_h"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "Your value"
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "6807629743:AAHsnFL_eb9F-egK2yjvvxVgKWIcQIhpNDA"
    TG_BOT_USERNAME = "Gmail_huntingbot"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002243902699
    # command handler
    COMMAND_HAND_LER = "6716174264"
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = [6716174264]
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
