namn = input("Vad är ditt namn?")
print(f"Hej, {namn} välkommen till testet!")
val = input("Vill du fortsätta? (ja/nej)")
if val.lower() == "ja":
    print("Bra! Vi fortsätter.")
else:
    print("Okej, vi avslutar testet. Ha en bra dag!")
    exit()

print("Framför dig ser du tre dörrar. En röd, en blå och en grön.")
dörr_val = input("Vilken dörr vill du gå igenom? (röd/blå/grön)")
if dörr_val.lower() == "blå":
    print("Du går igenom den blå dörren och kommer till ett nytt rum.")
elif dörr_val.lower() == "grön":
    print("Du går igenom den gröna dörren och kommer till ett mörkt och läskigt rum.")
    print("Plötsligt börjar väggarna röra sig innåt och du blir klämd till dödens.")
    print("Game Over")
    exit()

else:
    print("Du går igenom den röda dörren och faller ner för ett stup och dör.")
    print ("Game Over")
    exit()
print("I det nya rummet ser du en lapp på golvet. Den säger: 'Två frågor kvar sedan är skatten din!")
frågor_val = input("Vill du fortsätta? (ja/nej)")
if frågor_val.lower() == "ja":
    print("Bra! Första frågan är...")
else: 
    print("Okej, lämna gärna rummet och gå hem.")
    exit()

fråga1 = input("Fråga 1: Är 2*2 + 5 = 10? (ja/nej)")
if fråga1.lower() == "nej":
    print("Du svarade rätt!")
else:
    print("Fel svar! Du är ute ut spelet.")
    print("Game Over")
    exit()

fråga2 = input("Fråga 2: Är 5*(2+6) = 40? (ja/nej)")
if fråga2.lower () == "ja":
    print("Korrekt svar! Framför dig har du skattkistan med 1 miljon kronor!")
else:
    print(f"Fel svar,{namn}! nu kommer du avrättas.")
    print("Game Over")
    exit ()