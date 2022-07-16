# 📑 Telegram Bot Template

This is a template repo for cloning and reusing to create custom telegram bots with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library in Python.

## Installation & usage

1. Clone the repo

```bash
$ git clone https://github.com/nuriddinislamov/telegram-bot-template my-bot
```

2. Go to project directory, create virtualenv and activate it

```bash
$ cd my-bot; python3 -m venv venv; source venv/bin/activate
```

3. Download and install all dependencies with `pip`

```bash
$ pip install -r requirements.txt
```

4.  Add an environment variable for bot's token. You can get one [here with BotFather](https://t.me/botfather).

    -   **❗️ Deprecated version**

        ```bash
        $ export BOT_TOKEN='your actual token'
        ```

    -   **👍 Recommended**
        Create a file with name `.env` (no name, just .env) and type in your bot's token as:

        `1. BOT_TOKEN='your actual token'`

    <br/>

5.  🎉 Great! Now run the bot and see the magic happen.

```bash
$ python3 bot.py
```

## Licence

This template is under [MIT](/LICENSE) license.

## Copyright

&copy; Nuriddin Islamov, 2021
