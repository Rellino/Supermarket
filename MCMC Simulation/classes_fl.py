""" 
random a uno dei settori
class for the Supermarcket: gestire tutto entrata movimento e uscita uscita finale alla chiusura 
class for the customers minuto per minito la posizione
"""
#%%
import datetime as dt
import numpy as np
import pandas as pd
import probs

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


#%%
class SuperMarket:

    def __init__(self):
        self.clients = []

    def enter(self, client):
        self.clients.append(client)
        print('f{client.name} has entered Rewe')

    def next_min(self):
        for a in self.animals:
            a.next_min()

    def all_out(self):

#%%

# Supermarket_start

#class Supermarket:
    #"""manages multiple Customer instances that are currently in the market.
    #"""

    #def __init__(self):        
        # a list of Customer objects
        #self.customers = []
       # self.minutes = 0
        #self.last_id = 0

    #def __repr__(self):
        #return ''

    #def get_time(self):
        #"""current time in HH:MM format,
        #"""
        #return None

    #def print_customers(self):
        #"""print all customers with the current time and id in CSV format.
        #"""
        #return None

    #def next_minute(self):
        #"""propagates all customers to the next state.
        #"""
        #return None
    
    #def add_new_customers(self):
        #"""randomly creates new customers.
        #"""
        #return None

    #def remove_exitsting_customers(self):
        #"""removes every customer that is not active any more.
        #"""
        #return None



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