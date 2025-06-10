# Pandas Tutorial

import pandas as pd

# Have to use
# `pip install -U pytest`
# `pip install hypothesis`
# in order to install dependencies
# -U upgrades all to latest avaiable
#
# Can also install with `pip install "pandas[test]"`
pd.test()

# Pandas has a variety of optional dependencies which you may only need to install for certain use cases

# One package that's recommended is the Performance package which can be installed with
# `pip install "pandas[performance]"
#
# This comes with
# - numexpr - Uses multiple cores to accelerate numerical operations
# - bottleneck - Uses cython to speed up certain types of `nan`
# - numba - Uses JIT compiler to take Python code and turn it into optimized machine code using the LLVM compiler

# Let's see if we can time how long the tests take before and after installing the performance package...
#
# All performed on Apple M1 Pro 32gb ram, OS 15.5
#
# Here's before...
# `time python pandasTut.py`
# >> python pandasTut.py  376.06s user 9.14s system 98% cpu 6:29.61 total
#
# Here's after...
# `time python pandasTut.py`
# >> python pandasTut.py  518.61s user 15.35s system 98% cpu 9:03.00 total
#
# Lol! Took... 142.5 seconds longer...
# Which is somewhere between a half and a third longer



# Pandas! Let's explore a bit...

## https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html

## Table representation...
## - has frame
## - with columns and rows

# Storing passengers of the Titanic
df = pd.DataFrame(
    {
        "Name": [
            "Carter, Dwayne Michael",
            "Martin, Christopher Edward",
            "Maraj, Onika Tanya"
        ],
        "Age": [42, 59, 42],
        "Sex": ["male", "male", "female"]
    }
)
# Three columns - Name, Age, Sex 
# Each column is a Series... of names, ages, or sexes in this case
df["Age"] # [42, 59, 42]
df["Age"].max() # Helpers exist on Series, Series can also be created on their own
df.describe() # Describes numerical Series in DataFrame, provides information such as count, mean, etc

# Pandas can read CSVs
# pd.read_csv('data/titanic.csv') # Will cause error if leave in

# There are ways to see ranges of rows from imported data and to export back to CSV, Excel, maybe others

# There are other ways to see filtered sets of rows, for instace by filtering for value in a column

# Pandas also incorporates with Matplotlib to create plots from DataFrames and Series

# And there's a variety of other ways to manipulate and filter and display our data...
# Great place to stop our Pandas exploration for now... Getting closer to wrapping up these initial libraries
# And moving on to doing some work with the rest of the book here
