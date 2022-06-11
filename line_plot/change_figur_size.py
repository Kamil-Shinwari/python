import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(6,2))
# import data set
flower=sns.load_dataset('iris')
# print(flower)
sns.lineplot(x='sepal_length',y='sepal_width',data=flower)
plt.title('flower data with xlimt and ylimt specified')

plt.show()