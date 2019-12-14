import os;
import sys;
import psutil;
import time;
import re;
import urllib;
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def isConnected():
    try:
        urllib.urlopen('http://216.58.192.142')
        return True
    except:
        return False

def sendMail(filename,toaddr):
    fromaddr="Your email_address"
    password="PassWord"

    try:
        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Log file"
        body = "To test:Sending mail with attachment"
        msg.attach(MIMEText(body, 'plain'))


        attachment = open(filename, "rb")


        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)


        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()


        s.login(fromaddr, password)

        text = msg.as_string()


        s.sendmail(fromaddr, toaddr, text)

        s.quit()

    except:
        print("Failed to send")
        return False



def main():
    if sys.argv[1] and sys.argv[2]:
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not (re.search(regex, sys.argv[2])):
            print("Invalid Email");
            exit(-1);

        if not os.path.exists(sys.argv[1]):
            os.mkdir(sys.argv[1]);

        filename = os.path.join(sys.argv[1], "log_%s.txt" % time.ctime());
        line = "~" * 40;
        fobj = open(filename, 'w');
        fobj.write(line + "\n");

        for pobj in psutil.process_iter():
            fobj.write("Username->"+str(pobj.username())+" PID->"+str(pobj.pid)+" Name->"+str(pobj.name())+"\n");
            fobj.write(line + "\n");
        if isConnected():
            print("connected to internet")
            sendMail(filename,sys.argv[2]);
        else:
            print("failed to connect to internet")
    else:
        print("First write valid emailid and password in 'sendmail()' and your account should have permission for 'Less secure app access'")
        print("Right way to give cmdline arguments is below:")
        print("python   python-script-name.py   directory-name   valid-email-address_of_sender")
        print("thats it..press enter...thank you")



if __name__ == "__main__":
    main();