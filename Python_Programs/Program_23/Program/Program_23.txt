# importing counter from collections
from collections import Counter
# given two strings
string1 = "skyis"
string2 = "ssyki"
# converting the both strings to lowercase using lower() function.
string1 = string1.lower()
string2 = string2.lower()
# finding the frequencies of both string using Counter()
freqstring1 = Counter(string1)
freqstring2 = Counter(string2)
# checking if both the strings are equal by comparing the frequencies.
if(freqstring1 == freqstring2):
    print("Both the strings are anagrams")
else:
    print("Both the strings are not anagrams")