
from flask import Flask, render_template, request, redirect, abort
from flask_pymongo import PyMongo
from urllib.parse import urlparse
from config import Config
from models.cache_config import CacheConfig
from models.language import Language
from controllers.change_language import change_language
from controllers.time import contact_time

app_config = Config()

app = Flask(__name__)
app.config["MONGO_URI"] = app_config.MONGO_URI
mongo = PyMongo(app)


@app.route("/")
def redirect_to_language():
    language = request.accept_languages.best_match(["en", "pl"])

    if language == "pl":
        return redirect("/pl")
    return redirect("/en")


@app.route("/<language>")
def main(language):
    if language in ["pl", "en"]:
        change_language_url = change_language(request.url)

        return render_template("base.html",
                               app_cfg = CacheConfig().get_config(mongo),
                               language = language,
                               home_page_url = urlparse(request.url).path[:3],
                               language_cache = Language().get_base(mongo = mongo, language = language),
                               change_language_url = change_language_url,
                               content=render_template("about.html",
                                                       language_cache = Language().get_about(mongo = mongo, language = language))
                               )
    else:
        abort(404)


@app.route("/<language>/about")
def about(language):
    if language in ["pl", "en"]:
        change_language_url = change_language(request.url)

        # if request.headers.get("HX-Request"):
        #     return render_template("about.html",
        #                            language_cache = Language().get_about(mongo = mongo, language = language))

        return render_template("base.html",
                               app_cfg = CacheConfig().get_config(mongo),
                               language = language,
                               home_page_url = urlparse(request.url).path[:3],
                               language_cache = Language().get_base(mongo = mongo, language = language),
                               change_language_url = change_language_url,
                               content=render_template("about.html",
                                                       language_cache = Language().get_about(mongo = mongo, language = language))
                               )
    else:
        abort(404)


@app.route("/<language>/portfolio")
def portfolio(language):
    if language in ["pl", "en"]:
        change_language_url = change_language(request.url)

        # if request.headers.get("HX-Request"):
        #     return render_template("portfolio.html",
        #                            language_cache = Language().get_portfolio(mongo = mongo, language = language))

        return render_template("base.html",
                               app_cfg = CacheConfig().get_config(mongo),
                               language = language,
                               language_cache = Language().get_base(mongo = mongo, language = language),
                               change_language_url = change_language_url,
                               home_page_url = urlparse(request.url).path[:3],
                               content=render_template("portfolio.html",
                                                       language_cache = Language().get_portfolio(mongo = mongo, language = language)
                                                       )
                               )
    else:
        abort(404)


@app.route("/<language>/contact")
def contact(language):
    if language in ["pl", "en"]:
        change_language_url = change_language(request.url)

        # if request.headers.get("HX-Request"):
        #     return render_template("contact.html",
        #                            language_cache = Language().get_contact(mongo = mongo, language = language))

        return render_template("base.html",
                               app_cfg = CacheConfig().get_config(mongo),
                               language = language,
                               language_cache = Language().get_base(mongo = mongo, language = language),
                               change_language_url = change_language_url,
                               home_page_url = urlparse(request.url).path[:3],
                               content=render_template("contact.html",
                                                       language_cache = Language().get_contact(mongo = mongo, language = language),
                                                       time = contact_time())
                               )
    else:
        abort(404)



@app.errorhandler(404)
def page_not_found(error):
    change_language_url = change_language(request.url)
    print(change_language_url)
    return render_template("base.html",
                           app_cfg = CacheConfig().get_config(mongo),
                           language = "pl",
                           change_language_url = "/pl",
                           home_page_url = "/pl",
                           language_cache = Language().get_base(mongo = mongo, language = "pl"),
                           content=render_template("404.html")), 404



@app.route("/send-email", methods=["POST"])
def test():
    print(request.values)
    return render_template("messageError.html")