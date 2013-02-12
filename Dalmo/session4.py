import requests
import sys
import getpass
from dateutil import parser
import datetime
from pandas import Series, DataFrame

password=getpass.getpass()
users = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=("tomasdalmo", password))
users_data = users.json()
messages_list=[]
date_list=[]
default="N/A"

for m in range(len(users_data)):
    commit_path=users_data[m]["commits_url"][:-6]
    commits=requests.get(commit_path, auth=("tomasdalmo", password))
    commits_data=commits.json()

    for n in range(len(commits_data)):
        try:
            commit_time=commits_data[n]["commit"]["author"]["date"]
            commit_message=commits_data[n]["commit"]["message"]
            time=parser.parse(commit_time)
            date_list.append(time)
            messages_list.append(commit_message)

        except KeyError:
             date_list.append(default)
             messages_list.append(default)
        

s = Series(messages_list, index=date_list, name="commit message")
DF=DataFrame(s)

print DF.values

