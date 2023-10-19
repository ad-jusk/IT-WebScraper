from classes.offer import Offer
from src.scraper import get_offers_info
from src.filters import welcome_user, ask_for_city, ask_for_seniority

URL = 'https://nofluffjobs.com/pl'
current_page = 0

def set_URL(city: str) -> str:
    global current_page
    current_page += 1
    return URL + '/' + city + '?page=' + str(current_page)

def main() -> None:
    global current_page
    action = 0
    welcome_user()
    seniority = ask_for_seniority()
    city = ask_for_city()

    while True:
        print('Searching for offers...\n')
        try:
            offers: list[Offer] = get_offers_info(set_URL(city), seniority)
        except Exception as e:
            print(e)
            continue
        if len(offers) == 0:
            print("Sorry, didn't find any matching offers.\n")
        else:
            for offer in offers:
                offer.present_offer()
            while True:
                try:
                    print('## Enter offer number if you want a direct link (or 0 to continue) ##')
                    action = int(input('Your choice: '))
                    if action >= 1 and action <= len(offers):
                        offers[action - 1].print_link()
                    elif action == 0:
                        print()
                        break
                    else:
                        print('Please enter a correct offer number or 0.')
                except ValueError:
                    print('Please enter a correct offer number or 0.')
        
        print('Enter 1 to keep searching')
        print('Enter 2 to change filters')
        print('Enter 3 to quit searching')

        while True:
            try:
                action = int(input('Your choice: '))
                if action == 1:
                    print()
                    break
                elif action == 2:
                    seniority = ask_for_seniority()
                    city = ask_for_city()
                    current_page = 0
                    break
                elif action == 3:
                    return
                else:
                    print('Please enter a correct integer.')
            except ValueError:
                print('Please enter a correct integer.')
        
if __name__ ==  '__main__':
    main()