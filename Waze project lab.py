#!/usr/bin/env python
# coding: utf-8

# # **Waze Project**
# **Course 2 - Get Started with Python**

# Welcome to the Waze Project!
# 
# Your Waze data analytics team is still in the early stages of their user churn project. Previously, you were asked to complete a project proposal by your supervisor, May Santner. You have received notice that your project proposal has been approved and that your team has been given access to Waze's user data. To get clear insights, the user data must be inspected and prepared for the upcoming process of exploratory data analysis (EDA).
# 
# A Python notebook has been prepared to guide you through this project. Answer the questions and create an executive summary for the Waze data team.

# # **Course 2 End-of-course project: Inspect and analyze data**
# 
# In this activity, you will examine data provided and prepare it for analysis. This activity will help ensure the information is,
# 
# 1.   Ready to answer questions and yield insights
# 
# 2.   Ready for visualizations
# 
# 3.   Ready for future hypothesis testing and statistical methods
# <br/>
# 
# **The purpose** of this project is to investigate and understand the data provided.
# 
# **The goal** is to use a dataframe contructed within Python, perform a cursory inspection of the provided dataset, and inform team members of your findings.
# <br/>
# 
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation
# * How can you best prepare to understand and organize the provided information?
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning, future exploratory data analysis (EDA), and statistical activities
# 
# * Compile summary information about the data to inform next steps
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into variables
# 
# 
# <br/>
# 
# Follow the instructions and answer the following questions to complete the activity. Then, you will complete an Executive Summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work.
# 
# 

# # **Identify data types and compile summary information**
# 

# <img src="images/Pace.png" width="100" height="100" align=left>
# 
# # **PACE stages**

# Throughout these project notebooks, you'll see references to the problem-solving framework, PACE. The following notebook components are labeled with the respective PACE stages: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## **PACE: Plan**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:

# ### **Task 1. Understand the situation**
# 
# *   How can you best prepare to understand and organize the provided driver data?
# 
# 
# *Begin by exploring your dataset and consider reviewing the Data Dictionary.*

# ==> ENTER YOUR RESPONSE HERE

# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## **PACE: Analyze**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### **Task 2a. Imports and data loading**
# 
# Start by importing the packages that you will need to load and explore the dataset. Make sure to use the following import statements:
# 
# *   `import pandas as pd`
# 
# *   `import numpy as np`
# 

# In[3]:


# Importing packages for data manipulation

import pandas as pd
import numpy as np


# Then, load the dataset into a dataframe. Creating a dataframe will help you conduct data manipulation, exploratory data analysis (EDA), and statistical activities.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[4]:


# Loading dataset into dataframe

df = pd.read_csv('waze_dataset.csv')


# ### **Task 2b. Summary information**
# 
# View and inspect summary information about the dataframe by **coding the following:**
# 
# 1.   df.head(10)
# 2.   df.info()
# 
# *Consider the following questions:*
# 
# 1. When reviewing the `df.head()` output, are there any variables that have missing values?
# 
# 2. When reviewing the `df.info()` output, what are the data types? How many rows and columns do you have?
# 
# 3. Does the dataset have any missing values?

# In[8]:


# Checking if any variables that have missing values
df.head(10)

''' -> found out that none of the variables have missing values '''


# In[6]:


# Checking what are the data types/how many rows and columns/for any missing values
df.info()

''' -> there are float64(3), int64(8), object(2) with total of 14999 rows and 13 columns and there is 700 missing value in column label (has only 14299)'''


# 1. None of the variables have missing values. 
# 2. There is float64(total_sessions, driven_km_drives, duration_minutes_drives), int64(ID, sessions, drives, n_days-after_onboarding, total_navigations_fav1, total_navigations_fav2, activity_days, driving_days), object(label, device), and total of 14999 rows and 13 columns
# 3. Yes, there is 700 missing value in column label (has only 14299)

# ### **Task 2c. Null values and summary statistics**
# 
# Compare the summary statistics of the 700 rows that are missing labels with summary statistics of the rows that are not missing any values.
# 
# **Question:** Is there a discernible difference between the two populations?
# 

# In[9]:


# Isolating rows with null values
null_df = df[df['label'].isnull()]

# Displaying summary stats of rows with null values
null_df.describe()


# In[10]:


# Isolating rows without null values
not_null_df = df[df['label'].isnull()]

# Displaying summary stats of rows without null values
not_null_df.describe()

''' Question: Is there a discernible difference between the two populations? 
-> no, there is NOT a discernible difference between the two populations.'''


# 1. Question: Is there a discernible difference between the two populations?

# ### **Task 2d. Null values - device counts**
# 
# Next, check the two populations with respect to the `device` variable.
# 
# **Question:** How many iPhone users had null values and how many Android users had null values?

