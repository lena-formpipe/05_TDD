# Söka efter användare
# Funktionen autocomplete_list(input, master_list)
# används för att visa sökresultat medan användaren skriver i ett sökfält.
# Funktionen tar två parametrar:
# - input är det användaren skriver,
# - master_list är en lista med alternativ som kan hittas.

# Formulera krav och acceptanskriterier.
# User story: Som en användare vill jag
# mata in delar av namn
# så att programmet kan visa mig vilka möjliga träffar som finns.

# AK1: om user_input inte är en string ska funktionen returnera False
# AK2: om name inte är en string ska funktionen returnera False
# AK3: om user_input återfinns i name, oberoende av case, ska funktionenreturnera en lista av alla passande namn
# AK4: annars (om strängarna är olika) returnera False(eller tom lista?)


def autocomplete_list(user_input: str, name_list:list):
    # kontroll att input och name är strängar
    if not isinstance(user_input, str):
        raise TypeError("Input måste vara en sträng.")
    if not isinstance(name_list, list):
        raise TypeError("Namnen som jämförs måste vara en lista")

    # skapa en to lista som ska innehålla matchande namn
    lista_matchningar = []
    for x in name_list:
        if user_input.lower() in x.lower():     # jämför gemener
            lista_matchningar.append(x)
    if len(lista_matchningar) > 0:
        return lista_matchningar
    elif len(lista_matchningar) == 0:
        return False


