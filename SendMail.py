import yagmail
import os
from dotenv import load_dotenv

load_dotenv()


sender = ""
reciever = "agbdtescorurke@dropmail.me"
subject = "Test mail using python"
contents = '''
this is the content side for sending mail
'''

yag = yagmail.SMTP(user=sender , password=os.getenv('PASSWORD'))
yag.send(to=reciever , subject=subject , contents=contents)
print("Email send ...")