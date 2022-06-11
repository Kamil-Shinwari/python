from matplotlib import style
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='whitegrid')
kashti=sns.load_dataset('tips')
# print(kashti)
# saturation is used for color intensity 0=black,1=white, 0-1 for diffrent grey shade
sns.boxplot(x='sex',y='total_bill',data=kashti,saturation=1)
plt.show()