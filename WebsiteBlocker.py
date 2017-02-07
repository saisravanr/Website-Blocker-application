__author__ = 'Rachiraju'
from datetime import datetime as dt
import time

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list =["www.facebook.com","fb.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,16) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("Sorry Working Hours...")
        #Change to hosts_path
        with open(hosts_temp, 'r+') as file:
            contents = file.read()
            for website in website_list:
                if website in contents:
                    pass
                else:
                    file.write(redirect + ' ' + website + "\n")
    else:
        #Change to hosts_path
        with open(hosts_temp, 'r+') as file:
            contents = file.readlines()
            file.seek(0)
            for line in contents:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
            print("Yayy Fun Hours..")
    time.sleep(5)