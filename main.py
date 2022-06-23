from src.scraper import getOffersInfo

URL = 'https://nofluffjobs.com/pl/lodz?page=1'

def main() -> None:

    #LIST OF OFFERS
    offers = getOffersInfo(URL)
    for offer in offers:
        offer.presentOffer()
if __name__ ==  '__main__':
    main()