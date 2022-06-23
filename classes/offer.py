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
        print(self.title, self.salary, self.company)
        print(self.requirements)
        print(self.seniority)
