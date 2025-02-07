# Scikit-Learn Imports (Basic)
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.naive_bayes import GaussianNB


class SpamClassifier:
    def __init__(self, vectorizer, model, X_train, y_train, X_test, y_test):
        self.vectorizer = vectorizer
        self.vectorizer_name = type(vectorizer).__name__
        self.model = model
        self.model_name = type(model).__name__

        # Vectorization
        self.X_train = self.vectorizer.fit_transform(X_train)
        self.X_test = self.vectorizer.transform(X_test)
        self.y_train = y_train
        self.y_test = y_test

        # Convert to dense if the model requires it (for GaussianNB)
        if isinstance(self.model, GaussianNB):
            self.X_train = self.X_train.toarray()
            self.X_test = self.X_test.toarray()

        # Training, Prediction, and Evaluation
        self.train(self.X_train, self.y_train)
        self.predict(self.X_test)
        self.evaluate_model_metrics()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        self.y_pred = self.model.predict(X_test)

    def evaluate_model_metrics(self):
        self.accuracy = accuracy_score(self.y_test, self.y_pred)
        self.precision = precision_score(self.y_test, self.y_pred)
        self.recall = recall_score(self.y_test, self.y_pred)
        self.f1_score = f1_score(self.y_test, self.y_pred)

    def get_model_metrics_object(self):
        return {
            "accuracy": self.accuracy,
            "precision": self.precision,
            "recall": self.recall,
            "f1_score": self.f1_score,
        }

    def get_model(self):
        return self.model
