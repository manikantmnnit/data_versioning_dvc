import pandas as pd
import numpy as np
import os

import pandas as pd
import numpy as np
import os

df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')

df = df.dropna()
df = df.drop(['Email', 'Address', 'Avatar'], axis=1)
df = df[df['Length of Membership'] > 1]

df.to_csv('data/data_v1.csv', index=False)