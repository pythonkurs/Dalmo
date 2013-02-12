import requests
import sys
import getpass
from dateutil import parser
import datetime
from pandas import Series, DataFrame

class (object):
    
    def __init__(self, dir):
        self.current = os.getcwd()
        self.new = dir
   	
    def __enter__(self):
        try:
            os.chdir(self.new)
        
        except OSError:
            print 'OSError: Path doesn\'t exists'
   	
    def __exit__(self, type, value, traceback):
        os.chdir(self.current)



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
        
s = {"Time" : Series(date_list), "Commit message" : Series(messages_list)}
DF=DataFrame(s)

DF
#print DF.values
n=0

Weekdays_list=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
Weekdays_dict={'Mon':n,'Tue':n,'Wed':n,'Thu':n,'Fri':n,'Sat':n,'Sun':n}
Hours_list=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
Hours_dict={'01:00':n,'02:00':n,'03:00':n,'04:00':n,'05:00':n,'06:00':n,'07:00':n,'08:00':n,'09:00':n,'10:00':n,'11:00':n,'12:00':n,'13:00':n,'14:00':n,'15:00':n,'16:00':n,'17:00':n,'18:00':n,'19:00':n,'20:00':n,'21:00':n,'22:00':n,'23:00':n,'24:00':n}

for f in range(len(DF)):
    try:
        DAY=DF["Time"][f].weekday()
        Weekdays_dict[Weekdays_list[DAY]]+=1
        HOUR=DF["Time"][f].hour
        Hours_dict[Hours_list[HOUR]]+=1

    
    except AttributeError:
        pass

MW=max(Weekdays_dict, key=Weekdays_dict.get)
MH=max(Hours_dict, key=Hours_dict.get)


print MW, MH

