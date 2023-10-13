"""Denna fil importeras senare in till vårt huvudprogram"""

def lista(prompt):
    """ Vår felhantering så användaren inte anger fel filnamn, godtar bara "students.txt" """

    while True:
        try:
            fil = input(prompt)
            if fil != "students.txt":
                print("Den filen finns inte. Skriv in ny fil. ")
            else:
                return open("students.txt", "r", encoding = "utf-8")
        except FileNotFoundError:
            print("Filen kunde inte hittas, skriv in ny fil. ")
