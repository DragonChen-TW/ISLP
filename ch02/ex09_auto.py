import pandas as pd
import matplotlib.pyplot as plt

# (a) 
auto = pd.read_csv('../data/Auto.csv', na_values='?')
auto.dropna(inplace=True)
print(auto.dtypes)
print(auto.head(10))

# inspect some columns to confirm data types
print(auto['cylinders'].value_counts())
print(auto['year'].value_counts())
print(auto['origin'].value_counts())

# mpg  cylinders  displacement  horsepower  weight  acceleration are quantitative
# year, origin and name are qualitative, origin might be categorical variable

# (b) (c)
quan_cols = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration"]
print(auto[quan_cols].describe())

# (d)
auto_drop = auto.drop(auto.index[9:84])
print(auto_drop[quan_cols].describe())

# (e)
pd.plotting.scatter_matrix(auto[quan_cols], alpha=0.3)
plt.show()

# (f)
# cylinders, displacement, horsepower and weight might have relation with mpg
