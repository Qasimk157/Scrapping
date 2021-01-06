import requests
from bs4 import BeautifulSoup
r = requests.get("http://sailwave.com/results/WembleySC/RS200")
c=r.content
# print(c)
soup=BeautifulSoup(c,"html.parser")
#print(soup)## to print just that link data
# total = soup.find("p", class_=False, id=False)## to scrape only paragraph(p)
# onee=total.find("a",class_=False, id=False)## to scrape the the a links complete
for link in soup.find_all('a'):## to scrape only links from html page
    resultt=link.get('href')
    print(resultt)

    f=open("C:/Users/Qasim/Desktop/data_in_html/all_folders_data/WembleySC/Laser/2012.csv", "a")## to save all links or other thing in a file
    f.write(resultt)## write that file reuslut in a file
    f.close()
