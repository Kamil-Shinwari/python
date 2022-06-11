import imp
import seaborn as sns
import matplotlib.pyplot as plt
# import dataset

kashti=sns.load_dataset('titanic')
# print(kashti)
sns.barplot(x='sex',y='adult_male',data=kashti)
plt.show()