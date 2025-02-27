from flask import redirect

def check_config(cache: dict, language_cache: dict, url: str, language:str):
    print(cache, language_cache, url)

    if len(cache) == 0 and len(language_cache) == 0:
        print("Passed")
        return redirect(f"/api/get_config/{language}&{url}")
    else:
        pass
