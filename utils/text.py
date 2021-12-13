import yaml


def text(key: str):
    """
    Reads texts from locale.yaml file. Return the string of the given key.
    """
    
    text_file = open('locale.yaml')
    contents = yaml.load(text_file, Loader=yaml.FullLoader)
    return contents['texts'][key]
