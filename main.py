import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import enum
import eel



#GLOBALS 


#is the program in a test state 
Test = True
#is the program logged in? 
LoggedIn = False
#Whats the user name 
Username =""
#whats the password 
Password = ""
#open chrome 
driver = webdriver.Chrome()

#close Everything 
@eel.expose
def EndProgram():
    driver.quit()
    quit(1)

#saves login to file
@eel.expose
def SaveLogin(Username,Password):
    FiletoSave = open("input.txt", "w")
    FiletoSave.write(Username)
    FiletoSave.write("\n")
    FiletoSave.write(Password)
    FiletoSave.close()

#logins to program 
def Login():
    global Username
    global Password
    driver.get("https://www.digiquatics.com/patron_counts/new?location_id=10991")
    driver.find_element_by_id("user_email").send_keys(Username)
    driver.find_element_by_id("user_password").send_keys(Password)
    driver.find_element_by_name("commit").click()
    #driver.get("https://www.digiquatics.com/patron_counts/new?location_id=10991")

#get the size of a file 
@eel.expose
def GetFileSize(FileInThing):
    size = 0
    for line in FileInThing:
        size+=1
    return size


#Loads Login from file 
def LoadLogin():
    #define usable globals 
    global Username
    global Password
    global LoggedIn
    #open file "input.txt" for reading 
    FileInputIn = open("input.txt", "r")
    #check file size and setup size 
    size = GetFileSize(FileInputIn)
    #if there are the correct number of vars store them in correct vars 
    if size == 2:
        tx = 0
        FileInputIn = open("input.txt", "r")
        for line in FileInputIn:
            if tx == 0:
                Username = line
            if tx == 1:
                Password = line
            tx+=1

        return(True)
    else:
        #if there is not enough vars return false 
        return(False)

#print from js 
@eel.expose
def PyPrint(print):
    print(print)

#the main function !
@eel.expose
def Start():
    print("program started")
    BLoadLogin = LoadLogin()
    #check if login was able to be done if not load the setup page if not login! 
    if BLoadLogin == False:
        eel.LoadSetupPage()
    elif BLoadLogin == True:
        Login()

