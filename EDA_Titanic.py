import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv(r"E:\Dheeraj\Finlatics Python\Capsule 4\Titanic.csv")
df = sns.load_dataset("Titanic")

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

"""sns.catplot(x = "embark_town", hue = "survived", col = "pclass", data = df, kind = "count", palette = "Set2")
plt.xlabel("Embarkation Town")
plt.ylabel("Number of Passengers")
plt.suptitle("Survival by Embarkation Town and Passenger Class")
plt.show()"""

# print(df.describe())
# print(df["embark_town"].describe())

# print(df["survived"].value_counts())
# print(df["alive"].value_counts())
#df.drop(columns = ["alive"], inplace = True)
#print(df.columns)
# print(df["embarked"].value_counts())
# print(df["embark_town"].value_counts())
# df.drop(columns = ["embarked"], inplace = True)  
# print(df.columns)
# print(df["class"].value_counts())
# print(df["pclass"].value_counts())
# df.drop(columns = ["class"], inplace = True)
# print(df.columns)

# print(df["adult_male"].value_counts())
# df["adult_male"].replace({True : 1, False : 0}, inplace = True)
# print(df["adult_male"].value_counts())

# print(df.isnull().sum())
# df.dropna(subset = ["age"], inplace = True)
# print(df.isnull().sum())

"""sns.boxplot(y = "age", data = df)
plt.ylabel("Age")
plt.title("Box Plot for Age Column")
plt.show()"""

# df["age"] = df["age"].fillna(df["age"].median())
# df["deck"] = df["deck"].fillna(df["deck"].mode()[0])
# df.dropna(subset = ["embark_town"], inplace = True)
# print(df.isnull().sum())

# df.rename(columns = {"deck" : "cabin"}, inplace = True)
# print(df.columns)

"""plt.hist(df["who"], color = "skyblue", edgecolor = "black")
plt.xlabel("Passenger Type")
plt.ylabel("Frequency")
plt.title("Distribution of Passengers Types")
plt.show()"""

numeric_df = df.select_dtypes(include = ["int64", "float64"])
corr_matrix = numeric_df.corr()
plt.figure(figsize = (10, 10))
sns.heatmap(corr_matrix, annot = True, cmap = "PuBuGn", fmt = ".2f")
plt.title("Correlation Matrix of Titanic Dataset")
plt.show()
