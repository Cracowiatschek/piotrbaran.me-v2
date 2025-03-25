from PiotrBaranMeV2.config import Config
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
    db.create_collection("messages")
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
            "description": "Od zawsze odnajdywałem się w\u00A0świecie cyfrowym, zaczęło się od hobby\u00A0i\u00A0pracy inżynierskiej, gdzie napisałem swój pierwszy model. Po studiach trafiłem do działu CRM\u00A0w\u00A0jednym\u00A0z\u00A0polskich banków, gdzie pracuję do\u00A0teraz\u00A0i\u00A0od tamtej pory, zajmuję się przygotowywaniem procesów ETL, przepływów danych, a\u00A0także przygotowywania danych do\u00A0raportowania. W\u00A0swojej karierze miałem okazję również pisać mikroaplikacje\u00A0w\u00A0frameworkach Dash\u00A0i\u00A0Flask.",
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
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 0 1-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 0 1 1.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 0 0-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 0 1-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H9.75\" />\n</svg>"
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
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\"> <path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"m6.75 7.5 3 2.25-3 2.25m4.5 0h3m-9 8.25h13.5A2.25 2.25 0 0 0 21 18V6a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 6v12a2.25 2.25 0 0 0 2.25 2.25Z\"/>\n</svg>"
                },
                "3": {
                    "level": "Regular",
                    "skill": "REST",
                    "additional_info": "Fast API, Flask, Make.com",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418\" />\n</svg>"
                }
            },
            "resume": {
                "name": "Pobierz CV",
                "file": "Piotr Baran CV - PL.pdf"
            },
            "portfolio": {
                "name": "Portfolio"
            }
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
                "button": {
                    "name":"Pobierz",
                    "file":"Piotr Baran CV - PL.pdf"
                }
            }
        }
    }
    portfolio = {
        "name": "portfolio.html",
        "components": {
            "1": {
                "name": "DictionaryApp",
                "description": "Aplikacja służąca do przypisywania definicji sukcesu do kampanii, zgodnie ze zdefiniowaną wcześniej strukturą.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377808/dictionaryAppHome_q1kkby.png",
                "badges": "",
                "button": {
                    "name": "Sprawdź",
                    "url": "/pl/portfolio?name=DictionaryApp"
                }
            },
            "2": {
                "name": "SAS Rule Engine",
                "description": "Zestaw makr w SAS, składający się na framework, do budowy silnika regułowego.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377949/rulesEngineCode_onuuhe.png",
                "badges": "",
                "button": {
                    "name": "Sprawdź",
                    "url": "/pl/portfolio?name=SAS%20Rule%20Engine"
                }
            },
            "3": {
                "name": "Praca Inżynierska",
                "description": "Modele regresyjne do wyznaczania objętości drzew stojących na terenie miasta.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741378208/dataSciencePairPlot_f3wwtp.png",
                "badges": "",
                "button": {
                    "name": "Sprawdź",
                    "url": "/pl/portfolio?name=Praca%20Inżynierska"
                }
            },
            "4": {
                "name": "SAS Automate Notification",
                "description": "Zestaw procedur w SAS, który umożliwia wysyłanie zestawu raportów przy pomocy email.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377945/notificationCode_aocopl.png",
                "badges": "",
                "button": {
                    "name": "Sprawdź",
                    "url": "/pl/portfolio?name=SAS%20Automate%20Notification"
                }
            }
        }
    }
    details_dct_app = {
        "name": "DictionaryApp",
        "context": "details",
        "about": {
            "name": "Opis",
            "description": "Aplikacja służy do przypisania definicji sukcesów, dla kampanii marketingowych. Pobrane wartości można filtorwać względem fraz oraz typu kampanii. W celu zachowania przejrzystości pobrane kampanie są dzielone na strony po maksymalnie 20 pozycji. Po wyborze tego co ma zostać zdefinowane, użytkownikowi zostaje ustawiona lista pozycji do przypisania wartości, a po dokonanym zapisie użytkownik zostaje przekierowany na stronę główną.",
            "img":{
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377808/dictionaryAppHome_q1kkby.png",
                "description": "Przedstawienie możliwości wyboru i filtrowania pozycji do zdefiniowania."
            },
            "buttons": {
                "1": {
                    "btn":"<a role=\"button\" href=\"https://github.com/Cracowiatschek/DictionaryApp\" target=\"_blank\" class=\"btn btn-primary\">Więcej</a>"
                }
            }
        },
        "technology": {
            "name": "Technologie",
            "description": "Front-end jest głównie oparty o MaterializeCSS i szablony z wykorzystaniem Jinja2, z kolei na back-end składa się przede wszystkim Flask oraz plikowa baza danych sqlite.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377840/dictionaryAppWrite_ehe8p1.png",
                "description": "Przedstawienie możliwości definiowania sukcesów dla poszczególnych pozycji."
            },
            "badges": {
                "1": {
                    "badge": "<div class=\"badge badge-accent\">Python</div>"
                },
                "2": {
                    "badge": "<div class=\"badge badge-warning\">Flask</div>"
                },
                "3": {
                    "badge": "<div class=\"badge badge-warning\">sqlite</div>"
                },
                "4": {
                    "badge": "<div class=\"badge badge-secondary\">MaterializeCSS</div>"
                },
                "5": {
                    "badge": "<div class=\"badge badge-primary\">Jinja2</div>"
                },
                "6": {
                    "badge": "<div class=\"badge badge-primary\">HTML/CSS</div>"
                }
            }
        }
    }
    details_sas_rule = {
        "name": "SAS Rule Engine",
        "context": "details",
        "about": {
            "name": "Opis",
            "description": "Dzięki temu frameworkow użytkownik jest w stanie zbudować silnik regułowy, do obliczania grup docelowych, przy pomocy jednego centralnego narzędzia. Całość jest w pełni konfigurowalna i zawiera również makra do zarządzania poszczególnymi wyzwalaczami i regułami. Docelowo w narzędziu ma się znaleźć komponent raportowy, który będzie wysyłał mailowe podsumowanie wyliczonych grup i poszczególnych kryteriów odrzutu.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377840/dictionaryAppWrite_ehe8p1.png",
                "description": "Fragment przykładowej konfiguracji silnika."
            },
            "buttons": {
                "1": {
                    "btn": "<a role=\"button\" href=\"https://github.com/Cracowiatschek/SAS-Rules-Engine\" target=\"_blank\" class=\"btn btn-primary\">Więcej</a>"
                },
                "2": {
                    "btn": "<a role=\"button\" href=\"https://github.com/Cracowiatschek/SAS-Rules-Engine/wiki\" target=\"_blank\" class=\"btn btn-primary\">Dokumentacja</a>"
                }
            }
        },
        "technology": {
            "name": "Technologie",
            "description": "Całość jest oparta w pełni o natywne funkcje języka SAS.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741377944/rulesEngineArchitecture_re3lcs.png",
                "description": "Fragment architektury rozwiązania."
            },
            "badges": {
                "1": {
                    "badge": "<div class=\"badge badge-info\">SAS</div>"
                }
            }
        }
    }
    details_thesis = {
        "name": "Praca Inżynierska",
        "context": "details",
        "about": {
            "name": "Opis",
            "description": "Praca dyplomowa polegała, na zebraniu pomiarów na terenie Krakowa, a następnie wykonaniu analizy eksploracyjnej danych i budowie modelu predykcyjnego dla objętości drzew w mieście. W efekcie powstało kilka modeli, o różnej dokładności, ale też z różnym zastosowaniem, od prostego terenowego wykorzystania, do zaawansowanego labolatoryjnego.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741378208/dataSciencePairPlot_f3wwtp.png",
                "description": "Analiza eksploracyjna zmiennych."
            },
            "buttons": {
                "1": {
                    "btn": "<a role=\"button\" href=\"https://github.com/Cracowiatschek/Thesis_project\" target=\"_blank\" class=\"btn btn-primary\">Więcej</a>"
                }
            }
        },
        "technology": {
            "name": "Technologie",
            "description": "Realizacja była oparta o środowisko zeszytowe w datalore od JetBrains, przy pomocy zestawu bibliotek ML w Python tj. pandas, seaborn, scipy, statsmodels i scikit-learn.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741378208/dataScienceCurves_ip3eqi.png",
                "description": "Przewidywania vs. Rzeczywiste objętości"
            },
            "badges": {
                "1": {
                    "badge": "<div class=\"badge badge-accent\">Python</div>"
                },
                "2": {
                    "badge": "<div class=\"badge badge-warning\">pandas</div>"
                },
                "3": {
                    "badge": "<div class=\"badge badge-warning\">sci-kit learn</div>"
                },
                "4": {
                    "badge": "<div class=\"badge badge-warning\">scipy</div>"
                },
                "5": {
                    "badge": "<div class=\"badge badge-warning\">statsmodels</div>"
                },
                "6": {
                    "badge": "<div class=\"badge badge-warning\">seaborn</div>"
                },
                "7": {
                    "badge": "<div class=\"badge badge-info\">Jupyter Notebook</div>"
                },

            }
        }
    }
    details_sas_notif = {
        "name": "SAS Automate Notification",
        "context": "details",
        "about": {
            "name": "Opis",
            "description": "To jest zestaw dwóch pojedynczych makr, które umożliwiają wysyłkę notyfikacji mailowej w sposób prosty lub personalizowany. Sposób prosty jest reprezentowany przez prostą tabelę z wynikami, natomiast personalizacja, może polegać na wstawieniu indywidualnej treści dla odbiorcy lub też spersonalizowaniu pełnego szablonu HTML.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377945/notificationCode_aocopl.png",
                "description": "Fragment przykładowej konfiguracji powiadomienia."
            },
            "buttons": {
                "1": {
                    "btn": "<a role=\"button\" href=\"https://github.com/Cracowiatschek/SAS_Autoamtion\" target=\"_blank\" class=\"btn btn-primary\">Więcej</a>"
                }
            }
        },
        "technology": {
            "name": "Technologie",
            "description": "Całość jest oparta w pełni o natywne funkcje języka SAS. W przypadku personalizowanym można również wykorzystać HTML.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377945/notificationEmail_xrtxad.png",
                "description": "Screenshot skrzynki mailowej."
            },
            "badges": {
                "1": {
                    "badge": "<div class=\"badge badge-info\">SAS</div>"
                },
                "2": {
                    "badge": "<div class=\"badge badge-warning\">HTML</div>"
                }
            }
        }
    }
    message = {
        "name": "messageContent.html",
        "title": "Wiadomość do Piotra Barana została dostarczona. Dziękuję!",
        "content": {
            "thanks": "Dziękuję za Twoją wiadomość!",
            "hello": "Cześć,",
            "about_the_answer": "Twoja wiadomość właśnie do mnie została dostarczona, postaram się na nią odpowiedzieć jak najszybciej.",
            "your_message": "Treść wiadomości:",
            "questions": "Jeśli masz jakieś pytania to śmiało adresuj je w odpowiedzi na tego maila.",
            "regards": "Pozdrawiam,",
            "come_back": "Wróć na stronę"
        }
    }
    pl.insert_many([base, about, contact, portfolio, details_dct_app, details_thesis, details_sas_rule, details_sas_notif, message])
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
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 0 1-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 0 1 1.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 0 0-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 0 1-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H9.75\" />\n</svg>"
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
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\"> <path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"m6.75 7.5 3 2.25-3 2.25m4.5 0h3m-9 8.25h13.5A2.25 2.25 0 0 0 21 18V6a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 6v12a2.25 2.25 0 0 0 2.25 2.25Z\"/>\n</svg>"
                },
                "3": {
                    "level": "Regular",
                    "skill": "REST",
                    "additional_info": "Fast API, Flask, Make.com",
                    "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\" stroke-width=\"1.5\" stroke=\"currentColor\" class=\"size-6\">\n\t<path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418\" />\n</svg>"
                }
            },
            "resume": {
                "name": "Get resume",
                "file": "Piotr Baran CV - EN.pdf"
            },
            "portfolio": {
                "name": "Portfolio"
            }
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
                "label": "last name",
                "placeholder": "Smith"
            },
            "email": {
                "label": "e-mail",
                "placeholder": "mail@site.com"
            },
            "message": {
                "label": "your message",
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
                "button": {
                    "name":"Get resume",
                    "file": "Piotr Baran CV - EN.pdf"
                }
            }
        }
    }
    portfolio = {
        "name": "portfolio.html",
        "components": {
            "1": {
                "name": "DictionaryApp",
                "description": "An application for assigning definitions of success to campaigns, according to a previously defined structure.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377808/dictionaryAppHome_q1kkby.png",
                "badges": "",
                "button": {
                    "name": "More",
                    "url": "/en/portfolio?name=DictionaryApp"
                }
            },
            "2": {
                "name": "SAS Rule Engine",
                "description": "A set of SAS macros that make up the framework for building a rule engine.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377949/rulesEngineCode_onuuhe.png",
                "badges": "",
                "button": {
                    "name": "More",
                    "url": "/en/portfolio?name=SAS%20Rule%20Engine"
                }
            },
            "3": {
                "name": "Thesis of engineer",
                "description": "Regression models for determining the volume of standing trees in the city.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741378208/dataSciencePairPlot_f3wwtp.png",
                "badges": "",
                "button": {
                    "name": "More",
                    "url": "/en/portfolio?Thesis%20of%20engineer"
                }
            },
            "4": {
                "name": "SAS Automate Notification",
                "description": "A set of procedures in SAS that allows you to send a set of reports via email.",
                "img": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377945/notificationCode_aocopl.png",
                "badges": "",
                "button": {
                    "name": "More",
                    "url": "/en/portfolio?SAS%20Automate%20Notification"
                }
            }
        }
    }
    details_dct_app = {
        "name": "DictionaryApp",
        "context": "details",
        "about": {
            "name": "About",
            "description": "The application is used to assign definitions of successes for marketing campaigns. Downloaded values can be filtered by phrases and campaign type. In order to maintain clarity, downloaded campaigns are divided into pages of up to 20 items. After selecting what is to be defined, the user is set a list of items to assign values to, and after saving, the user is redirected to the main page.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377808/dictionaryAppHome_q1kkby.png",
                "description": "Presentation of the possibilities of selecting and filtering items to be defined."
            },
            "buttons": {
                "1": {
                    "btn": "<a role=\"button\" href=\"https://github.com/Cracowiatschek/DictionaryApp\" target=\"_blank\" class=\"btn btn-primary\">More</a>"
                }
            }
        },
        "technology": {
            "name": "Tech stack",
            "description": "The front-end is mainly based on MaterializeCSS and templates using Jinja2, while the back-end consists primarily of Flask and an sqlite file database.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377840/dictionaryAppWrite_ehe8p1.png",
                "description": "Presentation of possibilities for defining success for individual positions."
            },
            "badges": {
                "1": {
                    "badge": "<div class=\"badge badge-accent\">Python</div>"
                },
                "2": {
                    "badge": "<div class=\"badge badge-warning\">Flask</div>"
                },
                "3": {
                    "badge": "<div class=\"badge badge-warning\">sqlite</div>"
                },
                "4": {
                    "badge": "<div class=\"badge badge-secondary\">MaterializeCSS</div>"
                },
                "5": {
                    "badge": "<div class=\"badge badge-primary\">Jinja2</div>"
                },
                "6": {
                    "badge": "<div class=\"badge badge-primary\">HTML/CSS</div>"
                }
            }
        }
    }
    details_sas_rule = {
        "name": "SAS Rule Engine",
        "context": "details",
        "about": {
            "name": "About",
            "description": "Thanks to this framework, the user is able to build a rule engine for calculating target groups using one central tool. The whole thing is fully configurable and also includes macros for managing individual triggers and rules. The tool is to eventually include a reporting component that will send an email summary of the calculated groups and individual rejection criteria.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377840/dictionaryAppWrite_ehe8p1.png",
                "description": "Fragment of an example engine configuration."
            },
            "buttons": {
                "1": {
                    "btn": "<a role=\"button\" href=\"https://github.com/Cracowiatschek/SAS-Rules-Engine\" target=\"_blank\" class=\"btn btn-primary\">More</a>"
                },
                "2": {
                    "btn": "<a role=\"button\" href=\"https://github.com/Cracowiatschek/SAS-Rules-Engine/wiki\" target=\"_blank\" class=\"btn btn-primary\">Docs</a>"
                }
            }
        },
        "technology": {
            "name": "Tech stack",
            "description": "The whole thing is based entirely on native SAS language functions.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741377944/rulesEngineArchitecture_re3lcs.png",
                "description": "Fragment of the solution architecture."
            },
            "badges": {
                "1": {
                    "badge": "<div class=\"badge badge-info\">SAS</div>"
                }
            }
        }
    }
    details_thesis = {
        "name": "Thesis of engineer",
        "context": "details",
        "about": {
            "name": "About",
            "description": "The diploma thesis consisted of collecting measurements in the area of Krakow, and then performing exploratory analysis of the data and building a predictive model for the volume of trees in the city. As a result, several models were created, with different accuracy, but also with different applications, from simple field use to advanced laboratory use.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741378208/dataSciencePairPlot_f3wwtp.png",
                "description": "Exploratory analysis of variables."
            },
            "buttons": {
                "1": {
                    "btn": "<a role=\"button\" href=\"https://github.com/Cracowiatschek/Thesis_project\" target=\"_blank\" class=\"btn btn-primary\">More</a>"
                }
            }
        },
        "technology": {
            "name": "Tech stack",
            "description": "The implementation was based on the notebook environment in datalore from JetBrains, using a set of ML libraries in Python, i.e. pandas, seaborn, scipy, statsmodels and scikit-learn.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/v1741378208/dataScienceCurves_ip3eqi.png",
                "description": "Projections vs. Actual Volumes"
            },
            "badges": {
                "1": {
                    "badge": "<div class=\"badge badge-accent\">Python</div>"
                },
                "2": {
                    "badge": "<div class=\"badge badge-warning\">pandas</div>"
                },
                "3": {
                    "badge": "<div class=\"badge badge-warning\">sci-kit learn</div>"
                },
                "4": {
                    "badge": "<div class=\"badge badge-warning\">scipy</div>"
                },
                "5": {
                    "badge": "<div class=\"badge badge-warning\">statsmodels</div>"
                },
                "6": {
                    "badge": "<div class=\"badge badge-warning\">seaborn</div>"
                },
                "7": {
                    "badge": "<div class=\"badge badge-info\">Jupyter Notebook</div>"
                },

            }
        }
    }
    details_sas_notif = {
        "name": "SAS Automate Notification",
        "context": "details",
        "about": {
            "name": "About",
            "description": "This is a set of two individual macros that allow you to send email notifications in a simple or personalized way. The simple way is represented by a simple table of results, while personalization can consist of inserting individual content for the recipient or personalizing the full HTML template.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377945/notificationCode_aocopl.png",
                "description": "Fragment of an example notification configuration."
            },
            "buttons": {
                "1": {
                    "btn": "<a role=\"button\" href=\"https://github.com/Cracowiatschek/SAS_Autoamtion\" target=\"_blank\" class=\"btn btn-primary\">More</a>"
                }
            }
        },
        "technology": {
            "name": "Tech stack",
            "description": "The whole thing is based entirely on native SAS language functions. In a personalized case, HTML can also be used.",
            "img": {
                "url": "https://res.cloudinary.com/dz3ms2ssv/image/upload/c_fill,w_1000,h_1000/v1741377945/notificationEmail_xrtxad.png",
                "description": "Screenshot of email inbox."
            },
            "badges": {
                "1": {
                    "badge": "<div class=\"badge badge-info\">SAS</div>"
                },
                "2": {
                    "badge": "<div class=\"badge badge-warning\">HTML</div>"
                }
            }
        }
    }
    message = {
        "name": "messageContent.html",
        "title": "Your message to Piotr Baran was delivered. Thank you!",
        "content": {
            "thanks": "Thanks for Your message!",
            "hello": "Hello,",
            "about_the_answer": "Your message has just been delivered to me, I will try to respond to it as soon as possible.",
            "your_message": "Message content:",
            "questions": "If you have any questions, feel free to address them in a reply to this email.",
            "regards": "Best regards,",
            "come_back": "Come back to website"
        }
    }
    pl.insert_many(
        [base, about, contact, portfolio, details_dct_app, details_thesis, details_sas_rule, details_sas_notif, message])
    r = pl.find()
    print("EN")
    for i in r:
        print(i.keys())
except Exception as e:
    print(e)


