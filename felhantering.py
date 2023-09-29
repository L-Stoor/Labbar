

def bokstav(prompt):
    """ Felhanteringen kommer att sköta alla inmatningsfel användaren gör under förnamn och eftternamn.
    Godkänner inte siffror i namnen, utan bara bokstäver. """
   
    while True:
        try:
            tecken = input(prompt)
            if not tecken.isalpha() == True:    
                raise ValueError
            else:
                return tecken
        except ValueError:
            print("Får bara vara bokstäver :) ")


def siffra(prompt):
    """ Felhanteringen kommer att stoppa användaren från att ange personnummer med något annat än siffror. """
   
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ett personnummer innehåller inte bokstäver :) ")