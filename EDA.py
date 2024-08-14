import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv(r"E:\Dheeraj\Finlatics Python\Capsule 4\titanic.csv")
df = sns.load_dataset("titanic")

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# print(df.head())
# print(df.tail(10))
# print(df.info())
# print(df.shape)
# print(df.columns)
# print(df["survived"])
# print(df["sex"])

# unique_counts = df.nunique()
# print(unique_counts)
# embarktown_unique_counts = df["embark_town"].unique()
# print(embarktown_unique_counts)
# sex_unique_counts = df["sex"].unique()
# print(sex_unique_counts)

# sex_value_counts = df["sex"].value_counts()
# print(sex_value_counts)
# survived_value_counts = df["survived"].value_counts()
# print(survived_value_counts)

# grouped_data_1 = df.groupby(["sex", "survived"])["survived"].count()
# print(grouped_data_1)
# grouped_data_2 = df.groupby(["pclass", "survived"])["survived"].count()
# print(grouped_data_2)
# grouped_data_3 = df.groupby(["embark_town", "pclass", "survived"])["survived"].count()
# print(grouped_data_3)

"""sns.countplot(x = "sex", hue = "survived", data = df)
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.title("Survival by Gender")
plt.show()"""

"""sns.countplot(x = "pclass", hue = "survived", data = df)
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.title("Survival by Class")
plt.show()"""


