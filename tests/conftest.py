import re
import pytest
import requests
from datetime import datetime
from PiotrBaranMeV2.app import create_app, mongo
from PiotrBaranMeV2.models.base_config import BaseConfig
from PiotrBaranMeV2.models.language import Language
from PiotrBaranMeV2.controllers.change_language import change_language
from PiotrBaranMeV2.controllers.time import contact_time

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    mongo.init_app(app)
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_m_base_config(client):
    config_file = BaseConfig.get_config(mongo)  # mongo jest teraz dostępne

    # test mandatory keys
    mandatory_keys = ["name", "head_title", "navbar_title", "language", "footer"]
    assert all(key in config_file.keys() for key in mandatory_keys)

    # test get valid configuration set
    assert config_file["name"] == "base.html"

    # test language keys
    language_keys = ["pl", "en"]
    assert all(key in config_file["language"].keys() for key in language_keys)

    # test footer keys
    footer_keys = ["logo", "logo_description", "social_media"]
    assert all(key in config_file["footer"].keys() for key in footer_keys)

    # test social_media keys
    social_media_keys = ["github", "linkedin"]
    assert all(key in config_file["footer"]["social_media"].keys() for key in social_media_keys)

    # test url is valid
    github = requests.get(config_file["footer"]["social_media"]["github"]).status_code
    linkedin = requests.get(config_file["footer"]["social_media"]["linkedin"]).status_code
    assert all([github in [200,202], linkedin in [200,202,999]]) #999 is specific for linked


def test_m_language_get_base(client):
    languages = ["pl", 'en']

    for lang in languages:
        config_file = Language.get_base(mongo, language = lang)

        # test mandatory keys
        mandatory_keys = ["name", "navbar"]
        assert all(key in config_file.keys() for key in mandatory_keys)

        # test get valid configuration set
        assert config_file["name"] == "base.html"

        # test navbar keys
        language_keys = ["about_me", "portfolio", "contact"]
        assert all(key in config_file["navbar"].keys() for key in language_keys)


def test_m_language_get_about(client):
    languages = ["pl", 'en']

    for lang in languages:
        config_file = Language.get_about(mongo, language = lang)

        # test mandatory keys
        mandatory_keys = ["name", "hero_banner"]
        assert all(key in config_file.keys() for key in mandatory_keys)

        # test get valid configuration set
        assert config_file["name"] == "about.html"

        # test hero_banner keys
        hero_banner_keys = ["title", "description", "achievements_top", "achievements_bottom", "resume"]
        assert all(key in config_file["hero_banner"].keys() for key in hero_banner_keys)

        #test achievements keys
        achievements = ["achievements_top", "achievements_bottom"]
        achievements_keys = ["level", "skill", "additional_info", "icon"]
        for i in achievements:
            for j in config_file["hero_banner"][i]:
                assert all(key in config_file["hero_banner"][i][j].keys() for key in achievements_keys)

        #test resume keys
        resume_keys = ["name", "file"]
        assert all(key in config_file["hero_banner"]["resume"].keys() for key in resume_keys)


def test_m_language_get_portfolio(client):
    languages = ["pl", 'en']

    for lang in languages:
        config_file = Language.get_portfolio(mongo, language = lang)

        # test mandatory keys
        mandatory_keys = ["name", "components"]
        assert all(key in config_file.keys() for key in mandatory_keys)

        # test get valid configuration set
        assert config_file["name"] == "portfolio.html"

        #test component keys
        for i in config_file["components"]:
            component_keys = ["name", "description", "img", "badges", "button"]
            assert all(key in config_file["components"][i].keys() for key in component_keys)

            #test button keys
            button_keys = ["name", "url"]
            assert all(key in config_file["components"][i]["button"].keys() for key in button_keys)

            #test img is valid
            response = requests.get(config_file["components"][i]["img"], stream = True)
            assert response.status_code == 200
            assert response.headers["Content-Type"].startswith("image/")


