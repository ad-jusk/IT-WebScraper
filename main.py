from src.scraper import getOffersInfo
from src.filters import welcomeUser, askForCity, askForSeniority


URL = 'https://nofluffjobs.com/pl'
current_page = 0

def setURL(city) -> str:
    global current_page
    current_page += 1
    return URL + '/' + city + '?page=' + str(current_page)

def main() -> None:
    
    welcomeUser()
    seniority = askForSeniority()
    city = askForCity()

    #LIST OF OFFERS
    offers = getOffersInfo(setURL(city), seniority)
    for offer in offers:
        offer.presentOffer()

if __name__ ==  '__main__':
    main()