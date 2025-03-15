
from flask import Flask, render_template, request, redirect, abort
from flask_pymongo import PyMongo
from urllib.parse import urlparse
from .config import Config
from .models.base_config import BaseConfig
from .models.language import Language
from .controllers.change_language import change_language
from .controllers.time import contact_time
from .controllers.send_email import send_message

app_config = Config()
mongo = PyMongo()

def create_app(config_class=app_config):
    app = Flask(__name__)
    app.config.from_object(config_class)  # load config class


    # mongo init
    mongo.init_app(app)


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
                                   app_cfg = BaseConfig().get_config(mongo),
                                   language = language,
                                   home_page_url = urlparse(request.url).path[:3],
                                   language_cache = Language().get_base(mongo = mongo, language = language),
                                   change_language_url = change_language_url,
                                   content = render_template("about.html",
                                                             language_cache = Language().get_about(mongo = mongo,
                                                                                                   language = language))
                                   )
        else:
            abort(404)


    @app.route("/<language>/about")
    def about(language):
        if language in ["pl", "en"]:
            change_language_url = change_language(request.url)

            return render_template("base.html",
                                   app_cfg = BaseConfig().get_config(mongo),
                                   language = language,
                                   home_page_url = urlparse(request.url).path[:3],
                                   language_cache = Language().get_base(mongo = mongo, language = language),
                                   change_language_url = change_language_url,
                                   content = render_template("about.html",
                                                             language_cache = Language().get_about(mongo = mongo,
                                                                                                   language = language))
                                   )
        else:
            abort(404)


    @app.route("/<language>/portfolio")
    def portfolio(language):
        if language in ["pl", "en"]:
            change_language_url = change_language(request.url)
            language_cache = Language().get_portfolio(mongo = mongo, language = language)

            if "name" in request.args and request.headers.get("HX-Request"):
                return render_template("portfolioDetails.html",
                                       product_name = request.args.get("name"),
                                       url = f"/{language}/portfolio?back=True",
                                       content = Language().get_portfolio_details(mongo, language,
                                                                                  request.args.get("name")),
                                       badges = "ready",
                                       buttons = "ready"
                                       )
            elif "name" in request.args and "HX-Request" not in request.headers:
                return render_template("base.html",
                                       app_cfg = BaseConfig().get_config(mongo),
                                       language = language,
                                       language_cache = Language().get_base(mongo = mongo, language = language),
                                       change_language_url = change_language_url,
                                       home_page_url = urlparse(request.url).path[:3],
                                       content = render_template("portfolio.html",
                                                                 language_cache = language_cache,
                                                                 header = True,
                                                                 content = render_template("portfolioDetails.html",
                                                                                           content = Language().get_portfolio_details(
                                                                                               mongo, language,
                                                                                               request.args.get(
                                                                                                   "name")),
                                                                                           badges = "ready",
                                                                                           buttons = "ready",
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
                                   app_cfg = BaseConfig().get_config(mongo),
                                   language = language,
                                   language_cache = Language().get_base(mongo = mongo, language = language),
                                   change_language_url = change_language_url,
                                   home_page_url = urlparse(request.url).path[:3],
                                   content = render_template("portfolio.html",
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
            return render_template("base.html",
                                   app_cfg = BaseConfig().get_config(mongo),
                                   language = language,
                                   language_cache = Language().get_base(mongo = mongo, language = language),
                                   change_language_url = change_language_url,
                                   home_page_url = urlparse(request.url).path[:3],
                                   content = render_template("contact.html",
                                                             language_cache = Language().get_contact(mongo = mongo,
                                                                                                     language = language),
                                                             time = contact_time(),
                                                             language = language)
                                   )
        else:
            abort(404)


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("base.html",
                               app_cfg = BaseConfig().get_config(mongo),
                               language = "pl",
                               change_language_url = "/pl",
                               home_page_url = "/pl",
                               language_cache = Language().get_base(mongo = mongo, language = "pl"),
                               content = render_template("404.html")), 404


    @app.route("/send-email", methods = ["POST"])
    def send_email():
        language = request.args.get("language")
        try:
            if language in ["pl", "en"]:
                message_template = Language().get_message_content(mongo = mongo, language = language)
                html_content = render_template("messageContent.html",
                                               message = message_template,
                                               message_content = request.form.get("message"),
                                               language = language
                                               )
                message = send_message(
                    ready_template = html_content,
                    sender = Config.SENDER_EMAIL,
                    receiver = request.form.get("email"),
                    subject = message_template["title"],
                    sg_api_key = Config.SENDGRID_API_KEY,
                    mongo = mongo,
                    request_content = request,
                    language = language
                )
                print(type(request), type(request.form))
                if message in [200, 202]:
                    return render_template("messageSuccessful.html", language = language)
                else:
                    return render_template("messageError.html", language = language), 500
            else:
                return render_template("messageError.html", language = language), 500
        except Exception as e:
            print(e)
            return render_template("messageError.html", language = language), 500

    return app


app = create_app(app_config)
