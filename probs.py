
import pandas as pd
import numpy as np


prob = np.array([0.102930,0.736824,0.058777,0.049947,0.051521,
                0.215608,0.010899,0.598602,0.087909,0.086983,
                0.201149,0.095972,0.054830,0.597310,0.050739,
                0.150048,0.193533,0.163428,0.090953,0.402039]).reshape(4,5)


prob_df = pd.DataFrame(prob,columns=['checkout','dairy','drinks','fruit','spices'],
                index=['dairy','drinks','fruit','spices'])

ent_prob = np.array([0.287576, 0.153526, 0.377435, 0.18146])
ent_prob_df = pd.DataFrame(ent_prob, index=['dairy', 'drinks', 'fruit', 'spices'], columns=['prob_location'])
ent_prob_df