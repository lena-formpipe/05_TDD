# 3a Diskutera följande kod. Ett testfall räcker inte för att testa funktionen
# föreslå fler testfall, som täcker in alla olika möjligheter för count_vowels.
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)

from collections import Counter

def count_vowels(word):
    # Omvandla till gemener för enklare hantering
    # läste att det även en funktion som heter casefold, men jag avstår från den här

    # kontrollera att det är en sträng och omvandla till gemener
    if not isinstance(word, str):
        raise TypeError(f"Input måste vara en sträng, inte {type(word)}.")
    gemener = word.lower()
    vokaler = "aeiouyåäö"  # kollar endast gemener
    antal_vokaler = 0
    # hantera tom sträng
    if word == "":
        return 0
    # om strängen innehåller något...
    elif len(gemener) > 0:
        for tecken in gemener:
            if tecken in vokaler:
                antal_vokaler += 1
        return antal_vokaler
    # return None

print(count_vowels("hej dÅ"))