# 2a Betrakta funktionen count_words(sentence), som tar en sträng och returnerar antalet ord.

# User story: "som en användare vill jag veta hur många ord en mening innehåller så att jag kan skriva ner det."
# Acceptanskriterier:
# appen ska varna om det inte är en lista
# appen ska kunna hantera en tom lista
# appen ska kunna räkna ord som har mellanslag som avskiljare

def count_words(sentence):
    # kontrollera att det är en sträng
    if not isinstance(sentence, str):
        raise TypeError(f"Input måste vara en sträng, inte {type(sentence)}.")
    words = sentence.split()
    return len(words)
