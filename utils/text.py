import json

j = json.load(open("app.json", "r", encoding="utf-8"))['app_data']


def text(key: str):
    """b Function that gets the text for the bot from text.json
    Args:
        key (str): [key for the json to find the right piece of text]
    Returns:
        [str]: [Text from text.json]
    """
    return j["texts"][key]


def button(key: str):
    """b Function that gets the text of a button in the bot from text.json
    Args:
        key (str): [key for the json to find the right piece of text]
    Returns:
        [str]: [Text from text.json]
    """
    return j["buttons"][key]
