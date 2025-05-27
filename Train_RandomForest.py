import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

df = pd.read_csv("C:\\Users\\ethan\\Downloads\\c2023ExportTable.csv")
X = df[["Band_1", "Band_2", "Band_3"]]
y = df["G_Code"]                       

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

dump(clf, "C:\\Users\\ethan\\Downloads\\eelgrass_model.pkl")
