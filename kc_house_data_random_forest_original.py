"""kc housing datset"""
#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#importing dataset
data = pd.read_csv("/home/yash/Programming/Machine Learning/practice_datasets/SGH_files/kc_house_data_original.csv")
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values


"""#optimising the dataset
import statsmodels.api as sm
X = np.append(np.ones((21613, 1)).astype(int), X, 1)
X_opt = X[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()"""


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 11)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

from sklearn.metrics import r2_score, mean_squared_error
score = r2_score(y_test, y_pred)
print(score * 100)
"""The accuracy is 88.313%"""

plt.plot(y_pred, y_test, color="red")
plt.scatter(y_test, y_pred, color="blue")
pred = pd.DataFrame(y_pred)
test = pd.DataFrame(y_test)
pred.describe()
test.describe()
import pickle

pickle.dump(regressor, open("KC_SAVED_RANDOM_FOREST_ORIGINAL.sav", "wb"))