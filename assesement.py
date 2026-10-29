import pandas as pd

data = {
    "Name": ["Asha", "Riya", "Neha"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
