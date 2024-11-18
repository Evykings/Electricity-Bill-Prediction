# -*- coding: utf-8 -*-
"""Bedc.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BBEBV9m0lxLw_Z1DGl5y_GVYIgfuZknM
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import SGDRegressor, LinearRegression

#define functions 
def style_negative(v, props=''):
    "'' Style negative values in dataframe""" 
    try:
        return props if v < 0 else None 
    except:
        pass
def style_positive(v, props=''):
    "''Style positive values in dataframe""" 
    try:
        return props if v > 0 and v < 100 else None 
    except:
        pass

# Loading the dataset into python
df = pd.read_excel('bedcdataset.xlsx')



# let's list all categorical features
categorical_columns= ['displaycode', 'tariffclassname', 'updateddssname']
# let's get the categories and their count for each feature
for col in categorical_columns:
  print(f"Categories and number of occurrences for '{col}'")
  print(df[col].value_counts())
  print()



# printing all the missing values
print("Missing Data:\n",df.isnull().sum())



# Droping all rows with missing values
df = df.dropna(subset=["tariffclassname", "tariffrates", "readconsumption", "energycharges", "updateddssname"])

# Checking the numbers of missing values again
print("Missing Data:\n",df.isnull().sum())



# Filling all missing values with 0
df = df.fillna(0)

print("Missing Data:\n",df.isnull().sum())


dfc = df.copy()
dfc = dfc.drop_duplicates()
dff = df.copy()

# Summary statistics for numerical features
df.describe()



# Creating a new dataset for the numerical columns
numerical_col= df[['tariffrates','previousreading', 'presentreading', 'readconsumption', 'cap', 'energycharges', 'billedamount', 'previouspayments' ]]

median_agg = numerical_col.median()

# printing the first 10 rows of the dataset
numerical_col.head(10)

mean_diff_agg = (numerical_col - median_agg).div(median_agg)

# Get the numerical column indices from the original DataFrame 'df'
numerical_col_indices = [df.columns.get_loc(col) for col in numerical_col.columns]

# Use the numerical indices to select and modify the columns in 'dfc'
dfc.iloc[:, numerical_col_indices] = (dfc.iloc[:, numerical_col_indices] - median_agg).div(median_agg)


import seaborn as sns
correlation_matrix = numerical_col.corr()
# Set the figure size
plt.figure(figsize=(12, 8))

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

# Set the title
plt.title('Correlation Heatmap')

# Show the plot
plt.show()



# Distribution of Tariff Class
plt.figure(figsize=(15, 10))
sns.countplot(x='tariffclassname', data=df)
plt.title('Distribution count of Tariff Class')
plt.xlabel('tariffclassname')
plt.ylabel('Count')
plt.tight_layout()
plt.show()



# Customer count analysis of Distribution Substation
plt.figure(figsize=(10, 200))
sns.countplot(y='updateddssname', data=df, order=df['updateddssname'].value_counts().index)
plt.title('Distribution Substation Customer count')
plt.show()



# Plotting Energy Charges vs Tariff Class
plt.figure(figsize=(15, 10))
plt.bar(df['tariffclassname'], df['energycharges'])
plt.xlabel('tariffclassname')
plt.ylabel('energycharges')
plt.title('updateddssname vs tariffclassname')
plt.show()

 

# Dataset to filter different Distribution Substation (DSS) names
df_filtered = df[df['updateddssname']=='AMENZE']





# Set up bar width and positions
bar_width = 0.2
x = np.arange(len(df_filtered))
y = [i+bar_width for i in x]

# Plot Stacked Bar Chart
fig, ax = plt.subplots(figsize=(15, 10))

# Plot Previous Payments
ax.bar(x, df_filtered['previouspayments'], bar_width, label='Previous Payments', color='skyblue')

# Plot Billed amount
ax.bar(y, df_filtered['billedamount'], bar_width,  label='Billed Amount', color='salmon')

# Labeling and Formatting
ax.set_xlabel('Customer Account Number')
ax.set_ylabel('Amount')
ax.set_title('Customer Payment Behavior: Billed vs. Payments Made')
ax.set_xticks(x)
ax.set_xticklabels(df_filtered['globalaccountnumber'])
#ax.set_yticklabels(df_filtered['billedamount'])
ax.legend()

# Display plot
plt.tight_layout()
plt.show()



# Scatter plot to show the relationship between readconsumption and billedamount
plt.scatter(df['readconsumption'], df['billedamount'], vmin=0, vmax=100, cmap='rainbow')
plt.xlabel('Read Consumption')
plt.ylabel('Billed Amount')
plt.title('readconsumption vs billedamount')
plt.show()

# Scatter plot for Billed Amount and Energy Charges
sns.set_style('darkgrid')
plt.scatter(df['energycharges'], df['billedamount'], vmin=0, vmax=100, cmap='rainbow')
plt.xlabel('Energy Charges')
plt.ylabel('Billed Amount')
plt.title('Energy Charges vs Billed Amount')
plt.show()



# Scatter plot for Billed Amount and Read Consuption for a particular Distribution Substation

plt.scatter(df_filtered['readconsumption'], df_filtered['billedamount'], vmin=0, vmax=100, cmap='rainbow')
plt.xlabel('Read Consumption')
plt.ylabel('Billed Amount')
plt.title('Read Consumption vs Billed Amount')
plt.show()

sns.set_style('darkgrid')
plt.scatter(df_filtered['energycharges'], df_filtered['billedamount'], vmin=0, vmax=100, cmap='rainbow')
plt.xlabel('Energy Charges')
plt.ylabel('Billed Amount')
plt.title('Energy Charges vs Billed Amount')
plt.show()



