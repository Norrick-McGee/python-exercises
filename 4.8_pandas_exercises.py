from pydataset import data
import pandas as pd
import numpy as np


df = data('mpg')
#data('mpg', show_doc = True)

moneys = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

ndf = pd.DataFrame(moneys)

print(ndf)
ndf = ndf.convert_objects(convert_numeric=True)
print(ndf)
