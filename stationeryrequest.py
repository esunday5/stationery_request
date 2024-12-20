import os
from flask import Flask, jsonify, request, Blueprint  # Import jsonify for JSON responses
from flask_mail import Mail, Message
import logging
from logging import StreamHandler

app = Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'emmanatesynergy@gmail.com'  # Your Gmail email
app.config['MAIL_PASSWORD'] = 'mrfl owrh pyoq hflx'  # App password if 2FA enabled
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_TIMEOUT'] = 10

mail = Mail(app)

@app.route("/stationeryrequest", methods=["POST"])
def send_email():
    # Get branch name from POST request
    data = request.get_json()  # Assumes the client sends JSON data
    branch_name = data.get("branch_name", "Unknown Branch")  # Default to "Unknown Branch" if missing
    request_type = data.get ("request_type", "Unknown Type")
    department = data.get("department", "Unknown Department")
    description = data.get("description", "N/A")
    quantity = data.get("quantity", "N/A")
    items = data.get("items", "N/A")

    # Define the HTML content with dynamic branch name
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Notification</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4; color: #555;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden;">
            <div style="background-color: #37a04e; padding: 20px; text-align: center;">
                <img src="https://ibank.mybankone.com/tenants/101/img/logo.png" alt="Logo" style="max-width: 150px;">
            </div>
            <p style="font-size: 22px; font-weight: bold; color: #388e3c; text-align: center;">You have a new request for {branch_name}!</p>

            <div style="padding: 20px; font-size: 14px; text-align: center;">
                <p><strong>Request Type:</strong> {request_type}</p>
                <p><strong>Department:</strong> {department}</p>
                <p><strong>Description:</strong> {description}</p>
                <p><strong>Quantity:</strong> {quantity}</p>
                <p><strong>Items:</strong> {items}</p>
            </div>


                <div style="text-align: center; margin: 20px 0;">
                    <a href="#" style="text-decoration: none; background-color: #337036; color: #ffffff; padding: 10px 20px; border-radius: 5px; font-size: 14px;">Click to review request</a>
                </div>
            </div>
            <!-- Footer -->
            <footer style="padding: 20px; text-align: center; font-size: 13px; color: #777; position: absolute-bottom;">
                <p style="margin: 0;">Copyright &copy; Ekondo Staff Portal 2024</p>
            </footer>
        </div>
    </body>
    </html>
    """

    # Create the email
    msg = Message(
        subject="New Request Notification",
            sender="emmanatesynergy@gmail.com",
            recipients=["henry.etim@ekondomfbank.com", "amanimeshiet@gmail.com"]  # Replace with actual recipient
    )
    msg.body = f"You have a new request for {branch_name}."  # Plain text fallback
    msg.html = html_content  # HTML content
    mail.send(msg)

    return {"message": "Email sent successfully!"}, 200

if __name__ == '__main__':
    app.run(debug=True)