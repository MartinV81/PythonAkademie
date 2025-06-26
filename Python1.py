print("hello world")
print(1 + 1)
# základní aritmetické operace
print(100 + 200)
print(300 - 100)
print(10 * 50)

# všimni si, jak klasické dělení nevrátí celé číslo,..
# ..ale desetinné číslo. Není to žádná chyba,..
# ..ale záměrný účel tohoto operátoru
print(700 / 350)

# pokud chceš ověřit, že jde skutečně o datový typ celých čísel,..
# ..vyzkoušej funkci type
print("Zkousim funkci type")
print(type(100))
# sčítání desetinných čísel
print(0.1 + 0.1)

# odčítání desetinných čísel
print(1.5 - 0.3)

# pomocí funkce type zkoušíme, jaký je číslo 1.3 datový typ
print("Test datoveho typu u cisla 1.3. Datovy typ je:")
print(type(1.3))
print(0.1 + 0.2)
print(10 // 3)
print(11 // 2)
print(10 % 3)
print(11 % 3)
# hodnota dva na druhou
print(2 ** 2)

# hodnota dva na třetí
print(2 ** 3)
# celočíselné dělení
print("Vytisknu vysledek z celociselneho deleni")
print(10 // 3)

# modulo (zbytek po dělení)
print("Vytisknu vysledek z modula, tzn. zbytek po deleni")
print(4 % 3)

# umocňování (2 ** 3 je hodnota dva na třetí)
print("Vytisknu vysledek z umocneni dva na treti")
print(2 ** 3)
print(144/12)
# zapisujeme string pomocí dvojitých uvozovek
print("Python")
# použijeme funkci type
print(type("Python"))
print("Marian")

# míň používaná varianta
print("""Marian""")
# Pouze textové znaky
print("Python")

# .. funguje i s číslem
print("Python3")

# .. s desetinným číslem
print("Python3.9")

# ověříme, že i čísla v uvozovkách jsou string
print(type("12345"))

# taky další znaky jsou string
print(type("@#!"))
print("It's friday")
print("It\'s \"kind of\" friday")
print("Prvni" + "Druhy")
print("123" + "456")
print("+" + "-" + "*" + "/")
# index 1 ti vypíše druhý znak
print("autobus"[1])
print("autobus"[0])
print("autobus"[1])
print("autobus"[2])
print("autobus"[3])
print("autobus"[-1])
print("autobus"[-2])
print("autobus"[-3])
# zkouška
# první dvě písmena
print("autobus"[0:2]) 

# první dvě písmena, ale zápis jedním číslem
print("autobus"[:2]) 

# od třetího písmena do konce
print("autobus"[2:7]) 

# od třetího písmena do konce, zápis jedním číslem
print("autobus"[2:])
# obrácené pořadí, začne "s", jeden znak za druhým
print("autobus"[::-1]) 

# obrácené pořadí, začne "s", poté každý druhý znak
print("autobus"[::-2]) 

# obrácené pořadí, začne "s", poté každý třetí znak
print("autobus"[::-3])
# tvorba proměnné jmeno s hodnotou Lukas
jmeno = "Lukas"

# použití proměnné
print(jmeno)
# proměnná jmeno obsahuje jen písemné znaky
jmeno = "Lukas"

# obsahuje i číselné znaky
jmeno2 = "Matous"

# obsahuje podtržítko
moje_jmeno = "Jan"

# jestli chceme proměnné vypsat, použijeme funkci print
print(jmeno)
print(jmeno2)
print(moje_jmeno)
mojeJmeno = "Matous"
novaHodnota = 1234
moje_jmeno = "Matous"
nova_hodnota = 1234
TIHOVE_ZRYCHLENI = 9.81
PI = 3.141
# tvůj první list
print(["Matous", "Marek", "Lukas"])
# můžeš si ověřit, jestli máme datový typ list
print(type(["Matous", "Marek", "Lukas"]))
# takhle vytvoříš list dle 1. možnosti
prvni_seznam = []

# takhle vytvoříš list dle 2. možnosti
druhy_seznam = list()

# ověř, že obě možnosti vyprodukovaly datový typ list
print(type(prvni_seznam))
print(type(druhy_seznam))
muj_seznam = ["Matous", "Marek", "Lukas"]
# chceš si vypsat první hodnotu z muj_seznam, index 0
print(muj_seznam[0])

# vypiš druhou hodnotu s indexem 1
print(muj_seznam[1])

# vypiš poslední hodnotu v listu, s indexem -1
print(muj_seznam[-1])

# poslední hodnota je třetí hodnota v listu
# takže jméno Lukas vypíše i index 2
print(muj_seznam[2])
treti_tupl = ("Praha", "Berlin", "Viden", "Bratislava")

# pozor, tuple můžeš vytvořit i bez kulatých závorek
# ..není to bežné, ale budeš vědět, že to existuje
ctvrty_tupl = 1.3, 3.6, 1.8, 0.4, 1.9

print(type(treti_tupl))
print(type(ctvrty_tupl))
jmeno = input("Zadej jméno:")

# uloženou hodnotu v proměnné pak vypíšeme
print(jmeno)

# můžeš ji vypsat i s nějakým textem
print("Tvé jméno je:", jmeno)
