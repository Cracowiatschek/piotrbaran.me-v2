
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from urllib.parse import urlparse
from config import Config
from models.cache_config import CacheConfig
from models.language import Language
from controllers.check_config import check_config

app_config = Config()

app = Flask(__name__)
app.config["MONGO_URI"] = app_config.MONGO_URI
mongo = PyMongo(app)
CACHE: dict = {}
LANGUAGE_CACHE: dict = {
    "pl":{},
    "en":{}
}


@app.route("/")
def redirect_to_language():
    language = request.accept_languages.best_match(["en", "pl"])
    CACHE["last_url"] = urlparse(request.url).path
    print(CACHE["last_url"])
    if "language" not in CACHE:
        CACHE["language"] = language

    if language == "pl":
        return redirect("/pl")
    else:
        return redirect("/en")


@app.route("/<language>")
def main(language):
    if language in ["pl", "en"]:
       CACHE["last_url"] = urlparse(request.url).path
    print(CACHE["last_url"])
    if "app_cfg" not in CACHE.keys() and len(LANGUAGE_CACHE["pl"]) == 0 and len(LANGUAGE_CACHE["en"]) == 0:
        CACHE["language"] = language
        return redirect(f"/api/get_config/")
    if language == "pl":
        change_language_url = "/en"
    else:
        change_language_url = "/pl"

    return render_template("base.html",
                           app_cfg = CACHE["app_cfg"],
                           language = language,
                           language_cache = LANGUAGE_CACHE[language]["base.html"],
                           change_language_url = change_language_url,
                           content=render_template("about.html",
                                                   language_cache = LANGUAGE_CACHE[language]["about.html"])
                           )


@app.route("/<language>/about")
def about(language):
    CACHE["last_url"] = urlparse(request.url).path
    print(CACHE["last_url"])
    if "app_cfg" not in CACHE.keys() and len(LANGUAGE_CACHE) == 0:
        CACHE["language"] = language
        return redirect(f"/api/get_config/{language}")

    if request.headers.get("HX-Request"):
        return render_template("about.html",
                               language_cache = LANGUAGE_CACHE["about.html"])
    return render_template("base.html",
                           app_cfg = CACHE["app_cfg"],
                           language = CACHE["language"],
                           language_cache = LANGUAGE_CACHE["base.html"],
                           content=render_template("about.html",
                                                   language_cache = LANGUAGE_CACHE["about.html"])
                           )


@app.route("/<language>/portfolio")
def portfolio(language):
    CACHE["last_url"] = urlparse(request.url).path
    print(CACHE["last_url"])
    if "app_cfg" not in CACHE.keys() and len(LANGUAGE_CACHE) == 0:
        CACHE["language"] = language
        return redirect(f"/api/get_config/{language}")

    if request.headers.get("HX-Request"):
        return render_template("portfolio.html",)
    return render_template("base.html", content=render_template("portfolio.html") )


@app.route("/<language>/contact")
def contact(language):
    CACHE["last_url"] = urlparse(request.url).path
    print(CACHE["last_url"])
    if "app_cfg" not in CACHE.keys() and len(LANGUAGE_CACHE) == 0:
        CACHE["language"] = language
        return redirect(f"/api/get_config/{language}")

    if request.headers.get("HX-Request"):
        return render_template("contact.html")
    return render_template("base.html", content=render_template("contact.html"))


@app.route("/api/get_config/")
def get_data():
    print("x")
    cache_config = CacheConfig()
    lang_config = Language()

    global CACHE
    CACHE["app_cfg"] = cache_config.get_config(mongo)
    global LANGUAGE_CACHE
    LANGUAGE_CACHE["pl"]["base.html"] = lang_config.get_base(mongo = mongo, language = "pl")
    LANGUAGE_CACHE["pl"]["about.html"] = lang_config.get_about(mongo = mongo, language = "pl")
    LANGUAGE_CACHE["en"]["base.html"] = lang_config.get_base(mongo = mongo, language = "en")
    LANGUAGE_CACHE["en"]["about.html"] = lang_config.get_about(mongo = mongo, language = "en")
    return redirect(CACHE["last_url"])

@app.route("/language", methods=["POST"])
def change_language():
    if CACHE["language"] == "pl":
        CACHE["last_url"] = "/en" + CACHE["last_url"][3:]
        CACHE["language"] = "en"
        return redirect("/api/get_config/en")

    if CACHE["language"] == "en":
        CACHE["last_url"] = "/pl"+CACHE["last_url"][3:]
        CACHE["language"] = "pl"
        return redirect("/api/get_config/pl")


@app.errorhandler(404)
def page_not_found(error):
    CACHE["last_url"] = urlparse(request.url).path
    print(CACHE["last_url"])
    if "app_cfg" not in CACHE.keys() and len(LANGUAGE_CACHE) == 0:
        if "language" not in CACHE:
            CACHE["language"] = request.accept_languages.best_match(["en", "pl"])
            return redirect(f"/api/get_config/{CACHE["language"]}")
        else:
            return redirect(f"/api/get_config/{CACHE["language"]}")

    return render_template("base.html",
                           app_cfg = CACHE["app_cfg"],
                           language = CACHE["language"],
                           language_cache = LANGUAGE_CACHE["base.html"],
                           content=render_template("404.html")), 404