# given string
given_string = "          B  t      echG   eeks               "
# printing the original string before removing white spaces
print("Before removing white spaces given string=", given_string)
# removing white spaces from the given string
given_string = "".join(given_string.split())
# printing the original string before after white spaces
print("after removing white spaces given string=", given_string)