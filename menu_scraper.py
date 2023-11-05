import requests
from bs4 import BeautifulSoup as soup
from nutrition_scraper import get_nutrition
import json
import time

start_time = time.time()

URL_BREAKFAST_LIVI = "http://menuportal23.dining.rutgers.edu/FoodPro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=03&locationName=Livingston+Dining+Commons&naFlag=1"
URL_LUNCH_LIVI = "http://menuportal23.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=03&locationName=Livingston+Dining+Commons&dtdate=11/3/2023&mealName=Lunch&sName=Rutgers+University+Dining"
URL_DINNER_LIVI = "http://menuportal23.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=03&locationName=Livingston+Dining+Commons&dtdate=11/3/2023&mealName=Dinner&sName=Rutgers+University+Dining"

URL_BREAKFAST_BUSCH = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=04&locationName=Busch+Dining+Hall&dtdate=11/6/2023&mealName=Breakfast&sName=Rutgers+University+Dining"
URL_LUNCH_BUSCH = "http://menuportal23.dining.rutgers.edu/foodpro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=04&locationName=Busch+Dining+Hall&naFlag=1"
URL_DINNER_BUSCH = "http://menuportal23.dining.rutgers.edu/foodpro/pickmenu.asp?locationNum=04&locationName=Busch+Dining+Hall&dtdate=11/4/2023&mealName=Dinner&sName=Rutgers+University+Dining"

URL_BREAKFAST_CD = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=05&locationName=Neilson+Dining+Hall&dtdate=11/6/2023&mealName=Breakfast&sName=Rutgers+University+Dining"
URL_LUNCH_CD = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=05&locationName=Neilson+Dining+Hall&naFlag=1"
URL_DINNER_CD = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=05&locationName=Neilson+Dining+Hall&dtdate=11/4/2023&mealName=Dinner&sName=Rutgers+University+Dining"

URL_BREAKFAST_AT = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=13&locationName=The+Atrium&naFlag=1"
URL_LUNCH_AT = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=13&locationName=The+Atrium&dtdate=11/4/2023&mealName=Lunch+Entree&sName=Rutgers+University+Dining"
URL_DINNER_AT = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=13&locationName=The+Atrium&dtdate=11/4/2023&mealName=Dinner+Entree&sName=Rutgers+University+Dining"

lis = [URL_BREAKFAST_LIVI, URL_LUNCH_LIVI, URL_DINNER_LIVI, URL_BREAKFAST_BUSCH, URL_LUNCH_BUSCH,
       URL_DINNER_BUSCH, URL_BREAKFAST_CD, URL_LUNCH_CD, URL_DINNER_CD, URL_BREAKFAST_AT, URL_LUNCH_AT, URL_DINNER_AT]

for index, i in enumerate(lis):
    req = requests.get(i)
    dic = {}
    bs = soup(req.content, 'html5lib')
    form = bs.find('div', attrs={'class': 'menuBox'})

    for name, nutrition in zip(form.find_all('div', attrs={'class': 'col-1'}), form.find_all('div', attrs={'class': 'col-3'})):
        # print(name.text)

        # breakfast[name.text]
        nutri_link = nutrition.a['href']
        # res = get_nutrition(nutri_link)
        nutri_link = 'http://menuportal23.dining.rutgers.edu/FoodPro/'+nutri_link
        # print(nutri_link)
        try:
            res = get_nutrition(nutri_link)
            # print(res)
            dic[name.get_text(strip=True)] = res
        except:
            print(f'did not get info on: {name.get_text(strip=True)}')

    file_name = 'data'+str(index)+'.json'

    w = open(file_name, "w")
    jsonfile = json.dumps(dic)
    w.write(jsonfile)
    w.close()

# req = requests.get(URL_BREAKFAST)

# req2 = requests.get(URL_LUNCH)

# req3 = requests.get(URL_DINNER)

# # bs = soup(req.content, 'html5lib')
# # print(bs.prettify())

# breakfast = {}
# lunch = {}
# dinner = {}

# bs = soup(req.content, 'html5lib')

# form = bs.find('div', attrs={'class': 'menuBox'})

# for name, nutrition in zip(form.find_all('div', attrs={'class': 'col-1'}), form.find_all('div', attrs={'class': 'col-3'})):
#     # print(name.text)

#     # breakfast[name.text]
#     nutri_link = nutrition.a['href']
#     # res = get_nutrition(nutri_link)
#     nutri_link = 'http://menuportal23.dining.rutgers.edu/FoodPro/'+nutri_link
#     # print(nutri_link)
#     try:
#         res = get_nutrition(nutri_link)
#         # print(res)
#         breakfast[name.get_text(strip=True)] = res
#     except:
#         print(f'did not get info on: {name.get_text(strip=True)}')

# # print(breakfast)

# w = open("breakfast.json", "w")
# jsonfile = json.dumps(breakfast)
# w.write(jsonfile)
# w.close()

# bs = soup(req2.content, 'html5lib')

# form = bs.find('div', attrs={'class': 'menuBox'})

# for name, nutrition in zip(form.find_all('div', attrs={'class': 'col-1'}), form.find_all('div', attrs={'class': 'col-3'})):
#     # print(name.text)

#     # breakfast[name.text]
#     nutri_link = nutrition.a['href']
#     # print(name)
#     # res = get_nutrition(nutri_link)
#     nutri_link = 'http://menuportal23.dining.rutgers.edu/FoodPro/'+nutri_link
#     # print(nutri_link)
#     try:
#         res = get_nutrition(nutri_link)
#         # print(res)
#         lunch[name.get_text(strip=True)] = res
#     except:
#         print(f'did not get info on: {name.get_text(strip=True)}')

# # print(breakfast)

# w = open("lunch.json", "w")
# jsonfile = json.dumps(lunch)
# w.write(jsonfile)
# w.close()

# bs = soup(req3.content, 'html5lib')

# form = bs.find('div', attrs={'class': 'menuBox'})

# for name, nutrition in zip(form.find_all('div', attrs={'class': 'col-1'}), form.find_all('div', attrs={'class': 'col-3'})):
#     # print(name.text)

#     # breakfast[name.text]
#     nutri_link = nutrition.a['href']
#     # res = get_nutrition(nutri_link)
#     nutri_link = 'http://menuportal23.dining.rutgers.edu/FoodPro/'+nutri_link
#     # print(nutri_link)
#     try:
#         res = get_nutrition(nutri_link)
#         # print(res)
#         dinner[name.get_text(strip=True)] = res
#     except:
#         print(f'did not get info on: {name.get_text(strip=True)}')

# # print(breakfast)

# w = open("dinner.json", "w")
# jsonfile = json.dumps(dinner)
# w.write(jsonfile)
# w.close()

end_time = time.time()
execution_time = start_time - end_time
print("Execution time:", execution_time)