# define the transformation
ct_cat = ColumnTransformer(
    [
        (
            "onehot_categorical", # --> name of the transformation
            OneHotEncoder(sparse_output=False, handle_unknown='ignore'), # --> main function to apply
            categorical_columns, #-->columns to apply it to
        ),
    ],
    remainder="passthrough", #--> what to do with the non-transformed columns. passthrough=keep them
    verbose_feature_names_out=False
)

# the output is an ARRAY with the encoded columns.
encoded_array= ct_cat.fit_transform(df)

# What if we want a dataframe back? We can combine the array with the info about
# the column names stored in ct.get_feature_names_out()
encoded_col_names= ct_cat.get_feature_names_out()
print(encoded_col_names)

df= pd.DataFrame(encoded_array, columns=encoded_col_names)

print()
print(df.head(5))



# Out target feature is the Billed Amount
X = df.drop('billedamount', axis=1)
y = df['billedamount']

print (X.shape)
print (y.shape)

print (y.head(5))

# separating of training and testing set: 80-20 separation
# random_state parameter is given to keep the same randomised splitting: important when you are creating the model
# and want to keep a specific separation across multiple runs.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    shuffle= True, random_state=42)

# initialise an instance of a linear regression model
lr = SGDRegressor()
lr.fit(X_train, y_train) # train the model on our training dataset
print('this is the training data')
print(X_train)



from sklearn.metrics import mean_squared_error, r2_score

# model evaluation for training set
# get the predictions
y_train_predict = lr.predict(X_train)
# compare predicted and true labels using the RMSE performance metrics.
rmse = np.sqrt(mean_squared_error(y_train, y_train_predict))
r2 = r2_score(y_train, y_train_predict)

print("Training SET")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))



# model evaluation for testing set
y_test_predict = lr.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_test_predict))


print("\nTesting SET")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))

from scipy.stats import norm

_ = plt.figure(figsize=(10, 5))

ax1 = plt.subplot(121)
_ = ax1.scatter(y_train, y_train_predict)
_ = ax1.set_title('Scatter plot: training set estimation')
_ = ax1.set_xlabel('Billed Amount (target)')
_ = ax1.set_ylabel('Billed Amount (predicted)')

ax2 = plt.subplot(122)
_ = ax2.scatter(y_test, y_test_predict)
_ = ax2.set_title('Scatter plot: test set estimation')
_ = ax2.set_xlabel('Billed Amount (target)')
_ = ax2.set_ylabel('Billed Amount (predicted)')


plt.tight_layout()
plt.show()

# Let's keep working with X_train and X_test from before.
learning_rates_to_try = [0.000001, 0.00001, 0.0001, 0.0002, 0.0005, 0.0007] #...] #how many do you want to try?

# Your turn now! Reimplement the above in a for loop, store all the results and take the maximum
all_results = []

# your code here
# I'll get you started with the structure
#for loop

# create and train model: remember that the argument to change is called eta0

# predict labels

# evaluate and store results

for i, e0 in enumerate(learning_rates_to_try):
    lr = SGDRegressor(learning_rate= 'constant', eta0= e0)
    lr.fit(X_train, y_train)
    y_test_predict = lr.predict(X_test)
    r2 = r2_score(y_test, y_test_predict)
    all_results.append(r2)

plt.plot(np.log10(learning_rates_to_try), all_results, '-x')



add_sidebar = st.sidebar.selectbox("Aggregate or Individual Substation", ("Aggregate Metrics For The Region","Individual Distribution Substation Analysis"))



if add_sidebar == 'Aggregate Metrics For The Region':
    st.metric('Previous Payment', median_agg['previouspayments'], delta = "{:.2%}".format((median_agg['previouspayments'] - 13999.86)/13999.86))
    st.metric('Billed Amount', median_agg['billedamount'], delta = "{:.2%}".format((median_agg['billedamount'] - 13999.86)/13999.86))
    st.metric('Emergy Charge', median_agg['energycharges'], delta = "{:.2%}".format((median_agg['energycharges'] - 13999.86)/13999.86))
    st.metric('Read Consumption', median_agg['readconsumption'])
    
    df_agg_diff_final = dfc.loc[:,['globalaccountnumber','energycharges','billedamount','previouspayments','updateddssname']]

    # Get the numerical column names from df_agg_diff_final
    numerical_cols = ['globalaccountnumber','energycharges', 'billedamount', 'previouspayments']  

    # Get the numerical column indices from df_agg_diff_final
    numerical_col_indices = [df_agg_diff_final.columns.get_loc(col) for col in numerical_cols if col in df_agg_diff_final.columns]

    # Apply styling
    
    st.dataframe(df_agg_diff_final.iloc[:, numerical_col_indices].style.applymap(style_negative, props='color:red;').applymap(style_positive, props='color:green;'))

if add_sidebar == 'Individual Distribution Substation Analysis':    
    dss = tuple(dff['updateddssname'])
    dssselect = st.selectbox('Select the Distribution Substation (dss) for your Analysis', dss)
    dss_filter = dff[dfc['updateddssname'] == dssselect]
    st.metric('Customers Count', dss_filter['updateddssname'].count())
    st.dataframe(dss_filter)
    
    dss_filter = dss_filter.set_index('globalaccountnumber')
    st.bar_chart(dss_filter['previouspayments'], x_label= 'Customers', y_label= 'Previous Payment')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    