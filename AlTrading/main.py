# This is a learning project for Algoritmic Trading
# Reference is : https://www.datacamp.com/community/tutorials/finance-python-trading
# Author: AdHuGo (Github)

import quandl
aapl = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")

print(aapl)

#descrive() method shows us a summary info about the imported data
print(aapl.describe())



#print(aapl.asfreq("M", method="bfill"))

# import matplotlib.pyplot as plt
#
# aapl["Close"].plot(grid=True)
# plt.show()