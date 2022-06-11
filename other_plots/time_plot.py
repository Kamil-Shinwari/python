import imp


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
dots=sns.load_dataset('dots')
# print(dots)
sns.relplot(data=dots,x='time',y='firing_rate',hue='coherence',size='choice')
plt.show()