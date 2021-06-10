""" 
random a uno dei settori
class for the Supermarcket: gestire tutto entrata movimento e uscita uscita finale alla chiusura 
class for the customers minuto per minito la posizione
"""
import datetime as dt

entrance = np.array([1, 0,0,0,0])

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



# class Zoo:

#     def __init__(self):
#         self.animals = []

#     def add(self, animal):
#         self.animals.append(animal)

#     def make_all_sounds(self):
#         for a in self.animals:
#             a.make_sound()



z = Zoo()

croc = Animal('crocodile', 'snap!')
z.add(croc)
z.add(Animal('elephant', 'toott'))
z.add(Animal('lion', 'roar'))
z.add(Dog('corgie'))




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


today = dt.date.today()
counter = dt.datetime(today.year,today.month,today.day,7)
counter = counter + dt.timedelta(minutes=1)  # aggiunge un minuto
print(counter)
print(f'0{counter.hour}:0{counter.minute}')