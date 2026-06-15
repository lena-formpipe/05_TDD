from autocomplete_list import *
from balansera_listor import *
from multiplication_table import *
from uppg1_3count_vowels import *
from uppg2_1celsius import *
from uppg2_2count_words import *
from uppg2_3find_median import *

print("Anrop av funktion autocomplete_list():")
input = "ANN"
name_list = ["Peter", "Annmarie", "GullANn"]
print(f"user_input {input} samt name_list {name_list}")
autocomplete = autocomplete_list(input, name_list)
print(f"Svar: {autocomplete}")
print("---------------------------")

print("Anrop av funktion multiplication_table():")
print("n = 5 och limit = 4")
multiplication = multiplication_table(n =5, limit=4)
print(f"Svar: multiplikationstabellen {multiplication}")
print("---------------------------")

print("Anrop av funktion balansera_listor():")
list_a = [1, 2, "hej"]
list_b = [4, 5, True, False, 10]
print(f"list_a = {list_a} och list_b = {list_b}")
balanserad = balansera_listor(list_a, list_b)
print(f"Svar: nya balanserade listor {balanserad}")
print("---------------------------")

print("Anrop av funktion count_vowels(word):):")
word = "hälleflundrA"
print(f"word = {word}")
vokaler = count_vowels(word)
print(f"Svar: Antal vokaler {vokaler}")
print("---------------------------")

print("Anrop av funktion c_to_f(degree):")
degree = 50
print(f"degree = {degree}")
fahrenheit = c_to_f(degree)
print(f"Svar:F {fahrenheit}")
print("---------------------------")

print("Anrop av funktion count_words(string):):")
string = "Hej alla barn i Bullerbyn"
print(f"sträng = {string}")
ord = count_words(string)
print(f"Svar: Antal ord {ord}")
print("---------------------------")

print("Anrop av funktion find_median(string):")
string_numbers = [1, 2, 3, 4, 5]
print(f"sträng = {string_numbers} har median 3")
medianen = find_median(string_numbers)
print(f"Svar: Median {medianen}")
print("---------------------------")

print("Anrop av funktion find_median(string):")
string_numbers = [1, 2, 3, 4, 5]
print(f"sträng = {string_numbers} har median 3")
medianen = find_median(string_numbers)
print(f"Svar: Median {medianen}")
