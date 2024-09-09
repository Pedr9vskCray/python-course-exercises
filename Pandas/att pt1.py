import pandas as pd
import numpy as np

# atividade 1

df = pd.DataFrame({
    "Sede" : ["Nova Iorque", "São Paulo", "Nova Iorque", "Londres", "Londres"],
    "Piloto" : ["Mike Ross", "Sebastian Thomas", "Glen Are", "Michael Schum", "Luiz da Silva"],
    "Mundiais" : [10, 11, 0, 3, 44],
    "Vitórias" : [321, 229, 12, 44, 1023] 
    })

df.index = ["X Racing", "Equatorial", "Typo", "Blue Race", "Capa Racing"]

print(df)

print("\n")

# atividade 2

print(df.loc["Blue Race"])

print("\n")

# atividade 3

print(df.loc["Capa Racing", "Mundiais"])

print("\n")

# atividade 4

print(df.loc[df["Mundiais"] >= 10])

print("\n")

# atividade 5

print(df.loc[(df["Mundiais"] >= 10) & (df["Vitórias"] > 300)])

print("\n")

# atividade 6

df.at["Equatorial", "Piloto"] = "Antônio Racer"

print(df)

print("\n")

# atividade 7

df.loc["X Racing",["Sede", "Vitórias"]] = ("São Paulo", df.loc["X Racing", "Vitórias"]+1)

print(df)

print("\n")

# atividade 8

df.loc["Red Cow"] = ("São Paulo", "Fernando Vetel", 0, 0)

print(df)

print("\n")

# atividade 9

df.sort_values("Vitórias", ascending=False, inplace=True)

print(df)