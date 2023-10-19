from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from classes.offer import Offer

URL_CONST = 'https://nofluffjobs.com'
OFFER_ELEMENT_CLASS = 'posting-list-item'
SALARY_ELEMENT_CLASS = 'salary'
TITLE_ELEMENT_CLASS = 'posting-title__position'
COMPANY_ELEMENT_CLASS = 'posting-title__company'
REQUIREMENTS_ELEMENT_ID = 'posting-requirements'
SENIORITY_ELEMENT_ID = 'posting-seniority'

def get_offers_info(URL, seniority_level) -> list[Offer]:
    try:
        page = get(URL)
    except RequestException:
        raise Exception('Error during get request for URL = ' + URL)
    
    page_parsed = BeautifulSoup(page.content, 'html.parser')
    offers = page_parsed.find_all('a', class_ = OFFER_ELEMENT_CLASS)

    if len(offers) == 0:
        raise Exception("No offers found on page - should never happen")

    result = []
    offer_id = 1

    for offer in offers:
        offer_link = prepare_link(offer['href'])
        try:
            subpage = get(offer_link)
        except RequestException:
            raise Exception('Error during get request for URL = ' + URL)
        
        subpage_parsed = BeautifulSoup(subpage.content, 'html.parser')

        seniority = find_seniority_level(subpage_parsed)

        if seniority_level not in seniority.lower():
            continue
        
        requirements = find_requirements(subpage_parsed)

        title_h3 = offer.find('h3', class_ = TITLE_ELEMENT_CLASS)
        salary_span = offer.find('span', class_ = SALARY_ELEMENT_CLASS)
        company_span = offer.find('span', class_ = COMPANY_ELEMENT_CLASS)

        title = parse_title(str(title_h3.text)) if title_h3 is not None else '[Title not found]'
        salary = parse_salary(str(salary_span.text)) if salary_span is not None else '[Salary not found]'
        company = parse_company(str(company_span.text)) if company_span is not None else '[Company not found]'

        result.append(Offer(offer_id, title, salary, company, seniority, requirements, offer_link))
        offer_id += 1

    return result

def find_seniority_level(subpage_parsed : BeautifulSoup) -> str:
    seniority_block = subpage_parsed.find('li', {'id': SENIORITY_ELEMENT_ID})
    if seniority_block is None:
        return ''
    seniority_span = seniority_block.find('span')
    if seniority_span is None:
        return ''
    return str(seniority_span.text).strip()

def find_requirements(subpage_parsed : BeautifulSoup) -> list:
    result = []
    req_block = subpage_parsed.find('div', {'id': REQUIREMENTS_ELEMENT_ID})
    if req_block is None:
        print("No requirements found - " + REQUIREMENTS_ELEMENT_ID + " identifier might not be valid")
        return result

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

def prepare_link(link: str) -> str:
    return URL_CONST + link

def parse_title(title: str) -> str:
    return title.strip()

def parse_salary(salary: str) -> str:
    temp = salary.split('-')
    if len(temp) == 2:
        return temp[0].strip() + ' - ' + temp[1].replace('PLN', '').strip()
    return temp[0].replace('PLN', '').strip()

def parse_company(company: str) -> str:
    return company.strip()