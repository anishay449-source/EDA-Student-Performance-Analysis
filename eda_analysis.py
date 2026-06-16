import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_d.csv")

# Basic Information
print("Dataset Shape:")
print(df.shape)

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Correlation Matrix
correlation = df.corr()
print("\nCorrelation Matrix:")
print(correlation)

# Correlation Heatmap
plt.figure(figsize=(8,6))
plt.imshow(correlation, cmap='coolwarm')
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# Hours Studied vs Final Score
plt.figure(figsize=(6,4))
plt.scatter(df["Hours_Studied"], df["Final_Score"])
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.title("Hours Studied vs Final Score")
plt.savefig("hours_vs_score.png")
plt.show()

# Attendance Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Attendance"], bins=5)
plt.xlabel("Attendance")
plt.ylabel("Frequency")
plt.title("Attendance Distribution")
plt.savefig("attendance_distribution.png")
plt.show()

# Final Score Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Final_Score"], bins=5)
plt.xlabel("Final Score")
plt.ylabel("Frequency")
plt.title("Final Score Distribution")
plt.savefig("score_distribution.png")
plt.show()