from os import name


class student:

    def __init__(self, name: str, age: int, classname = "student"):
        self.name = name
        self.age = age
        self.classname = classname
    def averagetestscore (self, name: str, test1: int, test2: int, test3: int):
        return ((test1 + test2 +test3)/3)
        
    

John = student("John", 21, "IT")
Jane = student("Jane", 22, "")
Adam = student("Adam", 23, "")
Ben = student("Ben", 20, "")
Becky = student("Becky", 28, "")

p1Avg = John.averagetestscore (John, 10,10,20)
p2Avg = Jane.averagetestscore (Jane, 30,20,10)
p3Avg = Adam.averagetestscore (Adam, 15,30,20)
p4Avg = Ben.averagetestscore (Ben, 15, 20, 19)
p5Avg = Becky.averagetestscore (Becky, 20, 22, 20)

Students_test_average = {John : p1Avg, Jane : p2Avg, Adam : p3Avg, Ben : p4Avg, Becky : p5Avg}


print(Students_test_average[Jane])
print(getattr (John, "classname"))


