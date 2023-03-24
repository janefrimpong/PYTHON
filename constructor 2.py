class Person():
    def __init__(self,name ,age ):
        self.name=name
        self.age=age
    def level(self):
        print(f"hola , this is {self.name},I am {self.age}")
        int(input("Enter your level :"))


kell=Person("Megatron",18)
kell.level()



