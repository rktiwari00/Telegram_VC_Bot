HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["1570870"])
    API_HASH = environ["ea9e3824816fc7af42580d083374a438"]
    SUDO_CHAT_ID = int(environ["1001374839083"]) # Chat where the bot will play the music.
    SUDOERS = list(int(x) for x in environ.get("SUDOERS", "1214419455").split()) # Users which have special control over the bot.
    SESSION_STRING = environ["BQAohk3KnXsIEjAlWt6Khr6DJn_riYeeL-9KGuBepXNOnJiv6mUMOJx9BCDu3Rpc0aLz-Q297adMjM-nxBTv-57LusQORT6EIIEswBNshYAN9vu9LYoLIBhMp7vCIpQf82fX7s8T96AplMNrqrjqWi5jVFW5RXGADDjIBZ2M8TkoHSs-4b-0ixZTc1-wTPdxUCmUCPHhMpAnkt_iEw-bydUS4HXEu4hkxLEZveLmNl0N4RS3JprliJuJpp_GQc3EwpfLvw_5zvhBqQ9L3b96zpF7dOGN8kVS20-LLj6iHe2w-dZKnQ5UJTKJ4OnsLOkXQkOh_Q_RKsW1ruzaznsFHBUpaKarxAE"] # Check Readme for session

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    SUDO_CHAT_ID = -1001485876964
    SUDOERS = [1243703097, 13216546]

# don't make changes below this line
ARQ_API = "https://thearq.tech"
