""" Importerar vår felhanterings kod som hanterar vår input i koden """
import hanteralabb


def läsa_fil():
    """ Skapar en funktion som ska öppna och läsa innehållet 
    i en fil och lägga in informationen i en lista """

    fil = hanteralabb.lista("Vad heter filen? ") #filen öppnas via vår felhantering
    lista = []

    for n in range(6): # Det är antalet studenter som finns i listan "students.txt"

        personnummer = fil.readline().strip()
        namn = fil.readline().strip()
        efternamn = fil.readline().strip()
        lista.append([efternamn, namn, personnummer])

    print("Dessa studenter är skrivna på KTH")
    return lista

for line in läsa_fil(): # Printar ut antalet studenter som finns med i den skapade listan
    print("Namn: " + line[0] + " " + line[1] + " Personnummer: " + line[2])
