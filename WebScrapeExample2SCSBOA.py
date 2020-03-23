import requests
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

print(object)
#nPfds = str(pdfs)
print('\n')
#print(aDict)
addressString = aDict.__getitem__("id0")
nAddressString = str(addressString)
index = nAddressString.find('href')
endIndex = nAddressString.find('.pdf"')
print(nAddressString)

print(type(nAddressString))
startPoint = index
endPoint = endIndex
finAddressString = ''
finAddressString = (nAddressString[startPoint+6 : endPoint+4])

print(startPoint)
print(endPoint)
#print(index)
#print(endIndex)
#print(addressString[startPoint:endPoint])


#while index < len(addressString):
 #   finAddressString += addressString.split()
  #  index = index + 1

#print(type(pdfs))
#print(pdfs)
#ad = pdfs.getItem("id")

print("This is a test")
print(finAddressString)




#Figure out how to take out and reformat the hyper link
#psuedo code traverse thru the item until the text displays the "href and from there we can store the https link"
#for item in pdfs:
    #w = item.find_all("href")[0]

#print(w)