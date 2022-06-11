from matplotlib import style
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='whitegrid')
kashti=sns.load_dataset('tips')
# print(kashti)
# x is used for horizental plot
sns.boxplot(x=kashti['total_bill'])
# y is used for vertical plot
sns.boxplot(y=kashti['total_bill'])
plt.show()