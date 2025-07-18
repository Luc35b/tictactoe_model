import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib

single = np.loadtxt('Data/tictac_single.txt')

single_df = pd.DataFrame(single).astype(int)
single_df = single_df.rename(columns={9:"Best Move"})
np.random.shuffle(single_df.values)
single_df_train, single_df_test = train_test_split(single_df, test_size=.2, random_state=10)

X_train = single_df_train.iloc[:,:9].values
y_train = single_df_train.iloc[:,9]
X_test = single_df_test.iloc[:,:9].values
y_test = single_df_test.iloc[:,9]

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = MLPClassifier(solver="adam", activation='relu', learning_rate='constant',
                      max_iter=3000, random_state=10, hidden_layer_sizes=(200, 100), alpha=.001)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, y_pred))

joblib.dump(model, 'tictac_model.pkl')
print("Model saved to tictac_model.pkl")