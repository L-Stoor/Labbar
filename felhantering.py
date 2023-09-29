"""Denna fil importeras senare in till vårt huvudprogram i en annan fil"""

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
            print("Namnet får bara innehålla bokstäver :) ")


def siffra(prompt):
    """ Felhanteringen kommer att stoppa användaren från att ange personnummer med något annat än siffror. """
   
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ett personnummer innehåller inte bokstäver :) ")
