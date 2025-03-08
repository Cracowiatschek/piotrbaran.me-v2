from config import Config
from pymongo import MongoClient

config = Config
client = MongoClient(config.MONGO_URI)

try:
    db = client.get_database(config.MONGO_DB)
    connection_list = db.list_collection_names()
    for i in connection_list:
        print(i)
except:
    pass

try:
    cfg = db.get_collection("config")
    cfg.drop()
    db.create_collection("config")
except Exception as e:
    print(e)

try:
    config = db.get_collection("config")
    config_content = {
        "name": "base.html",
        "head_title": "Piotr Baran",
        "navbar_title": "Piotr Baran",
        "language": {
            "pl": "PL",
            "en": "EN"
        },
        "footer": {
            "logo": "<svg\n\twidth=\"36\"\n\theight=\"36\"\n\tviewBox=\"0 0 24 24\"\n\txmlns=\"http://www.w3.org/2000/svg\"\n\tfill-rule=\"evenodd\"\n\tclip-rule=\"evenodd\"\n\tclass=\"fill-current\">\n\t<path\n\t\td=\"M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z\"></path>\n\t</svg>",
            "logo_description": "© 2025 Piotr Baran",
            "social_media": {
                "github": "https://github.com/Cracowiatschek",
                "linkedin": "https://www.linkedin.com/in/piotr-baran-765702217",
            }
        }
    }
    config.insert_one(config_content)
    r = config.find_one()
    print("Config")
    print(r.keys())
except Exception as e:
    print(e)

try:
    cfg = db.get_collection("pl")
    cfg.drop()
    db.create_collection("pl")
    cfg = db.get_collection("en")
    cfg.drop()
    db.create_collection("en")
except Exception as e:
    print(e)


