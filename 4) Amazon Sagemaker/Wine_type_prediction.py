# %pip install sagemaker --upgrade --quiet 

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Het laden van de "Wine dataset"
wine = load_wine()

# De volledige data opdelen in X="info data" en de Y="data dat we willen voorspellen"
X = wine.data
y = wine.target

# Splits de dataset in training en testing sets
# X_train en y_train is voor het trainen van het model
# X_test en y_test is voor het testen van het model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definieren van het model: Decision Tree Classifier
model = DecisionTreeClassifier()

# Trainen van het model met de training data
model.fit(X_train, y_train)

# Voorspellen op de test data
y_pred = model.predict(X_test)

# Berekenen van de accuracy
accuracy = accuracy_score(y_test, y_pred)





print(f"Accuracy: {accuracy:.2f}")




# Maken vanvoorspellingen met nieuwe data
# Elk data punt heeft 13 input waarden. Hier zijn dat de karakteristieken van de wijn. 
new_data = [[13.2, 2.77, 2.51, 18.5, 98, 2.23, 2.43, 0.26, 1.57, 5.2, 1.08, 3.12, 1000],
            [12.37, 0.94, 1.36, 10.6, 88, 1.98, 0.57, 0.28, 0.42, 1.95, 1.05, 1.82, 520]]

new_predictions = model.predict(new_data)
new_predictions_labels = [wine.target_names[pred] for pred in new_predictions]

for i, pred in enumerate(new_predictions_labels):
    if(pred == "class_0"):
        print(f"De wijn type van Nr.{i + 1}: Rode wijn")
    elif(pred =="class_1"):
        print(f"De wijn type van Nr.{i + 1}: Witte wijn")
    elif(pred =="class_2"):
        print(f"De wijn type van Nr.{i + 1}: Rosé wijn")