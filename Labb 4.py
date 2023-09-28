class Student: # Definerar en class, student där 
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = input(print("Vad är studentens förnamn?"))
        self.efternamn = input(print("Vad är studentens efternamn?"))
        self.personnummer = input(print("Vad är studentens personnummer?"))

    def __str__(self):
        return "Namn: " + self.förnamn + " " + self.efternamn + " Personnummer: " + str(self.personnummer)


def main():
    studentlista = []
    studentlista.append(Student("förnamn", "efternamn", 2001))
    studentlista.append(Student("förnamn", "efternamn", 2001))
    studentlista.append(Student("förnamn", "efternamn", 2001))

    for student in studentlista: # Taget från OLI sidorna
        print(student)

main()