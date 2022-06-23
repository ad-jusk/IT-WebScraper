from src.scrapper import getOffersInfo

URL = 'https://nofluffjobs.com/pl/lodz?page=1'

def main() -> None:

    #LIST OF OFFERS
    offers = getOffersInfo(URL)

if __name__ ==  '__main__':
    main()