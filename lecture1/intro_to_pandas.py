import pandas as pd # type: ignore


# dataframe is our main object. Columns are the stocks
# rows are data corresponding to the stocks: typically we look at monthly data
# each column can be a different data type 
# dataframe: object that holds a rectulangular data structure

# the series data type is a single column of data
# when you grab one column of data from the dataframe it becomes a series

# in this class we typically use csv files
# feather files for higher frequency data like daily or intraday data

# we will use read_csv function in pandas to read this file from diether's web server
# This file contains two stocks: AMZN and HRL
# Since it is a smaller data set it is fine to get it remotely
df = pd.read_csv("https://diether.org/prephd/01-intro.csv")

# displaying data: we use the print function
# rounding to 1 decimal place for better readability (also removes scientific notation on market cap)
# can also pass a dictionary to the round function to specify different rounding for different columns

# print(df.round(1))

# marketcap = price * shares outstanding
# this is how data is organized in finance and how we want our data organized

# indexing: 
df['revenue']  # grabs the revenue column as a series


# pass a list to grab multiple columns
df[['year', 'revenue']]  # grabs multiple columns as a dataframe

# checking the data type: use type() function
type(df['revenue'])

# profit margin = ebit / revenue
# ebit = earnings before interest and taxes (whats left over after costs before taxes)
# revenue = total sales (Doesnt take off cost of accounts sold and operating expenses)

df['profit_margin'] = df['ebit'] / df['revenue'] # pandas works element by element for division
print(df.round(2))

# pandas also have if then else logic
# df['year'] > 2010  # returns a series of True/False values
df['gt_2010'] = df['year'] > 2010  # creates a new column with True/False values

# can do data selection with these boolean values
print(df[df['gt_2010']])

# could have also done:
print(df[df['year'] > 2010])

# can also make a smaller dataframe using this sorting logic
sub = df[df['year'] > 2010]