from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from classes.offer import Offer

LINK_CONST = 'https://nofluffjobs.com'

def getOffersInfo(URL, seniority_level) -> list:
    try:
        page = get(URL)
    except RequestException:
        return []
    page_parsed = BeautifulSoup(page.content, 'html.parser')
    offers = page_parsed.find_all('a', class_ = 'posting-list-item')
    result = []
    id = 1
    for offer in offers:
        #DIRECT LINK TO OFFER
        link = prepareLink(offer['href'])
        subpage = get(link)
        subpage_parsed = BeautifulSoup(subpage.content, 'html.parser')

        #SENIORITY
        seniority = findSeniorityLevel(subpage_parsed)

        if(seniority_level not in seniority.lower()):
            continue
        
        #REQUIREMENTS
        requirements = findRequirements(subpage_parsed)

        #INFO FROM MAIN PAGE
        title = parseTitle(str(offer.find('h3').text))
        salary = parseSalary(str(offer.find('span', class_ = 'salary').text))
        company = parseCompany(str(offer.find('span', class_ = 'posting-title__company').text))

        result.append(Offer(id, title, salary, company, seniority, requirements, link))
        id += 1
    return result

def findSeniorityLevel(subpage_parsed : BeautifulSoup) -> str:
    seniority_block = subpage_parsed.find('li', {'id': 'posting-seniority'})
    return str(seniority_block.find('span', class_ = 'mr-10 font-weight-medium').text).strip()

def findRequirements(subpage_parsed : BeautifulSoup) -> list:
    result = []
    req_block = subpage_parsed.find('div', {'id': 'posting-requirements'})

    #sometimes requirements are stored in different tags
    #so far i've seen buttons, links and spans
    requirements_button = req_block.find_all('button')
    requirements_a = req_block.find_all('a')
    requirements_span = req_block.find_all('span')
    
    for requirement in requirements_a:
        result.append(str(requirement.text).strip())
    for requirement in requirements_button:
        result.append(str(requirement.text).strip())
    for requirement in requirements_span:
        result.append(str(requirement.text).strip())
    return result

def prepareLink(link: str) -> str:
    return LINK_CONST + link

def parseTitle(title: str) -> str:
    return title.strip()

def parseSalary(salary: str) -> str:
    temp = salary.split('-')
    if len(temp) == 2:
        return temp[0].strip() + ' - ' + temp[1].replace('PLN', '').strip()
    return temp[0].replace('PLN', '').strip()

def parseCompany(company: str) -> str:
    return company.strip()