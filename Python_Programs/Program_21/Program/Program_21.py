# importing regex
import re
# given string which we want  to remove the punctuation marks
given_string = "BTechGeeks, is best: for !Python.?[]() ;"
# using regex
noPunctuationString = re.sub(r'[^\w\s]', '', given_string)

# printing the given string after removing the punctuations
print("printing the given string after removing the punctuations : ")
print(noPunctuationString)