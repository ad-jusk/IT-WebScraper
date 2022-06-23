from requests import get
from bs4 import BeautifulSoup
from classes.offer import Offer

def getOffersInfo(URL) -> list:
    page = get(URL)
    page_parsed = BeautifulSoup(page.content, 'html.parser')
    offers = page_parsed.find_all('a', class_ = 'posting-list-item')
    result = []
    for offer in offers:
        title = parseTitle(str(offer.find('h3').text))
        salary = parseSalary(str(offer.find('span', class_ = 'salary').text))
        company = parseCompany(str(offer.find('span', class_ = 'posting-title__company').text))

        #TODO find requirements

        result.append(Offer(title, salary, company, None))
    return result


def parseTitle(title) -> str:
    return title.strip()

def parseSalary(salary) -> str:
    return salary.replace('PLN', '').strip()

def parseCompany(company) -> str:
    return company.strip()