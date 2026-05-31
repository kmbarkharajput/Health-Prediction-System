import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("dataset/health_data.csv")

X = data[["glucose", "haemoglobin", "cholesterol"]]

y = data["risk"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(criterion="gini", random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("MODEL TRAINING COMPLETED")
print("=" * 50)
print(f"Accuracy: {accuracy * 100: .2f}%")
print("\nClassification_report:")
print(classification_report(y_test, y_pred))

joblib.dump(model, "health_model.pkl")
print("\nModel saved as 'health_model.pkl'")

