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
counter = 0
outputs = int(input('Kolik rodných čísel chceš generovat?: '))

with open("seznamRc.txt", "w", encoding="utf-8") as f:

    while(counter < outputs):
            # get a random int in the range 6001010000 - 9930129999, the number is divisible by 11
            rc = divisible_random(1000000000,9999999999,11)

            #slice YY/MM/DD
            rcyear = str(rc)
            slice_year = slice(0, 2)
            rcyear = rcyear[slice_year]

            rcmonth = str(rc)
            slice_month = slice(2, 4)
            rcmonth = rcmonth[slice_month]
            rcday = str(rc)
            slice_day = slice(4, 6)
            rcday = rcday[slice_day]

            # chceck real date YY/MM/DD
            # RČ do roku 1953 byly za / 3 místná
            if 0 < int(rcyear) <21 or 53 < int(rcyear) < 99:
                if 0 < int(rcmonth) <= 12:
                    # řešíme jen dny 1 - 28 kvůli přestupnému roku
                    if 0 < int(rcday) <= 28:
                        # create rndm woman ID = MM + 50
                        rndmsexlist = [0, 50]
                        if (random.choice(rndmsexlist)) != 0:
                            print("\nNÁHODNÁ Žena měním RČ z " + str(rc))
                            rc = rc + 50000000
                            print("na " + str(rc))
                            print("Podmínky OK, Zapisuji ŽENU do souboru - RČ: " + str(rc))
                            counter = counter + 1
                            f.write(str(rc) + "\n")
                        else:
                            print("\nPodmínky OK, Zapisuji MUŽE  do souboru - RČ: " + str(rc))
                            counter = counter + 1
                            f.write(str(rc) + "\n")

    print("Celkem vygenerováno RČ: " + str(counter))
print("Zápis proběhl do soubru ./seznamRc.txt")