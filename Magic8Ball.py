#Magic8Ball.py
#Name: Elizabeth Wiggins
#Date: 2/1/25
#Assignment:Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")

  #Prompt the user for their question.
  input("What is your question?")
  response= print(random.choice(["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", 
            "Don't count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.",
             "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes-definitely.",
              "You may rely on it."]))
  #Answer question randomly with one of the options from your earlier list.


if __name__ == '__main__':
  main()

