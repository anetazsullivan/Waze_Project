#!/usr/bin/env python
# coding: utf-8

# # **Waze Project**
# **Get Started with Python**

# Importing packages for data manipulation
import pandas as pd
import numpy as np


# Loading dataset into dataframe
df = pd.read_csv('waze_dataset.csv')


# Checking if any variables that have missing values
df.head(10)

''' None of the variables have missing values '''



# Checking what are the data types/how many rows and columns/for any missing values
df.info()

''' There are float64(3), int64(8), object(2) with total of 14999 rows and 13 columns and there is 700 missing value in column label (has only 14299)'''

# **Question:**
# 1. When reviewing the `df.head()` output, are there any variables that have missing values?
# 2. When reviewing the `df.info()` output, what are the data types? How many rows and columns do you have?
# 3. Does the dataset have any missing values?

# **Answers:**
# 1. None of the variables have missing values. 
# 2. There is float64(total_sessions, driven_km_drives, duration_minutes_drives), int64(ID, sessions, drives, n_days-after_onboarding, total_navigations_fav1, total_navigations_fav2, activity_days, driving_days), object(label, device), and total of 14999 rows and 13 columns
# 3. Yes, there is 700 missing value in column label (has only 14299)

 
# Comparing the summary statistics of the 700 rows that are missing labels with summary statistics of the rows that are not missing any values.

# Isolating rows with null values
null_df = df[df['label'].isnull()]


# Displaying summary stats of rows with null values
null_df.describe()


# Isolating rows without null values
not_null_df = df[df['label'].isnull()]


# Displaying summary stats of rows without null values
not_null_df.describe()



# Getting count of null values by device
null_df['device'].value_counts()



# Calculating % of iPhone nulls and Android nulls
null_df['device'].value_counts(normalize=True)



# **Question:**
# Is there a discernible difference between the two populations?
# How many iPhone users had null values and how many Android users had null values?
# How does this compare to the device ratio in the full dataset


# **Answer:**
# There is NOT a discernible difference between the two populations.
# Of the 700 rows, there is 447 iPhones users and 253 Android users with null value.
# There is nothing to suggest a non-random cause of the missing data.




# Calculating % of iPhone users and Android users in full dataset
df['device'].value_counts(normalize=True)




# Calculating counts of churned vs. retained

print(df['label'].value_counts())
print(df['label'].value_counts(normalize=True))

# This dataset contains 82% retained users and 18% churned users. -> calculate: the median and NOT the mean = not having outliers to affect the portrayal of a typical user





# Calculating median values of all columns for churned and retained users
df.groupby('label').median()



# Groupping data by `label` and calculate the medians
medians_by_label = df.groupby('label').median('driven_km_drives')



# Dividing the median distance by median number of drives
medians_by_label['driven_km_drives']/ medians_by_label['drives']



# Dividing the median distance by median number of driving days
medians_by_label['driven_km_drives'] / medians_by_label['driving_days']




# Dividing the median number of drives by median number of driving days
medians_by_label['drives'] / medians_by_label['driving_days']




# For each label, calculating the number of Android users and iPhone users
df.groupby(['label', 'device']).size()




# For each label, calculating the percentage of Android users and iPhone users
df.groupby('label')['device'].value_counts(normalize=True)





# **Conclusion**

# **Questions:**
# 
# 1. Did the data contain any missing values? How many, and which variables were affected? Was there a pattern to the missing data?
# 
# 2. What is a benefit of using the median value of a sample instead of the mean?
# 
# 3. Did your investigation give rise to further questions that you would like to explore or ask the Waze team about?
# 
# 4. What percentage of the users in the dataset were Android users and what percentage were iPhone users?
# 
# 5. What were some distinguishing characteristics of users who churned vs. users who were retained?
# 
# 6. Was there an appreciable difference in churn rate between iPhone users vs. Android users?
# 
# 
# 
# **Answers:**

# 1. Yes, in the data set were 700 values missing in 'label' column. Fortunately, there was no patern or concern about the missing values. 
# 
# 2. The benefit of using median instead of mean because median shows the middle value and doesn't have outliers so it won't skew the data. 
# 
# 3. Yes, I would like to explore more about the driver who are actually driving the most but churning the Waze app the most. 
# 
# 4. 64% of iPhone users and 36% of Android users
# 
# 5. The churned users drove farther and longer in fever days, and also used the app half as many times than retaines users. 
# 
# 6. No. 

