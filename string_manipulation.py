

### FIRST, ordinary string manipulation ###

with open('declaration.txt') as f:
    declaration = f.read()


# Splitting a string into a list of strings at every new-line (usually encoded as "\n")
lines = declaration.splitlines()
lines[0]  # first line
lines[-1]  # last line

# Putting a list of strings together into a single string
s = "\n".join(lines)
s == declaration


# Count the number of occurrences of a substring within a larger string
declaration.count("other")
# is this telling us how many times the word "other" shows up?
# it would also count words like "bother" - could delimit with spaces...
declaration.count(" other ")
# but there might be a punctuation mark immediately before or after...


# Finding the first occurrence of a substring within larger string
index = declaration.find("Quartering")
index
declaration[(index-100):(index+100)]

# Replacing all occurrences of a substring within a larger string
new_declaration = declaration.replace("united", "divided")
new_declaration[:100]
# if you only want to replace the first occurrence in the string: declaration.replace("united", "divided", 1)


# There are many other str functions that can be found in the Python
# documentation and tutorials online.








# EXERCISE 1: Create a string of the declaration of independence that has all
#             occurrences of the word "we" (or "We") in the last paragraph
#             replaced with all-caps "WE".









################# REGULAR EXPRESSIONS ###############


# The "find" and the "replace" functions work well when you have a
# specific substring in mind. But what if you wanted to, for example,
# find every word that begins with a capital letter?
# Many tasks that are difficult or impossible with the ordinary string functions become
# quite easy if you have enough proficiency with "regular expressions".


s = "What do you think you'll do this year?"


import re

# Find every instance of "you" - nothing special going on here
re.findall("you", s)

# Now let's start to see how regular expressions provide more flexibility.
# The following command finds all substrings that have a y followed by
# another letter
re.findall("y\w", s)
# The "\w" matches any word character (upper- or lower-case letter)

# how about y followed by any number of letters.
re.findall("y\w*", s)
# while the "*" means any number of occurrences of such.

# add apostrophe to the set of matched symbols
re.findall("y[\w']*", s)


re.findall("y\w*", "The very same things I do every year.")
re.findall("y\w+", "The very same things I do every year.")
# The "+" means at least one occurrence.

# Now let's find every word that has at least one "y".
# That means any number of word characters,
# followed by a y, followed by any number of word characters.
re.findall("[\w']*y[\w']*", "The very same things you've seen me do every year.")


# words that start and end with "d"

re.findall("b\w*b", "My friend Bob is a blob.")

# ignoring case

re.findall("b\w*b", "My friend Bob is a blob.", re.IGNORECASE)


# back to the Declaration...

# Let's find all the words that start with a capital letter.
re.findall("[A-Z]\w*", declaration)

# Let's reconsider occurrences of the word "other" (possibly capitalized)
re.findall("[Oo]ther", declaration)
# Upon closer inspection, one of these matches is actually "another"
re.findall("\w*[Oo]ther\w*", declaration)
# We can make sure that "other" is at the beginning of the word.
re.findall("\\b[Oo]ther\w*", declaration)
# The "\\b" matches a word boundary. https://developmentality.wordpress.com/2011/09/22/python-gotcha-word-boundaries-in-regular-expressions/
# But this regular expression would still match, for example, "otherwise"
# let's only match "other" or "others"
re.findall("\\b[Oo]thers?", declaration)
# The "?" means either zero or one occurrences of the preceding "s".



# A more practical example - finding mathematical expressions in latex...

tex = "Let $x$ and $y$ be vectors."

# the dot character "." matches anything except a newline

re.findall("$.*$", tex)

# dollar signs among the "special characters" in re - need to "escape" them

re.findall("\$.*\$", tex)

# too greedy! add a "?" to end the match at the first opportunity

re.findall("\$.*?\$", tex)

# we can use parentheses to "capture" the inside without the dollar sign delimiters

re.findall("\$(.*?)\$", tex)


# "match" objects

match = re.search("\$(.*?)\$", tex)
match.group() # the whole matched group
match.group(1) # first captured group

# to get "match" objects through the whole string
# rather than stopping at the first match, use "finditer":

matches = re.finditer("\$(.*?)\$", tex)
for match in matches:
    print(match.group(1))



## Replacing text via regex: the SUBstitution function ###

# in simple cases, you don't need the replacement to depend on the matched text

re.sub("\$.*?\$", "MATH", tex)

