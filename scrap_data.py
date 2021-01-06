import requests
from bs4 import BeautifulSoup
import csv
with open(r"C:\Users\Qasim\Desktop\links_htm2\merlinrocketoe\merlinrocketoe.csv", 'r') as file:
    reader = csv.reader(file)## reading file in scv , form
    i=0
    for row in reader:
        for i in range(300):##using a loop to scrap data in html form
            url =row[i]
            print(url)
            print(i)
            r = requests.get(url)
            soup = BeautifulSoup(r.text,'html.parser')
            names = row[i]
            s = names
            s = s.replace("http://sailwave.com/results/merlinrocket/", "")## that is the link from where data scrapped
            q= s.replace(".htm","")
            p= q+".htm"
            print(q)
            f = open(p, "w",encoding='utf-8')
            str_soup = str(soup)
            f.write(str_soup)##htm files save in the code dirctory folder with the name of last link text leaving .htm
            f.close()



















            # check = input("press q to proceed to the next level ")
            #
            # if check == 'q':
            #     i=i+1
            #     continue
            # else:
            #     break
















#
#
# import os.path
# save_path = r'C:\Users\Manan\Desktop\New folder'
# name_of_file = input("abc")
# completeName = os.path.join(save_path, name_of_file+".txt")
# file1 = open(completeName, "w")
# toFile = input("def")
# file1.write(toFile)
# file1.close()
