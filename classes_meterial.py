#%%
import random
import probs as fra
import pandas as pd
#%%
print(fra.ent_prob)
#%%
class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """
    
    def __init__(self, name, state='entrance', budget=100):
        self.name = name
        self.state = state
        self.budget = budget

    def __repr__(self):
        return f'<Customer {self.name} in {self.state}>'


    def first_state(self):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        self.state = random.choice(['spices', 'drinks', 'fruit', 'dairy'])


#%%
cust1 = Customer("Jake", budget=50)
cust2 = Customer("Margaret", "spices")

print(cust1.name, cust1.state)
print(cust2.name, cust2.budget)

print(cust1)

# %%
print(cust1.first_state())
# %%

#HARD CODING:
ent_prob = np.array([0.287576, 0.153526, 0.377435, 0.18146])
ent_prob_df = pd.DataFrame(ent_prob, index=['dairy', 'drinks', 'fruit', 'spices'], columns=['prob_location'])
ent_prob_df




# %%
