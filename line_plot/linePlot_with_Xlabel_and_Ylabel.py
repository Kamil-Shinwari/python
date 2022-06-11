import seaborn as sns
import matplotlib.pyplot as plt
# import data set
flower=sns.load_dataset('iris')
# print(flower)
sns.lineplot(x='sepal_length',y='sepal_width',data=flower)
plt.title('flower data with xlimt and ylimt specified')
plt.xlim(2)
plt.xlabel('gulab_sepal_length')
plt.ylabel('Gulab_sepal_width')
plt.ylim(1)
plt.show()