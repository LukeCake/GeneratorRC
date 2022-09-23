# Random person ID generator / Generátor rč pro osoby narození od 1960 do 1999

import random

def divisible_random(a,b,n):
    if b-a < n:
      raise Exception('{} is too big'.format(n))
    result = random.randint(a, b)
    while result % n != 0:
      result = random.randint(a, b)
    return result

#input
outputs = int(input('Kolik rodných čísel chceš generovat?: '))

with open("seznamRc.txt", "w", encoding="utf-8") as f:
    for i in range(outputs):
            # get a random int in the range 6001010000 - 9930129999, the number is divisible by 11
            rc = divisible_random(6001010000,9930129999,11)
            print(rc)

            rcyear = str(rc)
            slice_year = slice(0, 2)
            rcyear = rcyear[slice_year]

            rcmonth = str(rc)
            slice_month = slice(2, 4)
            rcmonth = rcmonth[slice_month]

            rcday = str(rc)
            slice_day = slice(4, 6)
            rcday = rcday[slice_day]


            print(rcyear + "/" + rcmonth + "/" + rcday)


            f.write(str(rc)+ "\n")

print("Zápis proběhl do soubru ./seznamRc.txt")