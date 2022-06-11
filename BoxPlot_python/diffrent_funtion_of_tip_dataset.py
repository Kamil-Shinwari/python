from matplotlib import style
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
kashti=sns.load_dataset('tips')
# describe function will show all mean of bills, tip ,min,max etc
print(kashti.describe())
