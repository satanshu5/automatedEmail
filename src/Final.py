import requests
import time
from bs4 import BeautifulSoup

emails = ['satanshuaglawe5@gmail.com','nkambleaglawe@gmail.com','satishaglawe5@gmail.com','kambleasmi3@gmail.com','jaybharati999@gmail.com','wadhwanisahil9@gmail.com','hasan.syed.online@gmail.com','anshumaanraut@gmail.com']

# send the mail
import smtplib

# email body    
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()

# Email content PlacehOlder
content = ''

# Extracting news froM Hacker News Stories
def extract_news(url):
    print("Extracting the news from Hacker News Stories...")
    cnt = ''
    cnt += (f'<b> MoneyControl Top News: <b> <br>\n\n'  )
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find('ul',class_='tabs_nwsconlist').parent.find_all('li')):
        cnt += ((str(i+1) +"] "+  (tag.text).replace("\n","")   ).replace("\t","").strip() )
        cnt += ("\n \n <br> <br>")
    cnt+="<br>-------------------<br>\n\n INDEXES : "
    for i, tag in enumerate(soup.find('table',class_='rhsglTbl').parent.find_all('tr')):
        cnt += ((tag.text +'<br> ').replace("\n"," ").strip() )
        cnt += ("\n \n<br> ")
    cnt+="<br>-------------------<br>\n\n Top Gainers Today : \n"
    for i, tag in enumerate(soup.find('div',{"id":"maBSE"}).parent.find_all('tr')):
        cnt += ((tag.text +"<br>").replace("\n"," ").strip() )
        cnt += ("\n\n <br>")
        
        # print(tag.prettify) #find_all('span', attrs={'class':'sitestr'})
    return (cnt)





cnt = extract_news('https://www.moneycontrol.com/')


content += cnt
content += ('<br>------------<br>')


content += ('<br>------------<br>')
content += ('<br><br>End of Message source : www.moneycontrol.com \n This is Auto Generated Email. Happy Investing ! \n --Regards Satanshu! \nThis Email is only sent to keep you updated about stock markets. (Also a demo project) ')
        
print(content)

print('Composing Email')
# Update your email details
for i in range(len(emails)):
    SERVER = 'smtp.gmail.com' #your smtp server
    PORT = 587 #port Number
    FROM = 'satanshuwork247@gmail.com'
    # TO = 'defendersatya5@gmail.com'  #can send to multiple by using a python list of email ids

    TO = emails[i]
    PASS = AddPasswordstring #Your Email Pass


    msg = MIMEMultipart()

    msg['Subject'] = 'Top News Stories From MoneyControl [Automated Email]' + ' '+ str(now.day) + '-' + str(now.month) + '-' +  str(now.year) + " " + str(now.strftime("%H:%M"))
    msg['From'] = FROM
    msg['To'] = TO

    msg.attach(MIMEText(content, 'html'))
# fp.close()
    print('Initiating Server')
    server = smtplib.SMTP(SERVER, PORT)
    server.set_debuglevel(1) #if theres error we will get to know
    server.ehlo()   #e hello
    server.starttls()
    server.login(FROM,PASS)
    server.sendmail(FROM, TO, msg.as_string())
    print('email sent...')
server.quit()




