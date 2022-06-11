from matplotlib import style
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='whitegrid')
kashti=sns.load_dataset('titanic')
# print(kashti)
sns.boxplot(x='class',y='fare',data=kashti)
plt.show()
