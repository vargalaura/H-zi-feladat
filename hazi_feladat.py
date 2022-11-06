#1.40 és 10 közötti számok kiíratása(csökkenő)!
for x in range(40,9,-1):
    print(x)
    
#2.Írjuk ki 1-100 között a számokat!
for x in range(1,101,1):
    print(x)
   
#3.Kérjünk be egész számokat mind addig, amíg nem kapunk 20-nál nagyobb értéket.
y = int(input("Kérem a számot:"))

while y < 20:
    y = int(input("Kérem a számot:"))

#4.10 és 20 közötti páros számok kiírása:
x = 10
while x < 21:
    if x % 2 == 0:
        print(x)
    x += 1
    
#5.10 és 100 között írjunk ki minden 2. értéket while ciklus segítségével
szam = 10
while szam <= 100:
    print(szam)
    szam = szam +2