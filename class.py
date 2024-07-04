class clothes:
    def __init__(self, type, size, color,gender):
        self.type = type
        self.size = size
        self.color = color
        self.gender = gender

    def wash(self):
        print(self.type,"is being washed")

cloth1 = clothes("shirts","small","white","male")
cloth2 = clothes("blouse","medium","grey","female")

print(cloth1.type)
print(cloth1.size)