from flask import Flask
from flask_mail import Mail, Message
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'jayshreemishra197@gmail.com'
app.config['MAIL_PASSWORD'] = 'pass' #I am not sharing my password for obvious reasons
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/")
def index():
    msg = Message(subject='Python (Selenium) Assignment - Jayshree Mishra', 
                  sender='jayshreemishra197@gmail.com', 
                  recipients=['tech@themedius.ai'], 
                  cc=['hr@themedius.ai'])

    msg.html = """
    <p>1. Screenshot of the form filled via code:</p>
    <img src="cid:screenshot">
    <p>2. Source code (GitHub repository): <a href="https://github.com/JayshreeMishra/selenium-assignment">https://github.com/JayshreeMishra/selenium-assignment</a></p>
    <p>3. Brief documentation of your approach:</p>
    <p>This script uses Selenium WebDriver to automate filling out a Google Forms. It starts by setting up the Edge browser in incognito mode and navigating to the form URL. Then, it uses XPath locators to identify and fill in the form fields, including full name, contact number, email ID, full address, pin code, date of birth, gender, and verification code. After filling in all the fields, it submits the form and waits for 60 seconds before closing the browser. The script uses WebDriverWait to ensure that each element is visible before attempting to interact with it, and time.sleep to introduce delays between actions.</p>
    <p>4. Your resume:</p>
    <p>JAYSHREE_MISHRA_RESUME_ML.pdf </p>
    <p>5. Links to past projects/work samples: <a href="https://github.com/JayshreeMishra">https://github.com/JayshreeMishra</a></p>
    <p>6. Confirm your availability to work full time (10 am to 7 pm) for the next 3-6 months:</p>
    <p>I am confirming my availability to work full-time from 10 am to 7 pm for the next 3-6 months. I am committed to contributing effectively during this period. Thank you for considering my application. I look forward to the opportunity.</p>
    <p>Best regards,<br>Jayshree Rajesh Mishra</p>
    """

    # screenshot image
    with open(r'C:\Users\jaysh\OneDrive\Desktop\Selenium-assignment\screenshot.jpg', 'rb') as f:
        img_data = f.read()
        msg.attach('screenshot.jpg', 'image/jpeg', img_data, headers={'Content-ID': '<screenshot>'})

    # resume PDF
    with open(r'C:\Users\jaysh\OneDrive\Desktop\JAYSHREE_MISHRA_RESUME_ML.pdf', 'rb') as f:
        pdf_data = f.read()
        msg.attach('JAYSHREE_MISHRA_RESUME_ML.pdf', 'application/pdf', pdf_data)

    mail.send(msg)
    return "Message sent!"

if __name__ == '__main__':
    app.run(debug=True)
