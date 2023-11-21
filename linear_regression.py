import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

#buat data jumlah kamar
bedrooms = np.array([1,1,2,2,3,4,4,5,5,5])

#data harga rumah. asumsi dalam dollar
house_price = np.array([15000,18000,27000,34000,50000,68000,6500,81000,85000,90000])

#%matplotlib inline
plt.scatter(bedrooms, house_price)

#latih model dengan Linear Regression.fit()
bedrooms = bedrooms.reshape(-1,1)
linreg = LinearRegression()
linreg.fit(bedrooms, house_price)

# menampilkan plot hubungan antara jumlah kamar dengan harga rumah
plt.scatter(bedrooms, house_price)
plt.plot(bedrooms, linreg.predict(bedrooms))