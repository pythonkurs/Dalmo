import requests
import sys
import getpass
from dateutil import parser
import datetime
from pandas import Series, DataFrame

password=getpass.getpass()
username=sys.argv[1]
GIT_API="https://api.github.com/orgs/pythonkurs/repos"
default="N/A"

def GetUserNamePassword(uname,pword):

    auth=(uname, pword)

    return auth


def GetUserInfo(gAPI,AUTH):
                       
    users = requests.get(gAPI, auth=AUTH)
    users_data = users.json()

    return users_data

def GetCommitList(Udata,AUTH):

    messages_list=[]
    date_list=[]

    for m in range(len(Udata)):

        commit_path = Udata[m]["commits_url"][:-6]
        commits = requests.get(commit_path, auth=AUTH)
        commits_data = commits.json()

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

    return s

def GetCommonDayHour(CList):

    DF=DataFrame(CList)
    n=0

    Weekdays_list=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    Weekdays_dict={'Mon':n,'Tue':n,'Wed':n,'Thu':n,'Fri':n,'Sat':n,'Sun':n}
    Hours_list=['01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','24:00']
    Hours_dict={'01:00':n,'02:00':n,'03:00':n,'04:00':n,'05:00':n,'06:00':n,'07:00':n,'08:00':n,'09:00':n,'10:00':n,'11:00':n,'12:00':n,'13:00':n,'14:00':n,'15:00':n,'16:00':n,'17:00':n,'18:00':n,'19:00':n,'20:00':n,'21:00':n,'22:00':n,'23:00':n,'24:00':n}

    for f in range(len(DF)):
        try:
            DAY=DF["Time"][f].weekday()
            Weekdays_dict[Weekdays_list[DAY]]+=1
            HOUR=DF["Time"][f].hour
            Hours_dict[Hours_list[HOUR]]+=1

        except AttributeError:
            pass

    COMMONWEEKDAY = max(Weekdays_dict, key=Weekdays_dict.get)
    COMMONHOUR = max(Hours_dict, key=Hours_dict.get)
    COMMON=[COMMONWEEKDAY, COMMONHOUR]

    return COMMON


def main():

    try:
        NamePass = GetUserNamePassword(username,password)
        UserInfo = GetUserInfo(GIT_API,NamePass)
        CommitList = GetCommitList(UserInfo,NamePass)
        CommonDayHour = GetCommonDayHour(CommitList)
        print "The most commmon day to commit is "+CommonDayHour[0]+" and the most common hour of any day to commit is at "+CommonDayHour[1]
    except KeyError:
        print "error"
    
    

if  __name__ =='__main__':main()



















