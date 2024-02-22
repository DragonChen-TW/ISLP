from ISLP import load_data
import pandas as pd
import matplotlib.pyplot as plt

# (a)
boston = load_data('Boston')
print(boston)

# (b)
print(boston.shape[0])

# (c)
pd.plotting.scatter_matrix(boston)
# plt.show()

# (d)
# chas, age, dis, lstat, medv might have associated with crim
# Positive: age, lstat
# Negative: chas, dis, medv

# (e)
print(boston.describe())
def df_with_high_rate(df: pd.DataFrame, col: str) -> pd.DataFrame:
    anchor = df[col].mean() + df[col].std()
    print(col, 'anchor', anchor)
    return df.loc[df[col] > anchor, col]

print(df_with_high_rate(boston, 'crim'))
print(df_with_high_rate(boston, 'tax'))
print(df_with_high_rate(boston, 'ptratio'))

# (f)
print(len(boston[boston['chas'] == 1]))

# (g)
print(boston['ptratio'].median())

# (h)
print(boston[boston['medv'] == boston['medv'].min()])
#              crim          zn       indus        chas         nox  ...         rad         tax     ptratio       lstat        medv
# count  506.000000  506.000000  506.000000  506.000000  506.000000  ...  506.000000  506.000000  506.000000  506.000000  506.000000
# mean     3.613524   11.363636   11.136779    0.069170    0.554695  ...    9.549407  408.237154   18.455534   12.653063   22.532806
# std      8.601545   23.322453    6.860353    0.253994    0.115878  ...    8.707259  168.537116    2.164946    7.141062    9.197104
# min      0.006320    0.000000    0.460000    0.000000    0.385000  ...    1.000000  187.000000   12.600000    1.730000    5.000000
# 25%      0.082045    0.000000    5.190000    0.000000    0.449000  ...    4.000000  279.000000   17.400000    6.950000   17.025000
# 50%      0.256510    0.000000    9.690000    0.000000    0.538000  ...    5.000000  330.000000   19.050000   11.360000   21.200000
# 75%      3.677083   12.500000   18.100000    0.000000    0.624000  ...   24.000000  666.000000   20.200000   16.955000   25.000000
# max     88.976200  100.000000   27.740000    1.000000    0.871000  ...   24.000000  711.000000   22.000000   37.970000   50.000000

# Compare with all the suburbs of Boston.
# These 2 suburbs have quite high crim rate, indus, high nox, high tax, high ptratio, high lstat

# (i)
print(len(bsoton[boston['rm'] > 7]))
print(len(bsoton[boston['rm'] > 8]))

