# 3a Betrakta funktionen find_median(numbers), som tar en lista med tal och returnerar medianen.
# Median är det mittersta talet, t.ex. är medianen 2 för listan [1, 2, 1000].
# Om listan har jämnt antal element ska funktionen returnera medelvärdet av de två mittersta talen.
# Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.

# som en matematiker
# vill jag kunna ange en lista
# så att jag får tillbaka medianen

# Tasks:
# Hitta det mittersta talet i en lista av tal
# kontrollera att listan består av tal
# om listan består av jämnt antal element ska de två mittersta talen summeras och delas med 2

def find_median(numbers_list:list):
    numbers_list_sorted = sorted(numbers_list)
    # längden räknar 1, 2, 3...
    # index räknar 0, 1, 2, 3...
    list_length = len(numbers_list_sorted)
    # heltalsdivision
    middle = list_length // 2
    # för en lista med udda antal nummer, är mittens index heltalsdivisionen
    if list_length % 2 == 1:
        median = numbers_list_sorted[middle]
        return median
    # för en lista med jämnt antal nummer,
    # summera index middle + (middle -1) och dela sedan med 2
    if list_length % 2 == 0:
        sum_two_middle_numbers = numbers_list_sorted[middle] + numbers_list_sorted[middle - 1]
        median = sum_two_middle_numbers / 2
        return median
nummer = (1, 2, 3, 4, 5)
print(find_median(nummer))
find_median(nummer)




