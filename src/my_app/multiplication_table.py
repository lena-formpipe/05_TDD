# Multiplikationstabell
# Funktion ska ge oss multiplikationstabellen.
# Parametern "n" talar om vilket tals tabell vi ska skapa.
# Parametern "limit" talar om var vi ska sluta multiplicera.
# Exempel 3:ans tabell, med limit==2, ska programmet räkna ut:3*1 = 3, 3*2 = 6
# multiplication_table(3, 2) → [3, 6]

# Formulera krav
# som användare
# vill jag kunna ange vilket tal och antal multiplikationer (med start från 1)
# så att jag får en lista med talets uträknade mulitplikationstabell

def multiplication_table(n, limit):
    # provar att sätta båda valideringarna för int i samma if-sats
    # då blir inte exakt position utpekad utan ges generellt meddelande om int.
    if not isinstance(n, int) or not isinstance(limit, int):
        raise TypeError("Parametrar måste vara av typen int.")

    multiplication_list = []

    for i in range(1, limit+1):
        value = n*i
        multiplication_list.append(value)
        i += 1
    return multiplication_list

