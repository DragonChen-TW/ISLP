import pandas as pd
import matplotlib.pyplot as plt

# (a)
college = pd.read_csv('../data/College.csv')
print(college)

# (b)
college2 = pd.read_csv('data/College.csv', index_col=0)
college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
college3 = college3.set_index('College')
print(college2)
print(college3)

college = college3

# (c)
print(college.describe())

# (d)
pd.plotting.scatter_matrix(college[['Top10perc', 'Apps', 'Enroll']])
plt.show()

# (e)
college.boxplot(column='Outstate', by='Private')
plt.show()