#%%
""" 
    Transition Matrix with checkout,
    Random probability calulator for entrance,
    and function for getting the number of customer per minute.
"""

#%%
import pandas as pd 
import numpy as np

#%%
# loading the cleaned data that was built in EDA.ipynb file
df = pd.read_csv('data/cleaned_up/clean_final.csv', index_col=0)

#%% [markdown]
### Building Transition Matrix
#%%
# adding next location column 
df['next_location'] = df['location'].shift(-1)
# frequency table for number of customers in each state
df.groupby('location')['next_location'].value_counts().unstack()
# leaving the 'checkout' rows from location to be able to add the 'absorbing state' later on
df_1 = df[df['location'] != 'checkout'].copy()
# probability table without checkout in location
trans_without_checkout= pd.crosstab(df_1['location'], df_1['next_location'], normalize=0)
# Hardcoding the absorbing state into transition matrix
prob = np.array([1.0,0.0,0.0,0.0,0.0,
                0.138084,0.330109,0.186343,0.232072,0.113392,
                0.143430,0.326136,0.183015,0.232778,0.114641,
                0.127124,0.334015,0.173851,0.246696,0.118313,
                0.131730,0.329882,0.174737,0.239726,0.123925
                ]).reshape(5,5)
trans_matrix = pd.DataFrame(prob,columns=['checkout','dairy','drinks','fruit','spices'],
                index=['checkout','dairy','drinks','fruit','spices'])

#%%
# random probability for entrance (for visualization purposes)
entrance = np.identity(1)
# Add a random drift term.  We can guarantee that the diagonal terms
entrance = entrance + np.random.uniform(low=0. , size=(1, 4))
# Lastly, divide by row-wise sum to normalize to 1.
entrance = entrance / entrance.sum(axis=1, keepdims=1)

#%%
# dataframe with the time and average number of daily customers entering the supermarket per minute
entrance_number = (round(
    df[df["section_order"] == "first"]
    .groupby(["time"])[["cust_id"]]
    .count()
    / 5, 0)
)

#%%
def get_customer_number(time):

    ''' 
        Given the time in string format 'HH:MM:SS',
        return the number of customer enter to the supermarket.
    '''
    for row, number in zip(entrance_number.index, entrance_number['cust_id']):
        if row == time:
            return(number)
        else:
            return('Supermarket is closed') 



