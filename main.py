namn = input("Vad är ditt namn?")
print(f"Hej, {namn} välkommen till testet!")
val = input("Vill du fortsätta? (ja/nej)")
if val.lower() == "ja":
    print("Bra! Vi fortsätter.")
else:
    print("Okej, vi avslutar testet. Ha en bra dag!")
    exit()

print(f"Framför {namn} ser vi tre dörrar. En röd, en blå och en grön.")
dörr_val = input(f"Vilken dörr vill {namn} gå igenom? (röd/blå/grön)")
if dörr_val.lower() == "blå":
    print(f"{namn} går igenom den blå dörren och kommer till ett nytt rum.")
elif dörr_val.lower() == "grön":
    print(f"{namn} går igenom den gröna dörren och kommer till ett mörkt och läskigt rum.")
    print("Plötsligt börjar väggarna röra sig innåt och du blir klämd till dödens.")
    print("Game Over")
    exit()

else:
    print(f"{namn} går igenom den röda dörren och faller ner för ett stup och dör.")
    print ("Game Over")
    exit()
print(f"{namn} går in i rummet och ser en lapp på golvet. Lappen säger: 'För att ta dig vidare måste du svara på två frågor korrekt.'")
frågor_val = input(f"Vill {namn} fortsätta? (ja/nej)")
if frågor_val.lower() == "ja":
    print("Bra! Första frågan är...")
else: 
    print(f"Okej, {namn} lämnar rummet och går hem.")
    exit()

fråga1 = input(f"Fråga 1: Är 2*2 + 5 = 10? (ja/nej)")
if fråga1.lower() == "nej":
    print(f"{namn} svarade rätt!")
else:
    print(f"Fel svar! {namn} är ute ur spelet.")
    print("Game Over")
    exit()

fråga2 = input(f"Fråga 2: Är 5*(2+6) = 40? (ja/nej)")
if fråga2.lower () == "ja":
    print(f"Korrekt svar! Framför {namn} står det en skattkista med 1 miljon kronor!")
    print(f"Grattis {namn}! Du tog dig igenom spelet!")
else:
    print(f"Fel svar! Nu kommer {namn} avrättas.")
    print("Game Over")
    exit () 
    