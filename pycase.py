import time
import os   # to access env variables & do sys calls
import subprocess   # Note: os.system("date") executes the date shell command but its output is forced to the screen.  Instead, subprocess.checkout("date") suppresses output of the command and captures it as a string.  Use this when evaluating shell commands within larger python expressions or when the output needs to be stored rather than displayed right away.

start_time = time.time()    # store script start time

def display_menu(): 
  os.system("clear")
  print """
Menu Options

  1)  Display menu options.
  2)  Display username.
  3)  Display date and calendar.
  4)  Display script name and its uptime in seconds.
  0)  Quit"""
  return
 

### Start program ###

display_menu();

print
reply = int(input("Enter a selection [0-4] > "))
while (reply != 0):
  if (reply == 1):
    display_menu();
  elif (reply == 2):
    print("User name: " + os.environ["USER"])
  elif (reply == 3):
    print("Date: " + subprocess.check_output("date"))
    os.system("cal")
  elif (reply == 4):
    print("Script name: " + os.path.basename(__file__))
    end_time = time.time()
    uptime = int(end_time - start_time)  # int to truncate decimal portion of time
    print("Script uptime: " + str(uptime) + " seconds")
  else:
    print("Invalid option.  Please try again.")
  print
  reply = int(input("Enter another selection [0-4] > "))

print("Goodbye")
