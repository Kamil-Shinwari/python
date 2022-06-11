
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='ticks',color_codes=True)
titanic=sns.load_dataset('titanic')
# count plot with one variable
sns.countplot(x='sex',data=titanic)
plt.show()