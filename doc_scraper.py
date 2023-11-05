import requests
from bs4 import BeautifulSoup as soup
from nutrition_scraper import get_nutrition
import json
import mysql.connector as sqltor


def doc_scraper(id):
    mycon = sqltor.connect(host="na05-sql.pebblehost.com", user="customer_586593_ruontime",
                           passwd="TmzuYi1sOBxJ!qdy9d7j", database="customer_586593_ruontime")
    if mycon.is_connected():
        print('Succesfully Connected to MySql')
    cursor = mycon.cursor()
    command = "SELECT health FROM menu WHERE id="+str(id)+";"
    cursor.execute(command)
    print(command)
    condition = cursor.fetchone()
    print(condition)

    # discordtoken = "MTE3MDQwNzUzOTQwMjM1NDgwMA.GMTV-Y.6BAtXH8KoLmQIKW_nPmjnfxzJ-YKt5VaJ3JUzU"

    # URL = "https://www.zocdoc.com/search?address=08901&after_5pm=false&before_10am=false&day_filter=AnyDay&dr_specialty=153&filters=%7B%7D&fit_questionnaire_type=PCP&gender=-1&insurance_carrier=323&insurance_plan=2364&language=-1&offset=0&reason_visit=3849&searchOriginator=SearchBar&searchQueryGuid=&searchType=specialty&search_query=Primary+Care+Physician+%28PCP%29&sees_children=false&sort_type=Default&visitType=inPersonAndVirtualVisits"
    # URL = "https://umg.rwjms.rutgers.edu/find_provider.php"
    URL = "https://umg.rwjms.rutgers.edu/search_results.php?chosen_insurance=&chosen_insurance_label=&chosen_specialty=&chosen_symptoms_or_condition=" + \
        str(condition)+"&typed_specialty=&typed_symptoms_or_condition=&view="
    req = requests.get(URL)

    bs = soup(req.content, 'html5lib')

    table = bs.find('div', attrs={'id': 'myTable'})

    # print(bs.prettify())


doc_scraper(390451900677619722)
# breakfast = {}390451900677619722
# lunch = {}
# dinner = {}

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
# json = json.dumps(breakfast)
# w.write(json)
# w.close()