try:
    pl = db.get_collection("pl")
    base = {
        "name": "base.html",
        "navbar":{
            "about_me": "O mnie",
            "portfolio": "Portfolio",
            "contact": "Kontakt"
        }
    }
    about = {
        "name": "about.html",
        "hero_banner": {
            "title": "O mnie!",
            "description": "Od zawsze odnajdywałem się w świecie cyfrowym, zaczęło się od hobby i pracy inżynierskiej, gdzie napisałem swój pierwszy model. Po studiach trafiłem do działu CRM w jednym z polskich banków, gdzie pracuję do teraz i od tamtej pory, zajmuję się przygotowywaniem procesów ETL, przepływów danych, a także przygotowywania danych do raportowania. W swojej karierze miałem okazję również pisać mikroaplikacje w frameworkach Dash i Flask.",
            "achievements_top": {
                "1": {
                    "level": "Regular",
                    "skill": "Python",
                    "additional_info": "Flask, FastAPI, Dash, Machine Learning",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M14.25 9.75 16.5 12l-2.25 2.25m-4.5 0L7.5 12l2.25-2.25M6 20.25h12A2.25 2.25 0 0 0 20.25 18V6A2.25 2.25 0 0 0 18 3.75H6A2.25 2.25 0 0 0 3.75 6v12A2.25 2.25 0 0 0 6 20.25Z\" />\n</svg>"
                },
                "2": {
                    "level": "Senior",
                    "skill": "SQL",
                    "additional_info": "DB/DWH, PL/SQL, pgSQL",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125\" />\n</svg>"
                },
                "3": {
                    "level": "Junior",
                    "skill": "No SQL",
                    "additional_info": "mongoDB",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-7\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 0 1-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 0 1 1.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 0 0-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 0 1-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H9.75\" />\n</svg>"
                }
            },
            "achievements_bottom": {
                "1": {
                    "level": "Regular",
                    "skill": "HTML/CSS",
                    "additional_info": "Materialize CSS, DaisyUI, HTMX, Jinja2",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M17.25 6.75 22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3-4.5 16.5\" />\n</svg>"
                },
                "2": {
                    "level": "Regular",
                    "skill": "SAS",
                    "additional_info": "Campaign Manager, ETL",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-7\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 0 1-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 0 1 1.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 0 0-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 0 1-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H9.75\" />\n</svg>"
                },
                "3": {
                    "level": "Regular",
                    "skill": "REST",
                    "additional_info": "Fast API, Flask, Make.com",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418\" />\n</svg>"
                }
            },
            "resume": "Pobierz CV"
        }
    }
    contact = {
        "name": "contact.html",
        "form": {
            "label": "Kontakt",
            "first_name": {
                "label": "imię",
                "placeholder": "Jan"
            },
            "last_name": {
                "label": "nazwisko",
                "placeholder": "Kowalski"
            },
            "email": {
                "label": "e-mail",
                "placeholder": "mail@site.com"
            },
            "message": {
                "label": "Twoja wiadomość",
                "placeholder": "Dzień dobry..."
            },
            "button": "Wyślij"
        },
        "response": {
            "correct": "Dziękuję za wiadomość!",
            "error": "Coś poszło nie tak, spróbuj ponownie."
        },
        "descriptions": {
            "cooperation": {
                "title": "Chcesz rozpocząć współpracę?",
                "description": "Skorzystaj z formularza kontaktowego lub bezpośrednio napisz wiadomość na poniższy adres e-mail."
            },
            "resume": {
                "title": "Może chcesz zapoznać się z moim doświadczeniem?",
                "description": "Spróbuj pobrać moje CV poniżej.",
                "button": "Pobierz"
            }
        }
    }
    portfolio = {
        "name": "portfolio.html",
        "components": {
            "1": {
                "name": "DictionaryApp",
                "description": "Aplikacja służąca do przypisywania definicji sukcesu do kampanii, zgodnie ze zdefiniowaną wcześniej strukturą.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741377808/dictionaryAppHome_q1kkby.png",
                "badges": "",
                "button": {
                    "name": "Sprawdź",
                    "url": "/pl/portfolio?name=DictionaryApp"
                }
            },
            "2": {
                "name": "SAS Rule Engine",
                "description": "Zestaw makr w SAS, składający się na framework, do budowy silnika regułowego.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741377949/rulesEngineCode_onuuhe.png",
                "badges": "",
                "button": {
                    "name": "Sprawdź",
                    "url": "/pl/portfolio?name=SAS%20Rule%20Engine"
                }
            },
            "3": {
                "name": "Praca Inżynierska",
                "description": "Modele regresyjne do wyznaczania objętości drzew stojących na terenie miasta.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741378208/dataSciencePairPlot_f3wwtp.png",
                "badges": "",
                "button": {
                    "name": "Sprawdź",
                    "url": "/pl/portfolio?name=Praca%20In%C5ynierska"
                },
            "4": {
                "name": "SAS Automate Notification",
                "description": "Zestaw procedur w SAS, który umożliwia wysyłanie zestawu raportów przy pomocy email.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741377945/notificationCode_aocopl.png",
                "badges": "",
                "button": {
                    "name": "Sprawdź",
                    "url": "/pl/portfolio?name=SAS%20Automate%20Notification"
                }
            }
            }
        }
    }
    pl.insert_many([base, about, contact, portfolio])
    r = pl.find()
    print("PL")
    for i in r:
        print(i.keys())
except Exception as e:
    print(e)



