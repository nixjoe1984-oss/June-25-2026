class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

parrot1=parrot("Mirah",7)
parrot2=parrot("Jordan",12)
print("Mirah is a {}".format(parrot1.species))
print("Jordan is also a {}".format(parrot2.species))
print("{} is {} years old.".format(parrot1.name,parrot1.age))
print("{} is {} years old.".format(parrot2.name,parrot2.age))