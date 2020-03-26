import requests
import tweepy
from bs4 import BeautifulSoup

r= requests.get("https://www.scsboa.org/field-recaps/)")
c = r.content

parse = BeautifulSoup(c, "html.parser")

x = 10
i =  0

while i < x:
    object = "table_55_row_" + str(i)
    id = "id" + str(i)
    pdfs = parse.find("tr",{"id":object})

    if i == 0:
        aDict = {id: pdfs}
    else:
        aDict.update({id : pdfs})
    i=i + 1
    #print(pdfs)

#print(object)
#nPfds = str(pdfs)
#print('\n')
#print(aDict)
addressString = aDict.__getitem__("id0")
nAddressString = str(addressString)
index = nAddressString.find('href')
endIndex = nAddressString.find('.pdf"')
#print(nAddressString)

#print(type(nAddressString))
startPoint = index
endPoint = endIndex
finAddressString = ''
finAddressString = (nAddressString[startPoint+6 : endPoint+4])

#print(startPoint)
#print(endPoint)
print(finAddressString)

# Code to Authenticate to Twiiter
auth = tweepy.OAuthHandler("Your Handler Key",
"Your secret Key")

auth.set_access_token("Access Token",
"Secret Access Token")

# Create API object
api = tweepy.API(auth)

# Create a tweet
try:
    api.verify_credentials()
    print("Auth OK")
except:
    print("Error during auth")


try:
    api.update_status("Test Results: " + finAddressString)
    print("Update succesful")
    #print("test")
   #Print my followers
   # print(api.followers(api.me()))
except:
    print("Update fail")
