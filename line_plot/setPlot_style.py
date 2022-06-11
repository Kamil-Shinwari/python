import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style(style=None,rc=None)
# import data set
flower=sns.load_dataset('iris')
# print(flower)
sns.lineplot(x='sepal_length',y='sepal_width',data=flower)
plt.title('flower data with xlimt and ylimt specified')
# plt.xlim(2)
# plt.ylim(1)
sns.set_style(style='dark')
plt.show()