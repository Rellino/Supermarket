""" 
random a uno dei settori
class for the Supermarcket: gestire tutto entrata movimento e uscita uscita finale alla chiusura 
class for the customers minuto per minito la posizione
"""


#built-in libraries
import datetime as dt
import time

#import other libraries
import numpy as np
import pandas as pd
from faker import Faker

#import scripts 
import proba


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
        return f'{self.name} is in {self.state}.'


    # def first_state(self):
    #     '''
    #     Sets the first aile for set customer
    #     Returns nothing.
    #     '''
    #     self.state = np.random.choice(['spices', 'drinks', 'fruit', 'dairy'], p=proba.ent_prob)

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



class SuperMarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self):        
        '''a list of Customer objects'''
        self.customers = []
        self.minutes = dt.datetime(today.year,today.month,today.day,6,50)
        #self.last_id = 0
        self.state = 'closed'

    def __repr__(self):
        return f'{self.minutes} – The supermarket is {self.state}: currently, there are {len(self.customers)} customers inside.'

    def get_time(self):
        """opens and closes the supermarket,
        and pushes customers to the checkout,
        """
        if self.minutes.hour >= 22 or self.minutes.hour <= 6 and self.minutes.minute <= 59:
            print(f'{self.minutes} - The supermarket is closed. It will reopen at 7 AM.')
            self.state = 'closed'
        elif self.minutes.hour == 21 and self.minutes.minute == 57:
            for cust in self.customers:
                if cust.is_active() == True:
                    cust.state = 'checkout'
                    #print(f'{self.minutes} – {cust}')
        elif self.minutes.hour == 7 and self.minutes.minute == 0:
            print(f'{self.minutes} - The supermarket has opened!')
            self.state = 'open'
        else:
            self.state = 'open'

        return None

    def add_new_customers(self):
        """generate new customers at their initial location based on the fluxes illustrated in the EDA.
        """
        if self.minutes.hour >= 22 or self.minutes.hour <= 6 and self.minutes.minute <= 59:
            pass
        else:
            tm = str(self.minutes)[-8:]
            try:
                cust_no = int(proba.entrance_number.loc[tm])
            except:
                cust_no = 0
            for cust in range(cust_no):
                c = Customer(f.name())
                print(f'{self.minutes} - {c.name} has entered the supermarket.')
                self.customers.append(c)

        return None

    
    def next_minute(self):
        """increase the time of the supermarket by one minute,
        propagates all customers to the next state.
        """
        self.minutes = self.minutes + dt.timedelta(minutes=1)
        for cust in self.customers:
            cust.next_state()
            print(f'{self.minutes} – {cust}')

        return None
    
    
    def remove_exiting_customers(self):
        """removes every customer that is not active any more.
        """
        for cust in self.customers:
            if cust.is_active() == False:
                print(f'{self.minutes} - {cust.name} has left the supermarket.')
                self.customers.remove(cust)

        return None

    def record_customers(self):
        """append the state of different customers to a log DataFrame.
        """
        df = pd.DataFrame(columns=['time','customer','location'])
        for cust in self.customers:
            if cust.state == 'checkout':
                final_st = 'checkout and leave'
            else:
                final_st = cust.state
            row = pd.DataFrame(data=[str(self.minutes)[-8:],cust.name,final_st], index=['time','customer','location']).transpose()
            df = pd.concat([df,row], ignore_index=True)

        return df 



if __name__ == "__main__":
    #output DataFrame
    record = pd.DataFrame(columns=['time','customer','location'])

    #Name faker
    today = dt.date.today()
    f = Faker()
    s = SuperMarket()

    #Loop
    for i in range(100):
        s.get_time()
        s.add_new_customers()
        df = s.record_customers()
        record = pd.concat([record,df], ignore_index=True)
        s.remove_exiting_customers()
        s.next_minute()
        
        #time.sleep(0.5)

#output file
record.to_csv('output/MCMC_sim_log.csv',sep=';')
    