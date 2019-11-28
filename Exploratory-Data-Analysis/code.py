# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here

#Loading the data
data = pd.read_csv(path)

#Plotting histogram 
data.hist('Rating')
plt.show()

#Filtering data with ('Rating'<=5) only
data = data[data['Rating'] <= 5].copy()
#print(data.shape)
data.hist('Rating')
plt.show()

#Code ends here


# --------------
#Checking for null values
total_null = data.isnull().sum()
percent_null = total_null / data.isnull().count()

#Missing data
missing_data = pd.concat([total_null, percent_null], keys = ['Total', 'Percent'], axis = 1)
print(missing_data)

#Dropping null values
data.dropna(axis = 0, inplace = True)

total_null_1 = data.isnull().sum()
percent_null_1 = total_null_1 / data.isnull().count()

missing_data_1 = pd.concat([total_null_1, percent_null_1], keys = ['Total', 'Percent'], axis = 1)
print(missing_data_1)


# --------------
#Correlation test between Category-Ratings
box_plt = sns.catplot(x = 'Category', y = 'Rating', data = data, kind = 'box', height = 10)

plt.xticks(rotation = 90)
plt.title('Rating vs Category [Boxplot]')

plt.show()


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Displaying value counts to observe distribution
print(data.Installs.value_counts())

#Cleaning column data to convert it to int
data['Installs'] = data.apply(lambda x: x['Installs'].replace('+', ''), axis = 1)
data['Installs'] = data.apply(lambda x: int(x['Installs'].replace(',', '')), axis = 1)
print(data.Installs.value_counts())

#Label Enconding for column 'Installs

#Initialize the encoder
le = LabelEncoder()

#Transform the column data
data['Installs'] = le.fit_transform(data['Installs'])

#Plotting RegPlot
a = sns.regplot(x = 'Installs', y = 'Rating', data = data)
plt.title('Rating vs Installs [RegPlot]')


# --------------
#Display value counts to observe distribution
print(data.Price.value_counts())

#Cleaning the column data of -> 'Price'
data['Price'] = data.apply(lambda x: float(x['Price'].replace('$', '')), axis = 1)

#Plot RegPlot
sns.regplot(x = 'Price', y = 'Rating', data = data)
plt.title('Rating vs Price [RegPlot]')


# --------------
#Unique values of 'Genre' column
print(data['Genres'].unique())

#Cleaning Data for column -> 'Genre'
splitted = data['Genres'].str.split(';')
data['Genres'] = splitted.str[0]
#print(data['Genres'][:5])
print('*'*50)

#Grouping Genre and Rating by Genre
gr_mean = data.groupby(['Genres'], as_index = False)[['Rating']].mean().sort_values(by = 'Rating')

#Stastical overview of gr_mean
print(gr_mean.describe())
print('*'*50)

#Display Lowest and Highest value
print(gr_mean.head(1))
print('*'*50)
print(gr_mean.tail(1))


# --------------
print(data['Last Updated'])
print('*'*50)

#Visualize 'Last Updated'
data.plot('Last Updated')
plt.show()

#Converting 'Last Updated' to datetime format
data['Last Updated'] = pd.to_datetime(data['Last Updated'])

#Adding new column
max_date = data['Last Updated'].max()
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days

#Visualize: Regression Plot
sns.regplot(x = 'Last Updated Days', y = 'Rating', data = data)
plt.title('Rating vs Last Updated [RegPlot]')
plt.show()


