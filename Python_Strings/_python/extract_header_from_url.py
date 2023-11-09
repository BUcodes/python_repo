''' 
A program that connects to the website- https://kivihal.me/itp.html- which contains a header, then read only the header.

'''

# import relevant function from library
# Urllib is a package that contains several modules for working with URLs
# urllib.request is the module for opening and reading URLs
# It uses the urlopen function and is able to fetch URLs using a variety of different protocols.
from urllib.request import urlopen 

# Address of the website assigned to variable "url"
url="https://kivihal.me/itp.html"
# fetch the website content using urlopen function
f=urlopen(url)
# This reads the website into variable "content"
content = f.read().decode("utf-8")

# inspect the content of the website
print (content)
# extract and print the header
print (content [content.find('<h1>') + 4 :content.find('</h1>')])
