"""
uppgift 2_1
2_1a Hitta på lämpligt testdata till följande funktion,
som omvandlar grader Celsius till grader Fahrenheit.
       testdata C: -300.. -273,146... -273,15... 0... 100
 2_1b Vilka ekvivalensklasser har parametern degree?
       1. över eller lika med -273,15 (absoluta nollpunkten)
       2. under -273,15
"""



def c_to_f(degree:float):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32