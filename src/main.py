from requests import get
from bs4 import BeautifulSoup

URL = 'https://nofluffjobs.com/pl/lodz?page=1'

def getOffersTitleAndSalary(page_parsed):
    offers = page_parsed.find_all('a', class_ = 'posting-list-item')
    result = {}
    for offer in offers:
        title = parseTitle(str(offer.find('h3').text))
        salary = parseSalary(str(offer.find('span', class_ = 'salary').text))
        result[title] = salary
    return result

def parseTitle(title):
    return title.strip()

def parseSalary(salary):
    return salary.replace('PLN', '').strip()

def main():
    page = get(URL)
    page_parsed = BeautifulSoup(page.content, 'html.parser')

    #DICTIONARY WITH TITLES AND SALARIES
    offers = getOffersTitleAndSalary(page_parsed)

if __name__ ==  '__main__':
    main()