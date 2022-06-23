class Offer:
    def __init__(self, title, salary, company, requirements) -> None:
        self.title = title
        self.salary = salary
        self.company = company
        self.requirements = requirements
    
    def presentOffer(self) -> None:
        print(self.title, self.salary, self.company)
