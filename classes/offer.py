from colorama import Fore, init

init(autoreset=True)

class Offer:
    def __init__(self, ID, title, salary, company, seniority, requirements, link) -> None:
        self.ID = ID
        self.title = title
        self.salary = salary
        self.company = company
        self.seniority = seniority
        self.requirements = requirements
        self.link = link

    def presentOffer(self) -> None:
        print(Fore.YELLOW + '#################### ' + str(self.ID) + ' ####################')
        print(Fore.WHITE + self.title)
        print(Fore.GREEN + 'Seniority: ' + self.seniority)
        print(Fore.CYAN + 'Salary: ' + self.salary)
        print(Fore.LIGHTMAGENTA_EX + 'Company: ' + self.company)
        print(Fore.LIGHTRED_EX + 'Requirements:')
        for requirement in self.requirements:
            print(Fore.LIGHTRED_EX + '- ' + requirement)
        print('')
    
    def printLink(self) -> None:
        print(Fore.YELLOW  + 'Here is your direct link --> ' + self.link)
