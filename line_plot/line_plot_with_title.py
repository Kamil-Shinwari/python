import seaborn as sns
import matplotlib.pyplot as plt
# import data set
flower=sns.load_dataset('iris')
# print(flower)
sns.lineplot(x='sepal_length',y='sepal_width',data=flower)
plt.title('flower line plot')
plt.show()