import pandas as pd
import matplotlib.pyplot as plt

college = pd.read_csv('../data/College.csv')
college = college.rename({'Unnamed: 0': 'College'}, axis=1)
college = college.set_index('College')

# (f)
print(college['Top10perc'].describe())
college['Elite'] = pd.cut(
    college['Top10perc'],
    [0, 50, 100],
    labels=['No', 'Yes'],
)
print(college.head())
print(college['Elite'].value_counts())

college.boxplot(column='Outstate', by='Elite')
plt.show()

# (g)
fig, axes = plt.subplots(2, 2, figsize=(8, 8))
axes[0, 0].hist(college['Apps'])
axes[0, 0].set_title('Apps')
axes[0, 1].hist(college['Room.Board'], bins=15)
axes[0, 1].set_title('Room.Board')
axes[1, 0].hist(college['Personal'], bins=5)
axes[1, 0].set_title('Personal')
axes[1, 1].hist(college['S.F.Ratio'], bins=21)
axes[1, 1].set_title('S.F.Ratio')
plt.show()

# (h)
# skipped for now