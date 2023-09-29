import felhantering
""" Importerar vår fil med filhantering för namn och personnummer """

class Student:
    """ Introducerar en class. Student. där man kan spara förnamn, efternamn och personnummer i de tre
    attributerna. """
    
    def __init__(self, förnamn, efternamn, personnummer):
        """ konstruktorn som anropas när vi lägger till ny student.
        Tilldelar parametrar: förnamn(str), efternamn(str), personnummer(int)"""
        
        self.förnamn = felhantering.bokstav("Vad är studentens förnamn? ")
        self.efternamn = felhantering.bokstav("Vad är studentens efternamn? ")
        self.personnummer = felhantering.siffra("Vad är studentens personnummer? ")
        print("Objekt skapat! ")
        
    def __str__(self):
        """ __str__ formulerar hur vår utskrift kommer att se ut när den printas. """
        
        return "Namn: " + str(self.förnamn) + " " + str(self.efternamn) + " Personnummer: " + str(self.personnummer)


def main(): # Taget från OLI sidorna
   
    studentlista = []
    studentlista.append(Student("förnamn", "efternamn", "personnummer"))
    studentlista.append(Student("förnamn", "efternamn", "personnummer"))
    studentlista.append(Student("förnamn", "efternamn", "personnummer"))

    print("Här är alla sparade objekt:")

    for student in studentlista: # Taget från OLI sidorna
        print(student)

main()
