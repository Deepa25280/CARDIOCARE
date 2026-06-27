import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/heart.csv")
df=df.drop(columns=["id","dataset"])


# Set Seaborn Style
sns.set_style("whitegrid")

# -----------------------------
# 1. Age Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["age"], bins=10, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.show()

# -----------------------------
# 2. Cholesterol Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["chol"], bins=15, kde=True)
plt.title("Cholesterol Distribution")
plt.xlabel("Cholesterol (mg/dL)")
plt.ylabel("Number of Patients")
plt.show()

# -----------------------------
# 3. Maximum Heart Rate Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["thalch"], bins=15, kde=True)
plt.title("Maximum Heart Rate Distribution")
plt.xlabel("Maximum Heart Rate")
plt.ylabel("Number of Patients")
plt.show()

# -----------------------------
# 4. Heart Disease Distribution
# -----------------------------
plt.figure(figsize=(6,4))
ax = sns.countplot(x="num", data=df)
ax.set_xticklabels(["No Disease", "Disease"])
plt.title("Heart Disease Distribution")
plt.xlabel("Heart Disease")
plt.ylabel("Number of Patients")
plt.show()

# -----------------------------
# 5. Gender Distribution
# -----------------------------
plt.figure(figsize=(6,4))
ax = sns.countplot(x="sex", data=df)
ax.set_xticklabels(["Female", "Male"])
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.show()

# -----------------------------
# 6. Correlation Heatmap
# -----------------------------

numeric_df = df.select_dtypes(include=["number"])

correlation = numeric_df.corr()

plt.figure(figsize=(14,10))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()

# -----------------------------
# 7. Boxplot of Age
# -----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x=df["age"])
plt.title("Age Boxplot")
plt.show()

# -----------------------------
# 8. Boxplot of Cholesterol
# -----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x=df["chol"])
plt.title("Cholesterol Boxplot")
plt.show()

# -----------------------------
# 9. Boxplot of Resting Blood Pressure
# -----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x=df["trestbps"])
plt.title("Resting Blood Pressure Boxplot")
plt.show()

# -----------------------------
# 10. Scatter Plot
# Age vs Cholesterol
# -----------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="age",
    y="chol",
    hue="num",
    data=df
)
plt.title("Age vs Cholesterol")
plt.xlabel("Age")
plt.ylabel("Cholesterol")
plt.legend(["No Disease", "Disease"])
plt.show()

# -----------------------------
# 11. Pairplot
# -----------------------------
sns.pairplot(
    df,
    vars=["age", "chol", "thalch", "trestbps"],
    hue="num"
)
plt.show()