from urllib.parse import urlparse

def change_language(url: str) -> str:
    get_url: str = urlparse(url).path

    destination_url: str = "/pl" + get_url[3:]
    if  get_url[:3] == "/pl":
        destination_url = "/en"+get_url[3:]

    return destination_url