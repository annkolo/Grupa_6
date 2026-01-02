
# Otwórz plik z danymi
with open('dane.txt', 'r') as plik:
    linie = plik.readlines()

print("Waga | Wzrost | BMI   | Stan")
print("-" * 30)

# Dla każdej linii w pliku...
for linia in linie[1:]:
    linia = linia.strip()  # Usuń spacje/enter
    if linia:  # Jeśli linia nie jest pusta
        # Podziel linię po przecinku
        czesci = linia.split(',')
        waga = float(czesci[0])   # Pierwsza część to waga
        wzrost = float(czesci[1]) # Druga część to wzrost
        
        # OBLICZ BMI (jedyny wzór do zapamiętania)
        bmi = waga / (wzrost * wzrost)
        
        # Sprawdź kategorię
        if bmi < 18.5:
            stan = "niedowaga"
        elif bmi < 25:
            stan = "norma"
        elif bmi < 30:
            stan = "nadwaga"
        else:
            stan = "otyłość"
        
        # Pokaż wynik
        print(f"{waga:4.0f} | {wzrost:6.2f} | {bmi:5.1f} | {stan}")