#enum for weekdays
class Day(enum.Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday= 6
    Sunday = 7

#ONE TIME takes DateIn(1/10/2022) DayofWeek(int = day of week 0 being monday ) LapIn(an array of all lap data) ActIn( an array of all Activitiy data )
@eel.expose
def OneTime(DateIn, DayofWeek, LapIn, ActIn):
    #loads Patron Page 
    driver.get("https://www.digiquatics.com/patron_counts/new?location_id=10991")
    #Sets Wday up Monday is a placeholder
    Wday = Day.Monday
    #setup vars from js 
    #string of the raw date from JS 
    Date = DateIn
    #Array of the LAp 
    Lap = LapIn
    #array of the activity pool 
    Activity = ActIn

    #Based on the day Setup the ENUM 
    if DayofWeek == 0:
        Wday = Day.Monday
    if DayofWeek == 1:
        Wday = Day.Tuesday
    if DayofWeek == 2:
        Wday = Day.Wednesday
    if DayofWeek == 3:
        Wday = Day.Thursday
    if DayofWeek == 4:
        Wday = Day.Friday
    if DayofWeek == 5:
        Wday = Day.Saturday
    if DayofWeek == 6:
        Wday = Day.Sunday


    #tnum defind the hour of the day starting at 0 so if we open at 8 then 0 would be 8am 
    tnum = 0
    #number of hours in that speciifc day
    numhours = 0
    #start time of that day 
    starttime =0
    #where we are in the activity array  
    ActCount = 0
    #where we are int the lap array 
    LapCount = 0
    #detects day and prints any errors 
    if Wday == Day.Monday:
        print("Mon")
        numhours = 16
        starttime = 5
        if len(Activity) != 32:
            print("Check Activity there is either too many or too little... ")
            print(Activity)
            print(len(Activity))
            print("32")
            quit(2)
        if len(Lap) != 26:
            print("Check Lap there is either too many or too little... ")
            print(Lap)
            print(len(Lap))
            print("26")
            quit(2)
    if Wday == Day.Tuesday:
        print("Tues")
        numhours = 16
        starttime = 5
        if len(Activity) != 32:
            print("Check Activity there is either too many or too little... ")
            print(Activity)
            print(len(Activity))
            print("32")
            quit(2)
        if len(Lap) != 26:
            print("Check Lap there is either too many or too little... ")
            print(Lap)
            print(len(Lap))
            print("26")
            quit(2)
    if Wday == Day.Wednesday:
        print("Wed")
        numhours = 16
        starttime = 5
        if len(Activity) != 32:
            print("Check Activity there is either too many or too little... ")
            print(Activity)
            print(len(Activity))
            print("32")
            quit(2)
        if len(Lap) != 26:
            print("Check Lap there is either too many or too little... ")
            print(Lap)
            print(len(Lap))
            print("26")
            quit(2)
    if Wday == Day.Thursday:
        print("Thrs")
        numhours = 16
        starttime = 5
        if len(Activity) != 32:
            print("Check Activity there is either too many or too little... ")
            print(Activity)
            print(len(Activity))
            print("32")
            quit(2)
        if len(Lap) != 26:
            print("Check Lap there is either too many or too little... ")
            print(Lap)
            print(len(Lap))
            print("26")
            quit(2)
    if Wday == Day.Friday:
        print("Fri")
        numhours = 15
        starttime = 5
        if len(Activity) != 28:
            print("Check Activity there is either too many or too little... ")
            print(Activity)
            print(len(Activity))
            print("26")
            quit(2)
        if len(Lap) != 21:
            print("Check Lap there is either too many or too little... ")
            print(Lap)
            print(len(Lap))
            print("16")
            quit(2)
    if Wday == Day.Saturday:
        numhours = 9
        starttime = 8
        print("Sat")
        if len(Activity) != 17:
            print("Check Activity there is either too many or too little... ")
            print(Activity)
            print(len(Activity))
            print("17")
            quit(2)
        if len(Lap) != 15:
            print("Check Lap there is either too many or too little... ")
            print(Lap)
            print(len(Lap))
            print("15")
            quit(2)
    if Wday == Day.Sunday:
        numhours = 9
        starttime = 8
        print("Sun")
        if len(Activity) != 17:
            print("Check Activity there is either too many or too little... ")
            print(Activity)
            print(len(Activity))
            print("17")
            quit(2)
        if len(Lap) != 15:
            print("Check Lap there is either too many or too little... ")
            print(Lap)
            print(len(Lap))
            print("15")
            quit(2)
    #FOR EACH DAY !!!
    for x in range(1,numhours+1):
        #click Date field
        driver.find_element_by_id("createdAtPicker").click()

        #clears date field with ctrl + a then del
        ActionChains(driver) \
            .key_down(Keys.CONTROL) \
            .key_down("a") \
            .key_up(Keys.CONTROL) \
            .key_up("a") \
            .key_down(Keys.DELETE) \
            .key_up(Keys.DELETE) \
            .perform()

        #Date = "11/13/2021 " #Month Day Year (leave space after !!!!) 
        #creates the Date from a hogpoge 
        DateTime = ((starttime-1)+x)%12
        texttime =""
        texttime += Date
        texttime += str(DateTime)
        texttime += ":00 "
        #determinds am or pm 
        if ((starttime-1)+x) >= 12:
            texttime += "PM"
        else:
            texttime += "AM"
        #sends keys and presses enter 
        driver.find_element_by_id("createdAtPicker").send_keys(texttime)
        driver.find_element_by_id("createdAtPicker").send_keys(Keys.ENTER)
        #driver.find_element_by_class_name("form-control").click()
        #needs sleep time for webpage to catch up with porgram (Py is fast) 
        time.sleep(.5)
        elementstest = driver.find_elements_by_class_name("form-control")



        # code Days
        #define inputs for each day 
        if Wday == Day.Monday:
            print("Monday")
            if tnum <=3:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys("0")#Spectators
                elementstest[8].send_keys("0")#Aqua Aerobics
            if tnum == 4:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys(Activity[ActCount])#Aqua Zumba
                ActCount += 1
                elementstest[7].send_keys(Activity[ActCount])#Spectators
                ActCount += 1
                elementstest[8].send_keys("0")#Aqua Aerobics
            if tnum == 5:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[6].send_keys(Activity[ActCount])#Aqua Zumba
                ActCount += 1
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons

                elementstest[7].send_keys(Activity[ActCount])#Spectators
                ActCount += 1
                elementstest[8].send_keys("0")#Aqua Aerobics

            if tnum >5 and tnum <9:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(Activity[ActCount])#Spectators
                ActCount += 1
                elementstest[8].send_keys("0")#Aqua Aerobics

            if tnum == 9 or tnum == 10 or tnum == 15:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1
                elementstest[8].send_keys("0")#Aqua Aerobics
            if tnum == 11:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Swim Lessons
                LapCount += 1
                ActCount += 1
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1
                elementstest[8].send_keys("0")#Aqua Aerobics
            if tnum == 12:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Swim Lessons
                LapCount += 1
                ActCount += 1
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1
                elementstest[8].send_keys("0")#Aqua Aerobics
            if tnum == 13:
                elementstest[2].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[1].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Swim Lessons
                LapCount += 1
                ActCount += 1
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1
                elementstest[8].send_keys("0")#Aqua Aerobics
            if tnum == 14:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1
                elementstest[8].send_keys("0")#Aqua Aerobics
        if Wday == Day.Tuesday:
            print("Tuesday")
            if tnum <=3:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys("0")#Spectators

            if tnum == 4:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys(Activity[ActCount])#Swim Lessons
                ActCount += 1
                elementstest[6].send_keys(Activity[ActCount])#Spectators
                ActCount += 1

            if tnum == 5:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[5].send_keys(Activity[ActCount])#Swim Lessons
                ActCount += 1
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1


                elementstest[6].send_keys(Activity[ActCount])#Spectators
                ActCount += 1


            if tnum >5 and tnum <9:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons

                elementstest[6].send_keys(Activity[ActCount])#Spectators
                ActCount += 1


            if tnum == 9 or tnum == 10 or tnum == 15:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons

                elementstest[6].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 11:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Swim Lessons
                LapCount += 1
                ActCount += 1

                elementstest[6].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 12:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Swim Lessons
                LapCount += 1
                ActCount += 1

                elementstest[6].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 13:
                elementstest[2].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[1].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Swim Lessons
                LapCount += 1
                ActCount += 1

                elementstest[6].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 14:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons

                elementstest[6].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1
        if Wday == Day.Wednesday:
            print("Wednesday")
            if tnum <=3:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys("0")#Spectators

            if tnum == 4:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys(Activity[ActCount])#Aqua Zumba
                ActCount += 1
                elementstest[7].send_keys(Activity[ActCount])#Spectators
                ActCount += 1

            if tnum == 5:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[6].send_keys(Activity[ActCount])#Aqua Zumba
                ActCount += 1
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons

                elementstest[7].send_keys(Activity[ActCount])#Spectators
                ActCount += 1


            if tnum >5 and tnum <9:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(Activity[ActCount])#Spectators
                ActCount += 1


            if tnum == 9 or tnum == 10 or tnum == 15:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 11:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Swim Lessons
                LapCount += 1
                ActCount += 1
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 12:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Swim Lessons
                LapCount += 1
                ActCount += 1
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 13:
                elementstest[2].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[1].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Swim Lessons
                LapCount += 1
                ActCount += 1
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 14:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")#Adult/River
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")#Swim Lessons
                elementstest[6].send_keys("0")#Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1
        if Wday == Day.Thursday:
            print("Thursday")
            if tnum <= 3:
                elementstest[1].send_keys(Lap[LapCount])  # Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")  # Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])  # Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")  # Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")  # Swim Lessons
                elementstest[6].send_keys("0")  # Aqua Zumba
                elementstest[7].send_keys("0")  # Spectators

            if tnum == 4:
                elementstest[1].send_keys(Lap[LapCount])  # Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")  # Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])  # Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")  # Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")  # Swim Lessons
                elementstest[6].send_keys(Activity[ActCount])  # Aqua Zumba
                ActCount += 1
                elementstest[7].send_keys(Activity[ActCount])  # Spectators
                ActCount += 1

            if tnum == 5:
                elementstest[1].send_keys(Lap[LapCount])  # Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")  # Open Swim (Lap Pool)
                elementstest[3].send_keys("0")  # Adult/River
                elementstest[6].send_keys(Activity[ActCount])  # Aqua Zumba
                ActCount += 1
                elementstest[4].send_keys(Activity[ActCount])  # Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")  # Swim Lessons

                elementstest[7].send_keys(Activity[ActCount])  # Spectators
                ActCount += 1

            if tnum > 5 and tnum < 9:
                elementstest[1].send_keys(Lap[LapCount])  # Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")  # Open Swim (Lap Pool)
                elementstest[3].send_keys("0")  # Adult/River
                elementstest[4].send_keys(Activity[ActCount])  # Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")  # Swim Lessons
                elementstest[6].send_keys("0")  # Aqua Zumba
                elementstest[7].send_keys(Activity[ActCount])  # Spectators
                ActCount += 1

            if tnum == 9 or tnum == 10 or tnum == 15:
                elementstest[1].send_keys("0")  # Lap Swim (Lap Pool)
                elementstest[2].send_keys(Lap[LapCount])  # Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")  # Adult/River
                elementstest[4].send_keys(Activity[ActCount])  # Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")  # Swim Lessons
                elementstest[6].send_keys("0")  # Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))  # Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 11:
                elementstest[1].send_keys("0")  # Lap Swim (Lap Pool)
                elementstest[2].send_keys(Lap[LapCount])  # Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")  # Adult/River
                elementstest[4].send_keys(Activity[ActCount])  # Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))  # Swim Lessons
                LapCount += 1
                ActCount += 1
                elementstest[6].send_keys("0")  # Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))  # Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 12:
                elementstest[1].send_keys("0")  # Lap Swim (Lap Pool)
                elementstest[2].send_keys("0")  # Open Swim (Lap Pool)
                elementstest[3].send_keys("0")  # Adult/River
                elementstest[4].send_keys("0")  # Open Swim (Leisure Pool)
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))  # Swim Lessons
                LapCount += 1
                ActCount += 1
                elementstest[6].send_keys("0")  # Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))  # Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 13:
                elementstest[2].send_keys("0")  # Lap Swim (Lap Pool)
                elementstest[1].send_keys(Lap[LapCount])  # Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")  # Adult/River
                elementstest[4].send_keys(Activity[ActCount])  # Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))  # Swim Lessons
                LapCount += 1
                ActCount += 1
                elementstest[6].send_keys("0")  # Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))  # Spectators
                LapCount += 1
                ActCount += 1

            if tnum == 14:
                elementstest[1].send_keys(Lap[LapCount])  # Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys(Lap[LapCount])  # Open Swim (Lap Pool)
                LapCount += 1
                elementstest[3].send_keys("0")  # Adult/River
                elementstest[4].send_keys(Activity[ActCount])  # Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys("0")  # Swim Lessons
                elementstest[6].send_keys("0")  # Aqua Zumba
                elementstest[7].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))  # Spectators
                LapCount += 1
                ActCount += 1
        if Wday == Day.Friday:
            print("Friday")
            if tnum <= 3:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")#Aqua Zumba
                elementstest[6].send_keys("0")#Spectators
            if tnum == 4:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys(Activity[ActCount])#Aqua Zumba
                ActCount += 1
                elementstest[6].send_keys(Activity[ActCount])#Spectators
                ActCount += 1
            if tnum == 5:
                elementstest[1].send_keys(Lap[LapCount])  # Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")  # Open Swim (Lap Pool)
                elementstest[3].send_keys("0")  # Adult/River
                elementstest[5].send_keys(Activity[ActCount])  # Aqua Zumba
                ActCount += 1
                elementstest[4].send_keys(Activity[ActCount])  # Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[6].send_keys(Activity[ActCount])  # Spectators
                ActCount += 1
            if tnum > 5 and tnum < 9:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")#Aqua Zumba
                elementstest[6].send_keys(Activity[ActCount])#Spectators
                ActCount += 1
            if tnum > 8:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")#Aqua Zumba
                elementstest[6].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                ActCount += 1
                LapCount += 1
        if Wday == Day.Saturday:
            print("Saturday")
            if tnum == 0 or tnum ==1:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount +=1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount+=1
                elementstest[4].send_keys("0")#Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")#Spectators
            if tnum == 2:
                elementstest[1].send_keys(Lap[LapCount])#Lap Swim (Lap Pool)
                LapCount += 2
                elementstest[3].send_keys(Activity[ActCount])#Adult/River
                ActCount += 1
                elementstest[2].send_keys("0")#Open Swim (Lap Pool)


                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(Activity[ActCount])#Spectators
                ActCount += 1
            if tnum == 3:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(Activity[ActCount])#Spectators
                ActCount += 1
            if tnum > 3:
                elementstest[1].send_keys("0")#Lap Swim (Lap Pool)
                elementstest[3].send_keys("0")#Adult/River
                elementstest[2].send_keys(Lap[LapCount])#Open Swim (Lap Pool)
                LapCount += 1
                elementstest[4].send_keys(Activity[ActCount])#Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))#Spectators
                LapCount += 1
                ActCount += 1
        if Wday == Day.Sunday:
            print("Saturday")
            if tnum == 0 or tnum == 1:
                elementstest[1].send_keys(Lap[LapCount])  # Lap Swim (Lap Pool)
                LapCount += 1
                elementstest[2].send_keys("0")  # Open Swim (Lap Pool)
                elementstest[3].send_keys(Activity[ActCount])  # Adult/River
                ActCount += 1
                elementstest[4].send_keys("0")  # Open Swim (Leisure Pool)
                elementstest[5].send_keys("0")  # Spectators
            if tnum == 2:
                elementstest[1].send_keys(Lap[LapCount])  # Lap Swim (Lap Pool)
                LapCount += 2
                elementstest[3].send_keys(Activity[ActCount])  # Adult/River
                ActCount += 1
                elementstest[2].send_keys("0")  # Open Swim (Lap Pool)

                elementstest[4].send_keys(Activity[ActCount])  # Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(Activity[ActCount])  # Spectators
                ActCount += 1
            if tnum == 3:
                elementstest[1].send_keys("0")  # Lap Swim (Lap Pool)
                elementstest[3].send_keys("0")  # Adult/River
                elementstest[2].send_keys(Lap[LapCount])  # Open Swim (Lap Pool)
                LapCount += 1
                elementstest[4].send_keys(Activity[ActCount])  # Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(Activity[ActCount])  # Spectators
                ActCount += 1
            if tnum > 3:
                elementstest[1].send_keys("0")  # Lap Swim (Lap Pool)
                elementstest[3].send_keys("0")  # Adult/River
                elementstest[2].send_keys(Lap[LapCount])  # Open Swim (Lap Pool)
                LapCount += 1
                elementstest[4].send_keys(Activity[ActCount])  # Open Swim (Leisure Pool)
                ActCount += 1
                elementstest[5].send_keys(str(int(Lap[LapCount]) + int(Activity[ActCount])))  # Spectators
                LapCount += 1
                ActCount += 1

        tnum+=1
        #my Test Stuff !! 
        #input("COntinue????")
        #driver.find_element_by_class_name("btn btn-pink full-width").move_to_element()






        #DANGER
        #DANGER
        #DANGER
        #DANGER
        #DANGER
        #DANGER
        if Test == False: 
            print("submitted: " + texttime)
            #driver.find_element_by_class_name("btn-pink").click()
        #DANGER
        #DANGER
        #DANGER
        #DANGER
        #DANGER



        driver.get("https://www.digiquatics.com/patron_counts/new?location_id=10991")


def ChemCheck(DateIn, LapIn, ActIn):
    print("ran Chem") 


def SetupChem():
    print("settingup chems")
def SetupPatron():
    print("setting up patron")


def main():
    #goes to folder Website and launcher main.html 
    eel.init('Website')
    eel.start('home.html')
#if its main run main 
if __name__ == "__main__":
    main()
