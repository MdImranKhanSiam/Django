class person:
    lastname = "Siam"

    def __init__(self, Name):
        self.name = Name

p1 = person('Imran')
p2 = person('Rafiq')

p1.lastname = "Khan"
person.lastname = "Khan"

print(p1.lastname)
print(p2.lastname)