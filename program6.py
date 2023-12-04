class Person:
    count=0
    def __init__(self,name,age,collegename):
        self.name=name
        self.age=age
        self.collegename=collegename
        Person.count+=1
person1=Person("lucky",25,"awec")
person2=Person("lahari",30,"awec")
print(Person.count)
print(person1.name)
print(person2.age)
print(person1.collegename)