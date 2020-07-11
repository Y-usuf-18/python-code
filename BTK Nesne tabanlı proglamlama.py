# # class Person:
# #
# #
# #     def __init__(self,name,year):
# #
# #
# #
# #         self.name = name
# #         self.year = year
# #         print("init metodu çalıstı")
# #
# #     def calculateAge(self):
# #             return 2020 - self.year
# #
# # p1 = Person("Ali",1999)
# # p2 = Person("Can",1892)
# #
# #
# #
# #
# #
# # print(f"Name : {p1.name}  Yaşım : {p1.calculateAge()}  ")
# # print(f"Name : {p2.name} Yaşım : {p2.calculateAge()} ")
#
# # class circle:
# #     pi = 3.14
# #
# #     def __init__(self,yaricap = 1):
# #         self.yaricap = yaricap
# #
# #     def CevreHesapla(self):
# #         return 2 * self.pi * self.yaricap
# #
# #     def AlanHesapla(self):
# #         return self.pi * (self.yaricap ** 2)
# #
# #
# # c1 = circle()
# # c2 = circle(5)
# #
# # print(f"alan :{c1.AlanHesapla()} Çevre:{c1.CevreHesapla()}")
# # print(f"alan :{c2.AlanHesapla()} Çevre:{c2.CevreHesapla()}")
#
# class Person():
#     def __init__(self,name,year):
#         self.name = name
#         self.year = year
#
#
#         print("Person created")
#
#
# class Student(Person):
#
#
#     # def __init__(self,name,year):
# #         Person.__init__(self,name,year)
# #         print("Student created")
# #     def sayHello(self):
# #         print("Hello There")
# #
# #
# #
# #
# #
# # p1 = Person("Ada",1990)
# # s1 = Student("Ada",1990)
# # s1.sayHello()
# # print(f"Benim adım {p1.name}")
# # print(f"Benim adım {s1.name}, I m was born in {s1.year}")



class Question():
    def __init__(self,text,choices,answers):
        self.text = text
        self.choices = choices
        self.answers = answers

    def CheckAnswers(self,answers):
        return  self.answers == answers



q1 =   Question("En iyi proglamama dili?",[",java","C#","pyhton"],"python")
q2 =   Question("En popüler proglamama dili",[",java","C#","pyhton"],"python")
q3 =   Question("En çok kazandıran proglamama dili?",[",java","C#","pyhton"],"python")

# print(q1.CheckAnswers("C#"))

class Quiz():
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.QuestionIndex = 0

    def GetQuestion(self):
        return  self.questions[self.QuestionIndex]

    def DisplayQuestion(self):
        question = self.GetQuestion()
        print(f"Soru {self.QuestionIndex + 1} : {question.text}")

        for q in question.choices:
            print("-" + q)

        answers = input("cevap:")

        self.guess(answers)

    def guess(self,answers):
        question = self.GetQuestion()

        if Question.CheckAnswers(answers):
            self.score += 1
        self.QuestionIndex += 1

        self.DisplayQuestion()





        q1 = Question("En iyi proglamama dili? ", [",java", "C#", "pyhton"], "python")
        q2 = Question("En popüler proglamama dili? ", [",java", "C#", "pyhton"], "python")
        q3 = Question("En çok kazandıran proglamama dili? ", [",java", "C#", "pyhton"], "python")
questions = [q1,q2,q3]
quiz = Quiz(questions)
question =quiz.questions

quiz.DisplayQuestion()


