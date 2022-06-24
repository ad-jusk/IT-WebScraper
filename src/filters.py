SENIORITY_LEVELS = ['trainee', 'junior', 'mid', 'senior', 'expert']
CITIES = {
    'warsaw': 'warszawa',
    'lodz': 'lodz',
    'gdansk': 'gdansk',
    'cracow': 'krakow',
    'wroclaw': 'wroclaw'
}

def welcomeUser() -> None:
    print('Hello, this program will quickly find IT job offers that might interest you.')
    print("Let's get started!")

def askForSeniority() -> str:
    level = None
    while True:
        try:
            level = int(input('Please rate your seniority level from 1 to 5: '))
            if level < 1 or level > 5:
                print('Please enter a correct integer.')
            else:
                return SENIORITY_LEVELS[level - 1]
        except ValueError:
            print('Please enter a correct integer.')

def askForCity() -> str:
    city = ''
    while True:
        city = str(input('Please enter your city: '))
        if city.lower() in CITIES:
            print()
            return CITIES[city]
        else:
            print('Sorry, this city is not supported.')


