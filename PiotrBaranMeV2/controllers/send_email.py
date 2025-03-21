from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime

def send_message(ready_template, sender, receiver, subject, sg_api_key, mongo, request_content, language):
    #config massage content to api
    message = Mail(
        from_email = sender,
        to_emails = receiver,
        subject = subject,
        html_content = ready_template
    )
    message.add_cc(sender)
    #materialize email client
    sg = SendGridAPIClient(sg_api_key)
    #send message
    response = sg.send(message)

    if response.status_code in [200, 202]: # if message send correct insert to database
        cursor = mongo.db.get_collection("messages")
        cursor.insert_one(
            {
                "name": "message-form",
                "first-name": request_content.form.get("first-name"),
                "last-name": request_content.form.get("last-name"),
                "e-mail": request_content.form.get("email"),
                "message": request_content.form.get("message"),
                "language": language,
                "time": datetime.now()
            }
        )

    return response.status_code
