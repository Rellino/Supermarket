#%%
import numpy as np
import pandas as pd 
import datetime
# %%[markdown]
# ![Markov-Chains]('supermarkt.png')
### Fruit:0, Spices:1, Dairy:2, Drinks:3, Checkout:4 

#%%
mon = pd.read_csv('/Week8/wk08_coll_project/data/monday.csv', sep=';', parse_dates=True, index_col="timestamp")
mon


# %%
# giving the state name and their respective number in a dictionary
state = {
    0 : "Fruit",
    1 : "Spices",
    2 : "Dairy",
    3 : "Drinks",
    4 : "Checkout"
}
state
# %%
# Transition Matrix
# A = np.array([[probabilty for fruits, probability for spices, and so on]]) -> each state should have 5 elements array

#%%
# Random walk on Markov-Chain
n = 15
start_state = 0 # we can change the state
print(state[start_state], "---->", end = " ") 
prev_state = start_state

while n-1:
    curr_state = np.random.choice([0,1,2,3,4], p=A[prev_state])
    print(state[curr_state], "---->", end = " "))
    prev_state = curr_state
    n-=1
print('stop') 

#%%[markdown]
### Approach 1 : Monte Carlo -> Finding the Staionary state
