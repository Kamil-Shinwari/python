from matplotlib import style
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='whitegrid')
kashti=sns.load_dataset('tips')
# print(kashti)
sns.boxplot(x='sex',y='total_bill',data=kashti)
plt.show()