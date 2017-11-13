import requests
from bs4 import BeautifulSoup
import json
#creating a list to append the elements
emp_details = []
for i in range(9,10):
    letter = chr(i+65)
    url = "https://www.groupon.com/browse/fort-worth?lat=32.7254&lng=-97.3208&address=Fort+Worth&query=a&locale=en_US"
    print(url)
    # Beautiful soup way
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    people = soup.findAll('a',{'class',"ls-gcx-flyout-link"})
    for person in people:
        subperson = person.findNext('div',{'class':'ls-gcx-flyout-item-content-child-label ls-clearfix'})
#fetching and printing the depts
        dept = person.findNext('div').text
        print(dept)
        person_dict = {}
        person_dict['dept'] = dept.strip()
#appending all elemets to list
        emp_details.append(person_dict)
        #printing all elements in list
#print(emp_details)
with open('output.json', 'w') as f:                             # write data into json file
    output=json.dumps(emp_details,indent=1)
    f.write(output)     
#print(emp_details)
