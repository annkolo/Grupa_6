ile = int(input("Ilu ludzi chcesz wpisać? "))
with open("wyniki.txt", "a") as plik:
    for i in range(ile):
        waga = float(input("Waga (kg): "))
        wzrost = float(input("Wzrost (m): "))
        bmi = round(waga / (wzrost**2), 2)
        if bmi < 18.5:
                kat = "Niedowaga"
                info = "Masz niedowagę - udaj się do lekarza."
            elif 18.5 <= bmi < 25:
                kat = "Norma"
                info = "Twoja waga jest prawidłowa. Tak trzymaj!"
            elif 25 <= bmi < 30:
                kat = "Nadwaga"
                info = "Masz nadwagę - zadbaj o aktywność fizyczną."
            else:
                kat = "Otyłość"
                info = "Otyłość - skonsultuj się z dietetykiem."
        plik.write(f"{waga}, {wzrost}, {bmi}\n")