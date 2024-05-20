import datetime

alarmHour=int(input("Enter an hour:"))
alarmMinute=int(input("Enter a minute:"))

amPm=str(input("am or pm:"))

if(amPm == "pm"):
    alarmHour=alarmHour+12

while True:
    if(alarmHour==datetime.datetime.now().hour and alarmMinute==datetime.datetime.now().minute):
        print("Alarm ringing...")
        break

print("Exited")