from datetime import datetime, timedelta


def contact_time() -> dict:

    time = {
        "request": (datetime.now() - timedelta(minutes = 2)).strftime("%H:%M"),
        "response": (datetime.now() - timedelta(minutes = 1)).strftime("%H:%M"),
        "write": datetime.now().strftime("%H:%M")
    }
    return time
