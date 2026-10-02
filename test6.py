class Student:
    def __init__(self, name, grades):
        self.name = name       
        self.grades = grades   

    def grade(self):
        
        if not self.grades:
            return 0  
            
        return sum(self.grades) / len(self.grades)

student1 = Student("Анна", [5, 4, 5, 4])
average = student1.grade()
print(f"Студент: {student1.name}")
print(f"Оценки: {student1.grades}")
print(f"Средний балл: {average}") 


    