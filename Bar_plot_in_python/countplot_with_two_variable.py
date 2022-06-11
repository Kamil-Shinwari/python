import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='ticks',color_codes=True)
titanic=sns.load_dataset('titanic')
sns.countplot(x='sex',data=titanic,hue='class')
plt.show()