# what if we need to switch the dollar sign delimiters to square brackets

re.sub("\$(.*?)\$", r"[\1]", tex)

# the "\1" means the first captured group (there's only one capture in this regex anyway)
# the "r" in front creates a "raw string"
# - it's a bit more convenient for this kind of regex replacement and some other scenarios

# Now let's instead modify what's inside the delimiters.
# Sometimes you need to write a function that you want to perform on
# each of the match items

def uppercase(match):
    return "$"+match.group(1).upper()+"$"

re.sub("\$(.*?)\$", uppercase, tex)



# EXERCISE 2: Write a function concatenateTxtFiles
#             that takes a directory path as its first argument
#             and a file path as its second argument. It should read in
#             all of the .txt files in the directory provided, and put their
#             text together (separated by newline characters "\n")
#             into a new file, saved as the file path provided.







#### MORE "REGEX" PRACTICE ####





# Find all occurrences of States OR Colonies
re.findall("States\\b|Colonies\\b", declaration)
# The "|" means OR.

# Let's find all the paragraphs that start with "He has"
re.findall("He has .*", declaration)
# The "." matches everything that isn't a newline character
# This isn't ideal because it could match "He has" starting anywhere
# within a paragraph. To make sure we're starting at the beginning:
re.findall("^He has .*", declaration, re.MULTILINE)
# The "^" matches the beginning of the string, and
# with re.MULTILINE, it also matches the beginning of any line.

# Similarly, "$" matches the end of the string (or of any line when MULTILINE is specified).
# What's the paragraph that ends with the word "Hands" ? ...
re.findall("^.* Hands\.$", declaration, re.MULTILINE)
# Notice that "\." was needed to match the period "." at the end.
# The backslash "escapes" the ordinary treatment of "." in a regular expression.

# You can use parentheses to indicate the part(s) of the regular expression
# that you want to "keep".
re.findall("^He has (.*)", declaration, re.MULTILINE)
re.findall("^He has (\w+) .*", declaration, re.MULTILINE)

# another example of "greedy" versus "lazy" matching
# greedy
re.findall("<li>.*</li>", "<li>item 1</li><li>item 2</li>")
# lazy
re.findall("<li>.*?</li>", "<li>item 1</li><li>item 2</li>")

# You can also use regular expressions to identify substrings that you
# want to replace. The "re.sub()" function from the re module does the trick.
# Let's replace every "We" and "we" with "WE".
new_declaration = re.sub("\\b[Ww]e\\b", "WE", declaration)
new_declaration[-100:]


# You can keep track of specific portions of a matched substring using "re.search()"
lines = declaration.splitlines()
s = lines[-1]
s
r = re.search("we mutually pledge to each other our (.*), our (.*) and our (.*)\.", s)
r.group()
r.group(1)
r.group(2)
r.group(3)
r.groups()

# the search object can also be used as a conditional
# indicating whether or not a match was found within the string
if r:
    print("match found")

# Regular expressions are incredibly powerful, but they can be challenging to use.
# Much more documentation is available on the web.
# https://www.w3schools.com/python/python_regex.asp
# https://www.tutorialspoint.com/python/python_reg_expressions.htm
# https://docs.python.org/3/library/re.html


# EXERCISE 3: Create a string of the declaration of independence in which
#             the word after "He has" is written in all capitals in each of the
#             "He has"-paragraphs.














############################## SOLUTIONS #####################################



## SOLUTION 1 ##

lines = new_declaration.splitlines()
s = lines[-1]
s = s.replace(" We ", " WE ")
s = s.replace(" we ", " WE ")
lines[-1] = s
"\n".join(lines)

# note: this only works if "we" doesn't have a punctuation mark immediately before or after it.
#       - a simpler and more robust solution would involve regular expressions



## SOLUTION 2 ##

from pathlib import Path

def concatenateTxtFiles(dir_path="", file_path="concatenated.txt"):
    full = "\n".join([file.read_text() for file in Path(dir_path).glob("*.txt")])
    Path(file_path).write_text(full)

concatenateTxtFiles()



## SOLUTION 3 ##

def uppercase(match):
    return "He has " + match.group(1).upper()  + " " + match.group(2)

s = re.sub("^He has (\w+) (.*)", uppercase, declaration, flags=re.MULTILINE)
           
# check:
re.findall("^He has .*", s, re.MULTILINE)
