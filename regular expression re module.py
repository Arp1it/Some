import re

mustr = mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiiin'''

# findall, search, split, sub, finditer
# print(r'\n')

# patt = re.compile(r'fass')
# patt = re.compile(r'.')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iin$')
# patt = re.compile(r'a*i*')
# patt = re.compile(r'ai+')
# patt = re.compile(r'ai{3}')
# patt = re.compile(r'(ai){1}')
# patt = re.compile(r'ai{1}|Fax')


# Special Sequences
# patt = re.compile(r'\ATata')
patt = re.compile(r'\bFax')
# patt = re.compile(r'27\b')

# patt = re.compile(r'\d{5}-\d{4}')

matches = patt.finditer(mustr)

for match in matches:
    print(match)
    # print(mustr[448:452])


# Function of re module - 
    # Meta Characters
    # [] A set of characters
    # \ Signals a special sequence (can also be used to escape special characters)
    # . Any character (except newline character)
    # ^ Starts with
    # $ Ends with
    # * Zero or more occurrences
    # + One or more occurrences
    # {} Exactly the specified number of occurrences
    # | Either or
    # () Capture and group


    # Special Sequences
    # \A Returns a match if the specified characters are at the beginning of the string
    # \b Returns a match where the specified characters are at the beginning or at the end of a word r” ain\b.”
    # \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

    # \d Returns a match where the string contains digits (numbers from 0-9)
    # \D Returns a match where the string DOES NOT contain digits
    # \s Returns a match where the string contains a white space character
    # \S Returns a match where the string DOES NOT contain a white space character
    # \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
    # \W Returns a match where the string DOES NOT contain any word characters
    # \Z Returns a match if the specified characters are at the end of the string