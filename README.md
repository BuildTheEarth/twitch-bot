<div align="center">

<img width="128" src="assets/logo.gif" />

# twitch-bot

_The official Twitch chatbot used in our BTELive account._

</div>

## BuildTheEarth

Join us in this massive project as we recreate the Earth in Minecraft, in 1:1 scale, one block at a time. [**Discord Server**][invite]

## Modules

This assumes the prefix is `=`.

### Snippets

#### Usage

`=snippets`

Subcommands

-   **add:** Add a snippet (moderator/broadcaster only).
    `=snippets add <name> <language> <body>` 
-   **edit:** Edit a snippet (moderator/broadcaster only).
    `=snippets edit <name> <language> <body>`
-   **delete:** Delete a snippet (moderator/broadcaster only).
    `=snippets delete <name> <language>`
-   **language:** List all languages a snippet is tranlated to.
    `=snippets language <name>`

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/cAttte"><img src="https://avatars.githubusercontent.com/u/26514199?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cAttte</b></sub></a><br /><a href="https://github.com/BuildTheEarth/twitch-bot/commits?author=cAttte" title="Documentation">📖</a></td>
    <td align="center"><a href="http://xboxbedrock.github.io"><img src="https://avatars.githubusercontent.com/u/68715625?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Xbox</b></sub></a><br /><a href="https://github.com/BuildTheEarth/twitch-bot/commits?author=XboxBedrock" title="Code">💻</a> <a href="#projectManagement-XboxBedrock" title="Project Management">📆</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification. Contributions of any kind are welcome!

## Setup

We can offer almost no support on this as this is customized for BTE's needs.

This has only been tested on [Python 3.9.0](https://www.python.org/downloads/release/python-390/) and we cannot guarantee it works on older versions.

### Config

Rename `_config.json` to `config.json` and fill in all the fields:

-   **prefix:** the prefix for your bot, default `=`
-   **token:** your Twitch OAuth token (without the `oauth:`), can be created [here](https://twitchapps.com/tmi/)
-   **client_id:** your Twitch application client ID, you can create a Twitch application [here](https://dev.twitch.tv/console/apps)
-   **channel:** the Twitch IRC channel you want to join, simply the name of the Twitch channel your bot is intended for in all *lowercase*
-   **username:** the bot account's Twitch username in all *lowercase*

### Installation

To install the dependencies, you'll need [pip](https://pypi.org/project/pip/).

    pip install -r requirements.txt

To set up the database, run `createdb.py`:

    python createdb.py

### Running

In order to run the bot, you must have completed the config and installation steps. Run `bot.py` in order to start it:

    python bot.py

<!-- References -->

[invite]: https://discord.gg/QEkPmBy
