
############################################################
################ Part 1: Parsing an html file ##############
############################################################


from pathlib import Path

# https://beautiful-soup-4.readthedocs.io/en/latest/#
# make sure you have the bs4 package
from bs4 import BeautifulSoup

html_file = Path("example.html")
s = BeautifulSoup(html_file.read_text())


## Searching the document ##

# Get first occurrence of a given type of html element
s.table
# Get the first "tr" element from the first "table" element
s.table.tr

# Get all occurrence of a given type of html element
s.find_all("p")

# Get all occurrence of a given list of types of html element
s.find_all(["td", "th"])

# Get first occurrence of an html element with a given "id" attribute value
s.find(id="cases2019")
# Get all "th" elements from within this element
s.find(id="cases2019").find_all("th")

# Loop through the "tr" elements within the first "table" element
for row in s.table.find_all("tr"):
    print(row.td)

# Get all occurrence of "p" elements with class "after-data"
s.find_all("p", attrs={"class": "after-data"})

# You can also search using a regular expression.
# For example, the following line finds every element whose "id" has
# four consecutive digits in it.
import re
s.find_all(id=re.compile("[0-9]{4}"))


## Extracting attributes and text ##

s.table["id"]
s.a["href"]

c = s.find(id="conclusion")
c
c.name
c.attrs # dictionary object
c.text
c["class"] # if multiple such attributes, returns a list
c.contents
c.text
c.parent


## EXERCISE 1: Create a list conmprising the 12 numbers from the 2019 table.





############################################################
########### Part 2: Acquiring data from the web ############
############################################################


## Web scraping example 1 ##
## - Get a publication date from Wikipedia ##

# https://docs.python-requests.org/en/master/
# make sure you have the requests package
import requests

booktitle = "The_Brothers_Karamazov"
url = "https://en.wikipedia.org/wiki/" + booktitle
r = requests.get(url)
# Navigate to https://en.wikipedia.org/wiki/The_Brothers_Karamazov
# right click on the background and select "View Source" to see the html
# that we're dealing with here.
# (These instructions may not be exactly right for you to see the html,
# as the process varies from browser to browser.)

s = BeautifulSoup(r.text)

trs = s.find("table", attrs={"class": "infobox"}).find_all("tr")
for tr in trs:
    if "Publication date" in tr.text:
        text = tr.text
        break

text

# Regular expressions are also useful for extracting data from an html file.
# Let's just grab the first sequence of four digits.
re.findall("[0-9]{4}", text)[0]


## EXERCISE 2: Write code to scrape the author from the Brothers Karamazov's
##             Wikipedia page. Define a function getAuthor that takes a book's
##             title and attempts to get the name of the author(s) from the
##             corresponding Wikipedia page. Your function should first replace
##             all spaces with underscores in order to guess the url.
##             (Note, this won't work for every book.)
##             Check that getAuthor("The Brothers Karamazov")
##             and getAuthor("Paradise Lost") work as expected.








## Web scraping example 2 ##
## - Get a list of the most popular books on Project Gutenberg ##

r = requests.get("https://www.gutenberg.org/ebooks/search/?sort_order=downloads")
s = BeautifulSoup(r.text)

book = s.find("li", attrs={'class': 'booklink'})
book

# Let's figure out how to extract the information we want for this book:
# title, number of downloads, and ID number

# title
book.find("span", attrs={'class': 'title'}).text

# downloads over the last 30 days
int(book.find("span", attrs={'class': 'extra'}).text.split()[0])

# ID
int(book.a['href'].split('/')[2])


# Grab the desired data for every result on this page.

# initialize empty lists
title = []
downloads = []
ID = []

books = s.findAll("li", attrs={'class': 'booklink'})


# loop through the results, appending the lists with the data as we go
for book in books:
    title.append(book.find("span", attrs={'class': 'title'}).text)
    downloads.append(int(book.find("span", attrs={'class': 'extra'}).text.split()[0]))
    ID.append(int(book.a['href'].split('/')[2]))

# Let's save the book data as a DataFrame object (from the pandas package).
import pandas
books = pandas.DataFrame({"ID": ID, "title": title, "downloads": downloads})
books
# For more on the pandas package, you might consult our
# "Python for Data Science" workshop material
# (and/or any number of online resources).


# Let's do this for every page of results to make a list of the 1000 most popular books.

# check that we can list the urls that we'll want to request
nums = [i*25+1 for i in range(40)]
for i in nums:
    print(f"https://www.gutenberg.org/ebooks/search/?sort_order=downloads&start_index={ i }")

