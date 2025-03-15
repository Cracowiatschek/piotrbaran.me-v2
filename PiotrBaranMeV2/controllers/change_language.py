from urllib.parse import urlparse

def change_language(url: str) -> str:
    get_url: str = urlparse(url).path  #parse url

    destination_url: str = "/pl" + get_url[3:] # if not pl redirect to pl
    if  get_url[:3] == "/pl": # if pl redirect to en
        destination_url = "/en"+get_url[3:]

    return destination_url