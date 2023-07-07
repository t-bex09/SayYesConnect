

class User:
    def __init__(self,first_name,last_name,age,gender,college,major,degree,occupation,company,username,password,struggles) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.college = college
        self.major = major
        self.degree = degree
        self.occupation = occupation
        self.company = company
        self.username = username
        self.password = password
        self.struggles = struggles
    def __str__(self) -> str:
        return f"User: {self.first_name} {self.last_name}\nOccupation: {self.occupation}\nCompany: {self.company}"
    def bio(self):
        info = f"First Name: {self.first_name}\n"
        info += f"Last Name: {self.last_name}\n"
        info += f"Age: {self.age}\n"
        info += f"Gender: {self.gender}\n"
        info += f"College: {self.college}\n"
        info += f"Major: {self.major}\n"
        info += f"Degree: {self.degree}\n"
        info += f"Occupation: {self.occupation}\n"
        info += f"Company: {self.company}\n"
        info += f"Struggles: {self.struggles}\n"
        return info