import time

title = []
downloads = []
ID = []

S = requests.Session()

for i in nums:
    r = S.get(f"https://www.gutenberg.org/ebooks/search/?sort_order=downloads&start_index={ i }")
    s = BeautifulSoup(r.text)
    for book in s.findAll("li", attrs={'class': 'booklink'}):
        title.append(book.find("span", attrs={'class': 'title'}).text)
        downloads.append(int(book.find("span", attrs={'class': 'extra'}).text.split()[0]))
        ID.append(int(book.find("a")['href'].split('/')[2]))
    time.sleep(30) # always be kind to servers -- wait a bit between requests

books = pandas.DataFrame({"ID": ID, "title": title, "downloads": downloads})





## EXERCISE 3: Write Python code to scrape the 85 Federalist Papers available from
##             http://avalon.law.yale.edu/subject_menus/fed.asp
##             and write them to files named "fed01.txt", "fed02.txt", etc.







## API example ##
## - reddit ##

# Sometimes a server will offer an API, which is an alternative way to access
# specific pieces of information, so that you don't have to go through all
# the work of "scraping" it out of an otherwise irrelevant html file.
# The API will have instructions for constructing http requests that
# specify the data that you'd like to receive.

# You can look up reddit's documentation and examples to learn what urls to use
# and what type of response to expect (json).
# documentation: www.reddit.com/dev/api
# example: www.pythonforbeginners.com/python-on-the-web/how-to-use-reddit-api-in-python/


# Let's get the current top posts from the "books" subreddit

r = requests.get("http://www.reddit.com/r/books/top/.json")
d = r.json()
d

# If that didn't work, try the following...

r = requests.get("http://www.reddit.com/r/books/top/.json", headers = {'User-agent': 'wdb'})
d = r.json()

# Here's the part of the response corresponding to the top post
print(d["data"]["children"][0])
# The title of that post:
print(d["data"]["children"][0]["data"]["title"])

# The titles of all the posts in the response
for post in d["data"]["children"]:
    print("---" + post["data"]["title"])

# The user who submitted the current top post:
username = d["data"]["children"][0]["data"]["author"]
username

# Next, let's get the recent comments of this user
r = requests.get("http://www.reddit.com/user/%s/comments/.json" % username, headers = {'User-agent': 'wdb'})
e = r.json()
print(e["data"]["children"][0])

for comment in e["data"]["children"]:
    print("---" + comment["data"]["body"])










############################## SOLUTIONS #####################################

## SOLUTION 1 ##

nums = []
for row in s.find(id="cases2019").find_all("tr"):
    tds = row.find_all("td")
    if tds:
        nums.append(tds[1].text)

# here's another way you might do it (using list comprehension)
nums = [e.text for e in s.find(id="cases2019").find_all("td")[1::2]]


## SOLUTION 2 ##

# I'm doing the loop a little differently this time to be more careful
for tr in trs:
    if tr.th:
        if tr.th.text == "Author":
            print(tr.td.text)
            break

def getAuthor(booktitle):
    booktitle = booktitle.replace(" ", "_")
    url = "https://en.wikipedia.org/wiki/" + booktitle
    r = requests.get(url)
    s = BeautifulSoup(r.text)
    trs = s.find("table", attrs={"class": "infobox"}).find_all("tr")
    for tr in trs:
        if tr.th:
            if tr.th.text == "Author":
                return(tr.td.text)

getAuthor("The Brothers Karamazov")
getAuthor("Paradise Lost")



## SOLUTION 3 ##

for i in range(85):
    num = i+1
    print(num)
    if num < 10:
        ID = "0" + str(num)
    else:
        ID = str(num)
    r = requests.get("http://avalon.law.yale.edu/18th_century/fed%s.asp" % ID)
    s = BeautifulSoup(r.text)
    ps = s.find_all("p")
    with open("papers/fed%s.txt" % ID, "w") as f:
        for p in ps:
            t = p.text
            t = t.replace(" Return to the Text", "")
            f.write(t + "\n")
    time.sleep(30)


# write authors as well
author = []
r = requests.get("https://www.congress.gov/resources/display/content/The+Federalist+Papers")
s = BeautifulSoup(r.text)
table = s.find("table", {"class": "confluenceTable"})
rows = table.findAll("tr")
for row in rows[1:]:
    author.append(row.findAll("td")[2].text)

with open("authors.csv", "w") as f:
    f.write("author\n")
    for a in author:
        f.write(a + "\n")


