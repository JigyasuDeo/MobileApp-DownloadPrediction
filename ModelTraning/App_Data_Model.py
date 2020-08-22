# Importing libraries 
import pandas as pd
import random
from sklearn.externals import joblib
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Loading dataset 
df = pd.read_csv('../appdata1.csv')
x = df[['Size', 'Price', 'Rating']]

# Scaling our data
y = df['Installs']/10000 # Scaling 

# Getting dummy variables for categories as it is string
categ = df['Category']
categ = pd.get_dummies(categ)

x= pd.concat([x,categ], axis=1)

# Dividing our data into training and testing set
X_train, x_test, Y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# Training our Model
model = RandomForestRegressor(n_estimators=2000, random_state=42)
model.fit(X_train, Y_train)

# Dumping our model for use in MainMenu.py file
joblib.dump(model , '../App_prediction.pk1')
