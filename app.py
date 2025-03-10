import os
from flask import Flask, render_template, request, redirect, abort, render_template_string
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
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
        language_cache = Language().get_portfolio(mongo = mongo, language = language)

        if "name" in request.args and request.headers.get("HX-Request"):
            return  render_template("portfolioDetails.html",
                                    product_name = request.args.get("name"),
                                    url = f"/{language}/portfolio?back=True",
                                    content=Language().get_portfolio_details(mongo, language, request.args.get("name")),
                                    badges="ready",
                                    buttons="ready"
                                    )
        elif "name" in request.args and "HX-Request" not in request.headers:
            return render_template("base.html",
                                   app_cfg = CacheConfig().get_config(mongo),
                                   language = language,
                                   language_cache = Language().get_base(mongo = mongo, language = language),
                                   change_language_url = change_language_url,
                                   home_page_url = urlparse(request.url).path[:3],
                                   content = render_template("portfolio.html",
                                                             language_cache = language_cache,
                                                             header = True,
                                                             content = render_template("portfolioDetails.html",
                                                                                       content = Language().get_portfolio_details(mongo, language, request.args.get("name")),
                                                                                       badges="ready",
                                                                                       buttons="ready",
                                                                                       url = f"/{language}/portfolio?back=True",
                                                                                       )
                                                             )
                                   )


        if "back" in request.args and request.headers.get("HX-Request"):
            return render_template("portfolio.html",
                                   language_cache = language_cache,
                                   content = render_template("portfolioMenu.html",
                                                             language_cache = language_cache)
                                   )

        return render_template("base.html",
                               app_cfg = CacheConfig().get_config(mongo),
                               language = language,
                               language_cache = Language().get_base(mongo = mongo, language = language),
                               change_language_url = change_language_url,
                               home_page_url = urlparse(request.url).path[:3],
                               content=render_template("portfolio.html",
                                                       language_cache = language_cache,
                                                       header = True,
                                                       content = render_template("portfolioMenu.html",
                                                                                 language_cache = language_cache)
                                                       )
                               )
    else:
        abort(404)


@app.route("/<language>/contact")
def contact(language):
    if language in ["pl", "en"]:
        change_language_url = change_language(request.url)
        # https: // hook.eu2.make.com / p12pjc4l53xac3tpkb6g5xw5rhhe1ojl
        return render_template("base.html",
                               app_cfg = CacheConfig().get_config(mongo),
                               language = language,
                               language_cache = Language().get_base(mongo = mongo, language = language),
                               change_language_url = change_language_url,
                               home_page_url = urlparse(request.url).path[:3],
                               content=render_template("contact.html",
                                                       language_cache = Language().get_contact(mongo = mongo, language = language),
                                                       time = contact_time(),
                                                       language=language)
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
def send_email():
    language = request.args.get("language")
    try:
        if language in ["pl", "en"]:
            receiver = request.form.get("email")
            message_content = request.form.get("message")
            message_template = Language().get_message_content(mongo = mongo, language = language)

            html_content = render_template("messageContent.html",
                                            message = message_template,
                                            message_content = message_content
                                            )
            message = Mail(
                from_email = Config.SENDER_EMAIL,
                to_emails = receiver,
                subject = message_template.title,
                html_content = html_content
            )

            sg = SendGridAPIClient(Config.SENDGRID_API_KEY)
            response = sg.send(message)
            if response.status_code in [200, 202]:
                return render_template("messageSuccessful.html", language = language)
            else:
                return Exception
        else:
            return Exception
    except Exception as e:
        print(e)
        return render_template("messageError.html", language = language), 500