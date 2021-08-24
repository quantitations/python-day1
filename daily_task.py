
#### Get today's "Quote of the Day"

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.brainyquote.com/quote_of_the_day")
s = BeautifulSoup(r.text, features="html5lib")

div = s.find("div", class_="mblCenterPhot").find("div", class_="grid-item")
div

quote = div.find("a", attrs={"title": "view quote"}).text
quote
quote = quote.strip()

author = div.find("a", attrs={"title": "view author"}).text
author


#### Write it to a file

from datetime import date
from pathlib import Path

# make directory for journal entries if it doesn't exist
journal_dir = Path("C:/Users/12565/Documents/journal-entries")
journal_dir.mkdir(parents=True, exist_ok=True)

# create today's entry file
today_file = journal_dir / (date.today().isoformat() + ".txt")
with today_file.open("w") as f:
    f.write(f'"{ quote }"\n -- { author }\n\n ------- my thoughts -------\n\n\n')



#### Open it in notepad (for Windows users)

import os

os.system("notepad " + str(today_file))


# This can be run from Anaconda Prompt: navigate to the containing folder and run
# python daily_task.py
# You can even make it run automatically every day at a specified time using "Task Scheduler".
# Set task scheduler to run python with this filename as the argument.
# I specified the Python from my anaconda installation "C:\Users\12565\Anaconda3\python.exe"
# and the absolute path of this script as the argument "C:\Users\12565\python-day1\daily_task.py"
