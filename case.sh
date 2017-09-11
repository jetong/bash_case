#!/bin/bash

display_menu() {
  clear
  echo "
Menu Options

  1)  Display menu options.
  2)  Display username.
  3)  Display date and calendar.
  4)  Display script name and its uptime in seconds.
  0)  Quit
  "
  return
}

### Start program ###

display_menu;

read -p "Enter selection [0-4] > "  # -p displays prompt for input
while [[ $REPLY -ne 0 ]]; do
  case $REPLY in
    1)  display_menu
        ;;
    2)  echo "Username: $USER"
        ;;
    3)  echo -e "Date: $(date)\n"   # -e option enables interpretation of \n
        echo "$(cal)"
        ;; 
    4)  echo "Script name: $0"
        echo "Script uptime: $SECONDS seconds"
        ;;
    *)  echo "Invalid option, please try again."
        ;;
  esac
    if [[ $REPLY != 1 ]]; then  # print newline after each case, except for 1)
      echo  
    fi
    read -p "Enter another selection [0-4] > "
done

echo "Goodbye"