def test_m_language_get_portfolio_details(client):
    languages = ["pl", 'en']

    for lang in languages:
        #setup names for language
        if lang == "pl":
            names = ["DictionaryApp", "SAS Rule Engine", "Praca Inżynierska", "SAS Automate Notification"]
        elif lang == "en":
            names = ["DictionaryApp", "SAS Rule Engine", "Thesis of engineer", "SAS Automate Notification"]
        for name in names:
            config_file = Language.get_portfolio_details(mongo, language = lang, name = name)

            # test mandatory keys
            mandatory_keys = ["name", "context", "about", "technology"]
            assert all(key in config_file.keys() for key in mandatory_keys)

            # test context keys
            assert config_file["context"] == "details"

            #test about keys
            about_keys = ["name", "description", "img", "buttons"]
            assert all(key in config_file["about"].keys() for key in about_keys)

            #test img keys
            img_keys = ["url", "description"]
            assert all(key in config_file["about"]["img"].keys() for key in img_keys)

            # test img is valid
            response = requests.get(config_file["about"]["img"]["url"], stream = True)
            assert response.status_code == 200
            assert response.headers["Content-Type"].startswith("image/")

            #test button
            for i in config_file["about"]["buttons"]:
                assert "btn" in config_file["about"]["buttons"][i].keys()

            # test technology keys
            technology_keys = ["name", "description", "img", "badges"]
            assert all(key in config_file["technology"].keys() for key in technology_keys)

            # test img keys
            img_keys = ["url", "description"]
            assert all(key in config_file["technology"]["img"].keys() for key in img_keys)

            # test img is valid
            response = requests.get(config_file["technology"]["img"]["url"], stream = True)
            assert response.status_code == 200
            assert response.headers["Content-Type"].startswith("image/")

            # test badges
            for i in config_file["technology"]["badges"]:
                assert "badge" in config_file["technology"]["badges"][i].keys()


def test_m_language_contact(client):
    languages = ["pl", 'en']

    for lang in languages:
        config_file = Language.get_contact(mongo, language = lang)

        # test mandatory keys
        mandatory_keys = ["name", "form", "response", "descriptions"]
        assert all(key in config_file.keys() for key in mandatory_keys)

        # is valid file
        assert config_file["name"] == "contact.html"

        # test form keys
        form_keys = ["label", "first_name", "last_name", "email", "message", "button"]
        assert all(key in config_file["form"].keys() for key in form_keys)

        for i in config_file["form"]:
            if i in ["first_name", "last_name", "email", "message"]:
                # test form input content
                assert "label" in config_file["form"][i]
                assert "placeholder" in config_file["form"][i]

        #test response keys
        response_keys = ["correct", "error"]
        assert all(key in config_file["response"].keys() for key in response_keys)

        #test description keys
        descriptions_keys = ["cooperation", "resume"]
        assert all(key in config_file["descriptions"].keys() for key in descriptions_keys)

        for i in config_file["descriptions"]:
            descriptions_deep_keys = ["title", "description"]
            assert all(key in config_file["descriptions"][i].keys() for key in descriptions_deep_keys)

            if i == "resume":
                #button test
                assert "button" in config_file["descriptions"]["resume"].keys()
                assert "name" in config_file["descriptions"]["resume"]["button"].keys()
                assert "file" in config_file["descriptions"]["resume"]["button"].keys()


def test_m_message_content(client):
    languages = ["pl", 'en']

    for lang in languages:
        config_file = Language.get_message_content(mongo, language = lang)

        # test mandatory keys
        mandatory_keys = ["name", "title", "content"]
        assert all(key in config_file.keys() for key in mandatory_keys)

        #is valid file
        assert config_file["name"] == "messageContent.html"

        #test content keys
        content_keys = ["thanks", "hello", "about_the_answer", "your_message", "questions", "regards", "come_back"]
        assert all(key in config_file["content"].keys() for key in content_keys)


def test_c_change_language():
    #test switch pl to en
    lang = change_language("/pl")
    assert lang == "/en"

    #test switch en to pl
    lang = change_language("/en")
    assert lang == "/pl"

    #test switch something else to pl
    lang = change_language("/de")
    assert lang == "/pl"


def test_c_time():
    time = contact_time()

    #test mandatory keys
    mandatory_keys = ["request", "response", "write"]
    assert all(key in time for key in mandatory_keys)

    #test hour format
    time_pattern = r"^\d{2}:\d{2}$"
    assert all(re.match(time_pattern, time) for time in time.values())

    #test time ordering
    request_time = datetime.strptime(time["request"], "%H:%M")
    response_time = datetime.strptime(time["response"], "%H:%M")
    write_time = datetime.strptime(time["write"], "%H:%M")
    assert request_time <= response_time <= write_time



