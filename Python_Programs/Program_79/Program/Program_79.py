# Import requests, BeautifulSoup, json, random and 
# os.path modules using the import keyword
import requests
from bs4 import BeautifulSoup as bs
import json
import random
import os.path

# Give the website URL of instagram and store it in a variable
instagramUrl='https://www.instagram.com'

# Give the insta username as user input using the input() function and 
# store it in another variable
instagramUsername= input("Enter some random instagram username =")

# Get the response using the requests module get() function
response = requests.get(f"{instagramUrl}/{instagramUsername}/")

# Check if the response is success(here ok attribute specifies request is success)
if response.ok:
    # Get the text of the response using the text attribute and save in a variable
    html=response.text
    bs_html=bs(html, features="lxml")
    bs_html=bs_html.text
    index=bs_html.find('profile_pic_url_hd')+21
    remaining_text=bs_html[index:]
    remaining_text_index=remaining_text.find('requested_by_viewer')-3
    string_url=remaining_text[:remaining_text_index].replace("\\u0026","&")

    print(string_url, "\n \n downloading..........")

while True:
    # Create a random file name to store using the random function and save it in a variable (here .jpg specifies image extension)
    filename='pic'+str(random.randint(1, 100000))+'.jpg'
    # Check if the above file exists in our system using the isfile() function
    file_exists = os.path.isfile(filename)
    # If the file doesn't exists then we can save with the above filename
    if not file_exists:
        # Open the above file in the write binary mode
        with open(filename, 'wb+') as handle:
            # Get the response from the string url using the requests module get() function
            response = requests.get(string_url, stream=True)
            # If we get in any error then we print the error
            if not response.ok:
                print(response)
            # Else we write the image to the file using the write() function
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
    else:
        continue
    break
print("The instagram profile picture is download succesfully!!")