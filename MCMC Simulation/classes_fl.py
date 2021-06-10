""" 
random a uno dei settori
class for the Supermarcket: gestire tutto entrata movimento e uscita uscita finale alla chiusura 
class for the customers minuto per minito la posizione
"""
#%%

#built-in libraries
import datetime as dt

#import other libraries
import numpy as np
import pandas as pd
from faker import Faker

#import scripts 
import proba


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
        return f'<Customer {self.name} is in {self.state}>'


    def first_state(self):
        '''
        Sets the first aile for set customer
        Returns nothing.
        '''
        self.state = np.random.choice(['spices', 'drinks', 'fruit', 'dairy'], p=proba.ent_prob)

    def next_state(self):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        #WARNING: CHECK THE ORDER OF THE AISLES WHEN THE ACTUAL MATRIX ARRIVES
        aisles = ['checkout','dairy','drinks','fruit','spices']

        if self.state in aisles:
        
            if self.state == 'dairy':
                initial_state = np.array([0.0,1.0,0.0,0.0,0.0])
            elif self.state == 'drinks':
                initial_state = np.array([0.0,0.0,1.0,0.0,0.0])
            elif self.state == 'fruit':
                initial_state = np.array([0.0,0.0,0.0,1.0,0.0])
            elif self.state == 'spices':
                initial_state = np.array([0.0,0.0,0.0,0.0,1.0])
            elif self.state == 'checkout':
                initial_state = np.array([1.0,0.0,0.0,0.0,0.0])
            
            next_state_prob = np.dot(initial_state,proba.prob)
            
            self.state = np.random.choice(aisles, p=next_state_prob)
        
        else:
            self.state = np.random.choice(['spices', 'drinks', 'fruit', 'dairy'], p=proba.ent_prob)
    
    def is_active(self):
        """Returns True if the customer has not reached the checkout yet."""
        if self.state == 'checkout':
            return False
        else:
            return True


# #%%

# cust1 = Customer("Jake", budget=50)
# cust2 = Customer("Margaret", "spices")

# print(cust1.name, cust1.state)
# print(cust2.name, cust2.budget)

# print(cust1)
# cust1.is_active()

# # %%
# cust1.first_state()
# #print(cust1.state)
# print(cust1)
# #%%
# for i in range(20):
#     cust1.next_state()
#     print(cust1)


#%%

class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self):        
        '''a list of Customer objects'''
        self.customers = []
        self.minutes = 0
        self.last_id = 0

    def __repr__(self):
        return ''

    def get_time(self):
        """current time in HH:MM format,
        """
        return None

    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        return None

    def next_minute(self):
        """propagates all customers to the next state.
        """
        return None
    
    def add_new_customers(self):
        """randomly creates new customers.
        """
        return None

    def remove_exitsting_customers(self):
        """removes every customer that is not active any more.
        """
        return None



#%%

if __name__ == "__main__":
    s = SuperMarket()

    tieme_counter = 
    while True:
        
        s.entrance/start 

        if len(s.clients) > 0:
            s.move()
        else:
            print('is closed')
        
        ....

#%%
#TIME COUNTER
#today = dt.date.today()
#counter = dt.datetime(today.year,today.month,today.day,7)
#counter = counter + dt.timedelta(minutes=1)  # aggiunge un minuto
#print(counter)
#print(f'0{counter.hour}:0{counter.minute}')


#customers that enter
#int(behzad.entrance_number.loc['07:04:00'])

#Name faker
f = Faker()
nm = f.name()
nm

# %%
