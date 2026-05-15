import pandas as pd
from sklearn.tree import DecisionTreeClassifier

class AkinatorAI:
    def __init__(self, csv_path='hp_modified.csv'):
        self.df = pd.read_csv(csv_path)
        self.candidates = self.df.copy()
        self.asked_features = []
        self.step_counter = 0

    def get_next_question(self):
        """Uses a Decision Tree to find the most discriminative feature."""
        if len(self.candidates) <= 1:
            return None
            
        X = self.candidates.drop(['name'], axis=1)
        X = X.drop(self.asked_features, axis=1) 
        y = self.candidates['name']

        if X.shape[1] == 0:
            return None

        clf = DecisionTreeClassifier(random_state=42, max_depth=1)
        clf.fit(X, y)
        
        best_feature_index = clf.tree_.feature[0]
        if best_feature_index < 0:
            return None
            
        return X.columns[best_feature_index]

    def update_candidates(self, feature, answer):
        """Filters the dataset pool based on the user's answer."""
        self.asked_features.append(feature)
        if answer == 1:
            self.candidates = self.candidates[self.candidates[feature] == 1]
        else:
            self.candidates = self.candidates[self.candidates[feature] == 0]
        self.step_counter += 1

    def get_prediction(self):
        """Returns the top guess from the remaining pool."""
        if len(self.candidates) > 0:
            return self.candidates.iloc[0]['name']
        return "Unknown"