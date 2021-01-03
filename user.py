import requests
import json
import csv
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


url = 'https://api.github.com/users'


def tot_user_details(): 
    user_details = requests.get(url).json()
    return user_details


def users_log(login): 
    user_log_details = requests.get(url+f'/{login}').json()
    return user_log_details


def tot_followers_details(login):
    followers_details = requests.get(url+f'/{login}/followers').json()
    return followers_details
    
    
all_user_data = tot_user_details()
rows = []
for user in all_user_data:
    if user["id"] % 10 == 0:  
        suser_data = users_log(user["login"])
        followers_details = tot_followers_details(suser_data["login"])

        for followers in followers_details:
            rows.append([user["id"], user["login"], suser_data["name"], followers["id"], followers['login']])


with open("Master.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['UserId', 'UserLogin', 'UserName', 'FollowerId', 'FollowerLogin'])
    csvwriter.writerows(rows)

    
def upload_drive(): 
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({"mimeType": "text/csv"})
    file.SetContentFile(r"Master.csv")
    file.Upload()
    
upload_drive()
