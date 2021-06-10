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
n