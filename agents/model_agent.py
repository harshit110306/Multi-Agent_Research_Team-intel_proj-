from agents.base_agent import BaseAgent
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ModelAgent(BaseAgent):

    def train_model(self):
        self.log("Starting autonomous experiment loop...")

        data = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(
            data.data, data.target, test_size=0.2, random_state=42
        )

        best_acc = 0

        for n_estimators in [50, 100, 150, 200]:

            model = RandomForestClassifier(n_estimators=n_estimators)
            model.fit(X_train, y_train)

            preds = model.predict(X_test)
            acc = accuracy_score(y_test, preds)

            self.log(f"n_estimators={n_estimators} → Accuracy={acc}")

            if acc > best_acc:
                best_acc = acc

        self.memory.write("model_accuracy", best_acc)

        self.log(f"Best accuracy achieved: {best_acc}")

        return best_acc
