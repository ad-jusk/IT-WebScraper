class Offer:
    def __init__(self, ID, title, salary, company, seniority, requirements, link) -> None:
        self.ID = ID
        self.title = title
        self.salary = salary
        self.company = company
        self.seniority = seniority
        self.requirements = requirements
        self.direct_link = link

    def presentOffer(self) -> None:
        print('#################### ' + str(self.ID) + ' ####################')
        print(self.title)
        print('Seniority: ' + self.seniority)
        print('Salary: ' + self.salary)
        print('Company: ' + self.company)
        print('Requirements:')
        for requirement in self.requirements:
            print('- ' + requirement)
        print('')
