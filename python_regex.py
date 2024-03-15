""" Regular Experssion """
import re

# RegEx Functions & Metacharacters

# Search the string to see if it starts with "The" and ends with "Spain":
TXT = "The rain in Spain45"
txt_var = re.search("^The.*Spain$", TXT)
if txt_var:
    print("YES! We have a match!")
else:
    print("No match")

# Find all lower case characters alphabetically between "a" and "z":
txt_var = re.findall("[a-z]", TXT)
print(txt_var)

# Find all digit characters:
# str = re.findall("\d", txt)
# print(str)

# Search for a sequence that starts with "Sp", followed by two (any) characters, and an "45":
# txt = "Spain45"
txt_var = re.findall("Sp...45", TXT)
print(str)

# Check if the string starts with 'The':
var = re.findall("^The", TXT)
if var:
    print("Yes, the string starts with 'The'")
else:
    print("No match")


# Check if the string ends with 'Spain45':
var = re.findall("Spain45$", TXT)
if var:
    print("Yes, the string ends with 'Spain45'")
else:
    print("No match")

# Search for a sequence that starts with "T", followed by 0 or more  (any) characters, and an "e":
var = re.findall("T.*e", TXT)
print(var)

# Search for a sequence that starts with "T", followed by 1 or more  (any) characters, and an "e":
var = re.findall("T.+e", TXT)
print(var)

# Search for a sequence that starts with "Sp", followed by 0 or 1  (any) character, and an "45":
var = re.findall("Sp.?45", TXT)
print(var)

# Search for a sequence that starts with "T", followed excactly 2 (any) characters, and an "e":
var = re.findall("T.{1}e", TXT)
print(var)

# Check if the string contains either "rain" or "stays":
var = re.findall("rain|stays", TXT)
print(var)
if var:
    print("Yes, there is at least one match!")
else:
    print("No match")
