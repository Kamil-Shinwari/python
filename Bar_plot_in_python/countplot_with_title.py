import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='ticks',color_codes=True)
titanic=sns.load_dataset('titanic')
p=sns.countplot(x='sex',data=titanic,hue='class')
p.set_title('my first plot')
plt.show()