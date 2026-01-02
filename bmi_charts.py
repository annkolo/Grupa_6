import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
 
def load_data(file_path="wyniki.txt"):
    df = pd.read_csv(
        file_path,
        header=None,
        names=["Waga_kg", "Wzrost_m", "BMI"],
        sep=","
    )
    return df
 
 
def add_bmi_category(df):
    def category(bmi):
        if bmi < 18.5:
            return "Niedowaga"
        elif bmi < 25:
            return "Norma"
        elif bmi < 30:
            return "Nadwaga"
        else:
            return "Otylosc"
 
    df["Kategoria"] = df["BMI"].apply(category)
    return df
 
 
def plot_bmi(df):
    sns.set(style="whitegrid")
 
    plt.figure(figsize=(8, 5))
    sns.histplot(df["BMI"], bins=10, kde=True)
    plt.title("Rozklad BMI")
    plt.xlabel("BMI")
    plt.ylabel("Liczba osob")
    plt.show()
 
 
def plot_categories(df):
    plt.figure(figsize=(7, 5))
    sns.countplot(x="Kategoria", data=df)
    plt.title("Kategorie BMI")
    plt.xlabel("Kategoria")
    plt.ylabel("Liczba osob")
    plt.show()
 
 
def main():
    df = load_data("wyniki.txt")
    df = add_bmi_category(df)
 
    print(df.head())
    plot_bmi(df)
    plot_categories(df)
 
 
if __name__ == "__main__":
    main()