try:
    pl = db.get_collection("en")
    base = {
        "name": "base.html",
        "navbar":{
            "about_me": "About me",
            "portfolio": "Portfolio",
            "contact": "Contact"
        }
    }
    about = {
        "name": "about.html",
        "hero_banner": {
            "title": "About me!",
            "description": "I have always found my place in the digital world, it started with a hobby and engineering work, where I wrote my first model. After graduation, I went to the CRM department in one of the Polish banks, where I work until now and since then, I have been involved in preparing ETL processes, data flows, and preparing data for reporting. In my career, I also had the opportunity to write microapplications in the Dash and Flask frameworks.",
            "achievements_top": {
                "1": {
                    "level": "Regular",
                    "skill": "Python",
                    "additional_info": "Flask, FastAPI, Dash, Machine Learning",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M14.25 9.75 16.5 12l-2.25 2.25m-4.5 0L7.5 12l2.25-2.25M6 20.25h12A2.25 2.25 0 0 0 20.25 18V6A2.25 2.25 0 0 0 18 3.75H6A2.25 2.25 0 0 0 3.75 6v12A2.25 2.25 0 0 0 6 20.25Z\" />\n</svg>"
                },
                "2": {
                    "level": "Senior",
                    "skill": "SQL",
                    "additional_info": "DB/DWH, PL/SQL, pgSQL",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125\" />\n</svg>"
                },
                "3": {
                    "level": "Junior",
                    "skill": "No SQL",
                    "additional_info": "mongoDB",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-7\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 0 1-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 0 1 1.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 0 0-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 0 1-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H9.75\" />\n</svg>"
                }
            },
            "achievements_bottom": {
                "1": {
                    "level": "Regular",
                    "skill": "HTML/CSS",
                    "additional_info": "Materialize CSS, DaisyUI, HTMX, Jinja2",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M17.25 6.75 22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3-4.5 16.5\" />\n</svg>"
                },
                "2": {
                    "level": "Regular",
                    "skill": "SAS",
                    "additional_info": "Campaign Manager, ETL",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-7\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 0 1-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 0 1 1.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 0 0-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 0 1-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H9.75\" />\n</svg>"
                },
                "3": {
                    "level": "Regular",
                    "skill": "REST",
                    "additional_info": "Fast API, Flask, Make.com",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418\" />\n</svg>"
                }
            },
            "resume": "Get resume"
        }
    }
    contact = {
        "name": "contact.html",
        "form": {
            "label": "Contact",
            "first_name": {
                "label": "name",
                "placeholder": "John"
            },
            "last_name": {
                "label": "nazwisko",
                "placeholder": "Smith"
            },
            "email": {
                "label": "e-mail",
                "placeholder": "mail@site.com"
            },
            "message": {
                "label": "Your message",
                "placeholder": "Hello..."
            },
            "button": "Send"
        },
        "response": {
            "correct": "Thanks for your message!",
            "error": "Something went wrong, please try again."
        },
        "descriptions": {
            "cooperation": {
                "title": "Do you want to start cooperation?",
                "description": "Please, use the contact form or send a message directly to the email address below."
            },
            "resume": {
                "title": "Maybe you would like to read about my experience?",
                "description": "Try get my CV below.",
                "button": "Get resume"
            }
        }
    }
    portfolio = {
        "name": "portfolio.html",
        "components": {
            "1": {
                "name": "DictionaryApp",
                "description": "An application for assigning definitions of success to campaigns, according to a previously defined structure.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741377808/dictionaryAppHome_q1kkby.png",
                "badges": "",
                "button": {
                    "name": "More",
                    "url": "/en/portfolio?name=DictionaryApp"
                }
            },
            "2": {
                "name": "SAS Rule Engine",
                "description": "A set of SAS macros that make up the framework for building a rule engine.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741377949/rulesEngineCode_onuuhe.png",
                "badges": "",
                "button": {
                    "name": "More",
                    "url": "/en/portfolio?name=SAS%20Rule%20Engine"
                }
            },
            "3": {
                "name": "Thesis of engineer",
                "description": "Regression models for determining the volume of standing trees in the city.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741378208/dataSciencePairPlot_f3wwtp.png",
                "badges": "",
                "button": {
                    "name": "More",
                    "url": "/en/portfolio?Thesis%20of%20engineer"
                }
            },
            "4": {
                "name": "SAS Automate Notification",
                "description": "A set of procedures in SAS that allows you to send a set of reports via email.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741377945/notificationCode_aocopl.png",
                "badges": "",
                "button": {
                    "name": "More",
                    "url": "/en/portfolio?SAS%20Automate%20Notification"
                }
            }
        }
    }
    pl.insert_many([base, about, contact, portfolio])
    r = pl.find()
    print("EN")
    for i in r:
        print(i.keys())
except Exception as e:
    print(e)


