

class User:
    def __init__(self,first_name,last_name,age,gender,college,major,degree,occupation,company) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.college = college
        self.major = major
        self.degree = degree
        self.occupation = occupation
        self.company = company
    
    def __str__(self) -> str:
        return f"User: {self.first_name} {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nCollege: {self.college}\nMajor: {self.major}\nDegree: {self.degree}\nOccupation: {self.occupation}\nCompany: {self.company}"