# In[11]:


# Getting count of null values by device
null_df['device'].value_counts()

'''Of the 700 rows, there is 447 iPhones users and 253 Android users with null value. '''


# 1. Of the 700 rows, there is 447 iPhones users and 253 Android users with null value. 

# Now, of the rows with null values, calculate the percentage with each device&mdash;Android and iPhone. You can do this directly with the [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html) function.

# In[13]:


# Calculating % of iPhone nulls and Android nulls
null_df['device'].value_counts(normalize=True)


# How does this compare to the device ratio in the full dataset?

# In[14]:


# Calculating % of iPhone users and Android users in full dataset
df['device'].value_counts(normalize=True)

'''There is nothing to suggest a non-random cause of the missing data.'''


# The percentage of missing values by each device is consistent with their representation in the data overall.
# 
# There is nothing to suggest a non-random cause of the missing data.

# Examine the counts and percentages of users who churned vs. those who were retained. How many of each group are represented in the data?

# In[31]:


# Calculating counts of churned vs. retained

print(df['label'].value_counts())

print(df['label'].value_counts(normalize=True))

'''This dataset contains 82% retained users and 18% churned users. -> calculate: the median and NOT the mean = not having outliers to affect the portrayal of a typical user
'''


# This dataset contains 82% retained users and 18% churned users.
# 
# Next, compare the medians of each variable for churned and retained users. The reason for calculating the median and not the mean is that you don't want outliers to unduly affect the portrayal of a typical user. Notice, for example, that the maximum value in the `driven_km_drives` column is 21,183 km. That's more than half the circumference of the earth!

# In[37]:


# Calculating median values of all columns for churned and retained users

df.groupby('label').median()


# This offers an interesting snapshot of the two groups, churned vs. retained:
# 
# Users who churned averaged ~3 more drives in the last month than retained users, but retained users used the app on over twice as many days as churned users in the same time period.
# 
# The median churned user drove ~200 more kilometers and 2.5 more hours during the last month than the median retained user.
# 
# It seems that churned users had more drives in fewer days, and their trips were farther and longer in duration. Perhaps this is suggestive of a user profile. Continue exploring!

# Calculate the median kilometers per drive in the last month for both retained and churned users.

# In[28]:


# Groupping data by `label` and calculate the medians
medians_by_label = df.groupby('label').median('driven_km_drives')

# Dividing the median distance by median number of drives
medians_by_label['driven_km_drives']/ medians_by_label['drives']


# The median user from both groups drove ~73 km/drive. How many kilometers per driving day was this?

# In[29]:


# Dividing the median distance by median number of driving days
medians_by_label['driven_km_drives'] / medians_by_label['driving_days']


# Now, calculate the median number of drives per driving day for each group.

# In[30]:


# Dividing the median number of drives by median number of driving days
medians_by_label['drives'] / medians_by_label['driving_days']


# The median user who churned drove 608 kilometers each day they drove last month, which is almost 250% the per-drive-day distance of retained users. The median churned user had a similarly disproporionate number of drives per drive day compared to retained users.
# 
# It is clear from these figures that, regardless of whether a user churned or not, the users represented in this data are serious drivers! It would probably be safe to assume that this data does not represent typical drivers at large. Perhaps the data&mdash;and in particular the sample of churned users&mdash;contains a high proportion of long-haul truckers.
# 
# In consideration of how much these users drive, it would be worthwhile to recommend to Waze that they gather more data on these super-drivers. It's possible that the reason for their driving so much is also the reason why the Waze app does not meet their specific set of needs, which may differ from the needs of a more typical driver, such as a commuter.

# Finally, examine whether there is an imbalance in how many users churned by device type.
# 
# Begin by getting the overall counts of each device type for each group, churned and retained.

# In[32]:


# For each label, calculating the number of Android users and iPhone users
df.groupby(['label', 'device']).size()


# Now, within each group, churned and retained, calculate what percent was Android and what percent was iPhone.

# In[35]:


# For each label, calculating the percentage of Android users and iPhone users
df.groupby('label')['device'].value_counts(normalize=True)


# The ratio of iPhone users and Android users is consistent between the churned group and the retained group, and those ratios are both consistent with the ratio found in the overall dataset.

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## **PACE: Construct**
# 
# **Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project.
# 
# 

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## **PACE: Execute**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:

# ### **Task 3. Conclusion**
# 
# Recall that your supervisor, May Santer, asked you to share your findings with the data team in an executive summary. Consider the following questions as you prepare to write your summary. Think about key points you may want to share with the team, and what information is most relevant to the user churn project.
# 
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
# 

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

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
