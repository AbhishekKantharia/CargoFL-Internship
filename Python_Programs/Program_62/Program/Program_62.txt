# importing re module
import re

# initializing string
test_str = '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.'

# printing original string
print("The original string is : " + str(test_str))

# initializing tag
tag = "b"

# regex to extract required strings
reg_str = "<" + tag + ">(.*?)</" + tag + ">"
res = re.findall(reg_str, test_str)

# printing result
print("The Strings extracted : " + str(res))
