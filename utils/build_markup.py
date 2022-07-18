from telegram import KeyboardButton
from typing import Union, List


def build_markup(
    buttons: List[KeyboardButton],
    n_cols: int,
    header_buttons: Union[KeyboardButton,
                          List[KeyboardButton]] = None,
    footer_buttons: Union[KeyboardButton,
                          List[KeyboardButton]] = None) -> List[List[KeyboardButton]]:
    markup = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        markup.insert(0, header_buttons if isinstance(
            header_buttons, list) else [header_buttons])
    if footer_buttons:
        markup.append(footer_buttons if isinstance(
            footer_buttons, list) else [footer_buttons])
    return markup
