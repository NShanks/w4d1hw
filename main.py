import re

with open('files/regex_test.txt') as f:
    data = f.readlines()

pattern = re.compile('([A-Z][a-z]+)\s?([A-Z][a-z]*)?\s?([A-Z][a-z]*)')

for person in data:
    match = pattern.search(person)
    if match:
        if match.group(2):
            print("\n" f"{match.group(1)} {match.group(2)} {match.group(3)}")
        else:
            print("\n" f"{match.group(1)} {match.group(3)}")

# pattern = re.compile('(\w+), ([A-Za-z]+-)*([A-Za-z]+). *\s(@[a-z]+$)')