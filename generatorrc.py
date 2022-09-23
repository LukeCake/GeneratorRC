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
            f.write(str(rc)+ "\n")

print("Zápis proběhl do soubru ./seznamRc.txt")