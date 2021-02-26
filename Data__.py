from selenium import webdriver 
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options
import time as t

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get ("https://app.coderpad.io/login")
driver.find_element_by_id("user_email").send_keys("tcscoding28@gmail.com")
driver.find_element_by_id("user_password").send_keys("TCS12345")
driver.find_element_by_name("commit").click()
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("tcscoding13@gmail.com", "TCS12345")

def createPad(name, lang, mail, date, contents, user, time):
    global driver
    driver.get("https://www.app.coderpad.io/dashboard/pads")
    driver.find_element_by_xpath("//input[@type='submit']").click();
    driver.switch_to.window(driver.window_handles[1])
    rwdata = driver.find_element_by_class_name("TitlePrompt").get_attribute("value")
    driver.find_element_by_class_name("TitlePrompt").clear()
    driver.find_element_by_class_name("TitlePrompt").send_keys(name + "'s Coder Pad")
    t.sleep(2.4)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("https://app.coderpad.io/" + rwdata.split(" ")[-1])
    url = "https://app.coderpad.io/" + rwdata.split(" ")[-1]
    print(name, lang, mail, date, contents, user, time)
    #print(response.json()['url'])
    sendMail(url, name, user, mail, date, lang.lower(), time)
    print(url, name, user, mail, date, lang.lower(), time)
    return url
    
def sendMail(link, name, user, mail, date, language, time):
    global s
    message1 = MIMEMultipart("alternative")
    message1["Subject"] = "TCS Coding Test"
    message1["From"] = "tcscoding9@gmail.com"
    message1["To"] = mail
    # saravanan.bose@tcs.com,kirti.varma@tcs.com,aravind.bhaskar@tcs.com,a.vamsi3@tcs.com
    names = {
        "java" : {
           # "cc" : "keerthy.g@tcs.com,saravanan.bose@tcs.com,kirti.varma@tcs.com,aravind.bhaskar@tcs.com,a.chaitanyakumari@tcs.com,a.vamsi3@tcs.com,venkateswar.balineni@tcs.com",
            "name" : "Vamsi Krishna",
            "mobile" : "9949165110",
            "meet" : " https://meet.google.com/mez-dxpo-spy"
        },
        'javascript' : {
            "cc" : "saravanan.bose@tcs.com,kirti.varma@tcs.com,s.saranya26@tcs.com,riya.sharma4@tcs.com,akashdeep.patra@tcs.com",
            "name" : "Riya Sharma",
            "mobile" : "9465639883",
            "meet" : "https://meet.google.com/ray-yjcu-qjf"
        },
        'python3' : {
            "cc" : "saravanan.bose@tcs.com,kirti.varma@tcs.com,sharma.aditya15@tcs.com,venkateswar.balineni@tcs.com",
            "name" : "Aditya Sharma",
            "mobile" : "7987252850",
            "meet" : "https://meet.google.com/dwa-tmba-tru"
        }
    }
    message1["Cc"] = names[language]["cc"]
    message = "Hi " + name + ",\nWish you Good day!\n\n\tI am " + names[language]["name"] + " from TCS, scheduling a " + language + " coding test for " + date + ". Please join the coder pad link and google meet at " + time + " through the below link\n\nMeet Link : " + names[language]["meet"] + "\n\nCoder pad link: " + link + "\n\nKindly acknowledge and if you have any queries please let me know.\n\nRegards,\n" + names[language]["name"] + "\n" + names[language]["mobile"]
    #msg.attach(message) 
    message1.attach(MIMEText(message, "plain"))
    print(message)
    s.sendmail("tcscoding13@gmail.com", names[language]["cc"].split(",") + [mail], message1.as_string())

f = open("list.csv", "r")
f1 = open("list_updated.csv", "w")
data = [i[:-1] for i in f.readlines()]
f1.write(data[0] + ",Coder Pad Link\n")
for i in data[1:]:
    record = i.split(",")
    f1.write(i + "," + createPad(record[0], record[1], record[2], record[3], " ", 0, record[4]) + "\n")
f.close()
f1.close()
