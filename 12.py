#import datetime
# from datetime import datetime
# print(datetime.datetime.now())
# import numpy as np
# matrix = np.matrix([[0.9,0.075,0.025],[0.15,0.8,0.05],[0.25,0.25,0.5]],dtype=float)
# vector1 = np.matrix([[0.3,0.4,0.3]],dtype=float)
# for i in range (100):
#     vector1 = vector1*matrix
#     print ("Current round:",i+1)
#     print (vector1)
# matrix = np.matrix([[0.9,0.075,0.025],[0.15,0.8,0.05],[0.25,0.25,0.5]], dtype=float)
# vector1 = np.matrix([[0.7,0.1,0.2]], dtype=float)
# for i in range(100):
#     vector1 = vector1*matrix
#     print ("Current round:" , i+1)
#     print (vector1)
from datetime import datetime
# a = datetime.now()
a=(datetime.now().strftime('%b-%d-%Y %H:%M:%S'))
dates = a.astype(datetime)
print(dates)