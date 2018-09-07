from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB


class KNeighbors(KNeighborsClassifier):
    name = "K-Nearest Neighbor"

    def fit(self, x, y):
        super(KNeighbors, self).fit(x, y)


class CSupportVector(SVC):
    name = "C-Support Vector"

    def fit(self, x, y):
        super(CSupportVector, self).fit(x, y)


class DecisionTree(DecisionTreeClassifier):
    name = "Decision Tree"

    def fit(self, x, y,
            sample_weight=None,
            check_input=True,
            X_idx_sorted=None):

        super(DecisionTree, self).fit(x, y, sample_weight, check_input, X_idx_sorted)


class RandomForest(RandomForestClassifier):
    name = "Random Forest"

    def fit(self, x, y, sample_weight=None):
        super(RandomForest, self).fit(x, y, sample_weight)


class AdaBoost(AdaBoostClassifier):
    name = "AdaBoost"

    def fit(self, x, y, sample_weight=None):
        return super(AdaBoost, self).fit(x, y, sample_weight)


class GaussianNaiveBayes(GaussianNB):
    name = "Naive Bayes"

    def fit(self, x, y):
        super(GaussianNaiveBayes, self).fit(x, y)


