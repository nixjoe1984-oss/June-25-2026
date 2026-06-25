class dog:
    animal="pet"
    def __init__(self,breed,color):
        self.breed=breed
        self.color=color
Huskey=dog("Huskey","Black and White")
Golden_Retriever=dog("Golden Retriever","Golden")
print("A {} is a {}.".format(Huskey.breed, Huskey.animal))
print("A {} is also a {}".format(Golden_Retriever.breed,Golden_Retriever.animal))
print("A {} is {}".format(Huskey.breed,Huskey.color))
print("A {} is {}".format(Golden_Retriever.breed,Golden_Retriever.color))