#FutureTime.py
#Name:Elizabeth Wiggins
#Date:2/1/25
#Assignment:Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour-5)%24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
moreHours=input("Number of Hours:")
  
  #Ask user for minutes
moreMins= input("Number of Minutes:")

futureMins= (currentMinute+moreMins)%60
extraHour= (currentHour+moreHours)//60
print(extraHour)
print (futureMins)

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
