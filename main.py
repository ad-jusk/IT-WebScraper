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

    action = 0
    while True:
        print('Searching for offers...')
        offers = getOffersInfo(setURL(city), seniority)
        if len(offers) == 0:
            print("Sorry, 'didn't find any matching offers.")
        else:
            for offer in offers:
                offer.presentOffer()
        
        while True:
            try:
                action = int(input('!! Enter offer number if you want a direct link !! (or 0 to continue) '))
                if action >= 1 and action <= len(offers):
                    print('Here is your direct link --> ' + offers[action - 1].getLink())
                elif action == 0:
                    break
                else:
                    print('Please enter a correct offer number or 0.')
            except ValueError:
                print('Please enter a correct offer number or 0.')
        
        print('Enter 1 to keep searching')
        print('Enter 2 to change filters')
        print('Enter 3 quit')

        while True:
            try:
                action = int(input('Your choice: '))
                if action == 1:
                    break
                elif action == 2:
                    seniority = askForSeniority()
                    city = askForCity()
                    break;
                elif action == 3:
                    return
                else:
                    print('Please enter a correct offer number or 0.')
            except ValueError:
                print('Please enter a correct offer number or 0.')
        
if __name__ ==  '__main__':
    main()