def test_app_redirect_to_language(client):
    response = client.get("/", follow_redirects=False)

    #test redirect
    assert response.status_code == 302

    #test path
    assert response.headers["Location"].endswith("/pl") or  response.headers["Location"].endswith("/en")


def test_app_not_found(client):
    response = client.get("/not_found_page", follow_redirects=False)

    #test not found code
    assert response.status_code == 404
    # 404.html render test
    assert b"<h1 class=\"text-9xl font-bold\">404</h1>" in response.data


def test_app_main(client):
    language = ["pl", "en"]
    for lang in language:
        response = client.get(f"/{lang}")

        # base.html render test
        assert response.status_code == 200
        assert b"<div class=\"navbar bg-base-100\">" in response.data

        # about.html render test
        assert b"id=\"stats-container\"" in response.data


def test_app_about(client):
    language = ["pl", "en"]
    for lang in language:
        response = client.get(f"/{lang}/about")

        # base.html render test
        assert response.status_code == 200
        assert b"<div class=\"navbar bg-base-100\">" in response.data

        # about.html render test
        assert b"id=\"stats-container\"" in response.data


def test_app_about_not_valid(client):
    response = client.get(f"/not_valid/about")

    # test not found code
    assert response.status_code == 404
    # 404.html render test
    assert b"<h1 class=\"text-9xl font-bold\">404</h1>" in response.data


def test_app_contact(client):
    language = ["pl", "en"]
    for lang in language:
        response = client.get(f"/{lang}/contact")

        # base.html render test
        assert response.status_code == 200
        assert b"<div class=\"navbar bg-base-100\">" in response.data

        # contact.html render test
        assert  b"hx-post=\"/send-email?language" in response.data


def test_app_contact_not_valid(client):
    response = client.get(f"/not_valid/contact")

    # test not found code
    assert response.status_code == 404
    # 404.html render test
    assert b"<h1 class=\"text-9xl font-bold\">404</h1>" in response.data


def test_app_portfolio(client):
    language = ["pl", "en"]
    for lang in language:
        response = client.get(f"/{lang}/portfolio")
        # test not found code
        assert response.status_code == 200

        # portfolio.html render test
        assert b"<div id=\"tech-content\" class=\"flex justify-center\">" in response.data

        # portfolioMenu.html render test
        assert b"hx-target=\"#tech-content\"" in response.data


def test_app_portfolio_not_valid(client):
    response = client.get(f"/not_valid/portfolio")

    # test not found code
    assert response.status_code == 404
    # 404.html render test
    assert b"<h1 class=\"text-9xl font-bold\">404</h1>" in response.data


def test_app_portfolio_details(client):
    language = ["pl", "en"]
    for lang in language:
        response = client.get(f"/{lang}/portfolio?name=DictionaryApp")
        # test not found code
        assert response.status_code == 200

        # portfolio.html render test
        assert b"<div id=\"tech-content\" class=\"flex justify-center\">" in response.data

        # portfolioDetails.html render test
        assert b"hx-target=\"#tech-content\"" in response.data

        # test come back button
        assert b"portfolio?back=True" in response.data


def test_app_portfolio_details_not_valid(client):
    response = client.get(f"/not_valid/portfolio?name=DictionaryApp")

    # test not found code
    assert response.status_code == 404
    # 404.html render test
    assert b"<h1 class=\"text-9xl font-bold\">404</h1>" in response.data


def test_app_send_email(client):
    collection_before = mongo.db.get_collection("messages")
    message_count_before = collection_before.count_documents({"message": "Test message"})

    data = {
        "email": "kontakt@piotrbaran.me",
        "message": "Test message",
        "first-name": "Test Name1",
        "last-name": "Test Name2",
    }
    response = client.post("/send-email?language=pl", data = data)

    assert response.status_code == 200

    assert b"toast toast-top toast-center" in response.data

    collection_after = mongo.db.get_collection("messages")
    message_count_after = collection_after.count_documents({"message": "Test message"})

    assert message_count_before < message_count_after

