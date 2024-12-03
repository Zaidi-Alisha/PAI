import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Path to the uploaded file
file_path = '/mnt/data/Iris.csv'

# Load the dataset
df = pd.read_csv(r"#file path")
print(df.head())

#Statistical analysis
# Drop the 'Id' column
df = df.drop(columns=['Id'])

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Mean of Sepal Length
mean_sepal_length = df['SepalLengthCm'].mean()
print("\nMean of Sepal Length:", mean_sepal_length)

# Median of Sepal Width
median_sepal_width = df['SepalWidthCm'].median()
print("Median of Sepal Width:", median_sepal_width)

# Mode of Sepal Length
mode_sepal_length = df['SepalLengthCm'].mode()[0]
print("Mode of Sepal Length:", mode_sepal_length)

# Variance and Standard Deviation of selected columns
variance_sepal_length = df['SepalLengthCm'].var()
std_dev_sepal_length = df['SepalLengthCm'].std()

variance_petal_width = df['PetalWidthCm'].var()
std_dev_petal_width = df['PetalWidthCm'].std()

print("\nVariance of Sepal Length:", variance_sepal_length)
print("Standard Deviation of Sepal Length:", std_dev_sepal_length)

print("\nVariance of Petal Width:", variance_petal_width)
print("Standard Deviation of Petal Width:", std_dev_petal_width)


# Lineplot of Sepal Length across IDs
plt.plot(df['Id'], df['SepalLengthCm'], label='Sepal Length')
plt.title("Lineplot of Sepal Length")
plt.xlabel("Id")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

#Histogram
plt.hist(df['SepalLengthCm'], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

#Scatter plot
plt.scatter(df['SepalLengthCm'], df['PetalLengthCm'], c='blue', alpha=0.6)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()

#Pie chart
species_counts = df['Species'].value_counts()
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Iris Species")
plt.show()

#Box plot
sns.boxplot(x='Species', y='SepalLengthCm', data=df)
plt.title("Box Plot of Sepal Length by Species")
plt.show()

#Violin Plot
sns.violinplot(x='Species', y='PetalWidthCm', data=df)
plt.title("Violin Plot of Petal Width by Species")
plt.show()

#Heat map
correlation_matrix = df.iloc[:, 1:-1].corr()  # Exclude 'Id' and 'Species'
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Heatmap of Feature Correlations")
plt.show()

#Bar chart
species_mean = df.groupby('Species')['SepalLengthCm'].mean()
species_mean.plot(kind='bar', color=['lightcoral', 'gold', 'lightblue'])
plt.title("Average Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Sepal Length (cm)")
plt.show()

#Pair plot
sns.pairplot(df, hue='Species', diag_kind='kde', palette='bright')
plt.show()

