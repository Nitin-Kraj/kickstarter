import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split


class Data(object):

    def __init__(self, fname, random_state=42):
        self.fname = fname
        self.radom_state = random_state
        self._scalar = None

    def load(self, subset=None):
        df = pd.read_csv(self.fname, index_col=0, skipinitialspace=True).iloc[:, 1:]
        if subset:
            df = df[subset + ["state_code"]]
        x = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values
        return x, y

    def normalize(self, x, algorithm="min-max"):

        if algorithm == "min-max":
            self._scalar = MinMaxScaler()
        elif algorithm == "standard":
            self._scalar = StandardScaler()
        elif algorithm == "robust":
            self._scalar = RobustScaler(quantile_range=(25, 78))
        self._scalar.fit(x)
        return self._scalar.transform(x)

    def split(self, x, y, test_ratio=0.2, random_state=None):
        if random_state is None:
            random_state = self.radom_state
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=test_ratio,
            stratify=y,
            random_state=random_state)
        return x_train, x_test, y_train, y_test



