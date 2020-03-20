import requests
from bs4 import BeautifulSoup

r= requests.get("https://www.scsboa.org/field-recaps/)")
c = r.content

parse = BeautifulSoup(c, "html.parser")

x = 10
i = 0
while i < x:
    object = "table_55_row_" + str(i)
    pdfs = parse.find("tr",{"id":object})
    i=i + 1
    print(pdfs)

print(object)

#for item in pdfs:
    #w = item.find_all("href")[0]

#print(w)