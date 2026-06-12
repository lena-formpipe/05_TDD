# Balansera listor
# Som en del i ett större program har vi en lista som kan innehålla flera element.
# Men elementen kan flyttas mellan denna och en annan lista.
# Vi behöver ett sätt att balansera listorna, så att de har lika många element (ungefär).
# Ordningen på elementen är inte viktig.

# krav:
# som en användare
# vill jag kunna mata in två listor och få dem balanserade
# så att båda listorna innehåller samma mängd element.

# acceptanskriterier
# 1. kunna räkna antalet element i två listor och se vilken som är längst
# 2. kunna beräkna differensen mellan listorna
# 3. flytta halva differensen element till den mindre listan och returnera nya listor
# 4. om differensen är 1 eller 0 ska ingen lista ändras
# 4. ta hänsyn till ifall inparametrar inte är listor



def balansera_listor(list_a:list, list_b:list):
    diff_length = len(list_a) - len(list_b)
    # om diff mellan -1 och 1
    if abs(diff_length <= 1) :
        return list_a, list_b
    else:
        # abs(x) gör att vi inte behöver fundera om värdet är positivt eller negativt
        while abs(len(list_a) - len(list_b)) > 1:
            if len(list_a) > len(list_b):
                list_b.append(list_a.pop())
            else:
                lista_a.append(lista_b.pop())
        return list_a, list_b

print(balansera_listor([1, 2, 3,4, 5], [1, 2]))
