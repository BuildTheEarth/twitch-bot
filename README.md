# BTELiveBOT
This is the official bot that runs on the BTELiveBot account.

# Modules
Currently the only Module that this has is snippets

Note this assumes the prefix is `=`

Usage

`=snippets`

Subcommands

• **add:** Add a snippet (moderator/broadcaster only). `=snippets add <name> <language> <body>` 
• **edit:** Edit a snippet (moderator/broadcaster only). `=snippets edit <name> <language> <body>`
 • **delete:** Delete a snippet (moderator/broadcaster only). `=snippets delete <name> <language>`
  • **language:** List all languages a snippet is tranlated to. `=snippets language <name>`

# Setup
We can offer almost no support on this as this is customised for BTE's needs
This has only been tested on [Python 3.9.0](https://www.python.org/downloads/release/python-390/) and we cannot guarantee it works on older versions
___


**Config**

 Rename `_config.json` to `config.json` and fill in all the fields

**Config fields**

"prefix" - the prefix for your bot, default `=`

"token" - your Twitch OAuth token (without the `oauth:`), can be created [here](https://twitchapps.com/tmi/)

"client_id" - your Twitch application client ID, you can create a Twitch application [here](https://dev.twitch.tv/console/apps)

"channel" -  the Twitch IRC channel you want to join, simply the name of the Twitch channel your bot is intended for in all *lowercase*

"username" -  the bot account's Twitch username in all *lowercase*
___
**Installation**

To install the dependencies you need [pip](https://pypi.org/project/pip/)

    pip install -r requirements.txt

To create the database you need to run `createdb.py`

    python createdb.py
___
**Running**
In order to run the bot you must have completed the config and installation

You need to run `bot.py` in order to start it

    python bot.py

