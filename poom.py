import numpy as np
import pandas as pd

class MyLineReg():
    def __init__(self, n_iter, learning_rate, weights=[]):
        self.n_iter = n_iter
        self.learning_rate = learning_rate
        self.weights = weights

    def __str__(self):
        return f'MyLineReg class: n_iter={self.n_iter}, learning_rate={self.learning_rate}'
    
    def fit(self, X, y, verbose=False):
        X.insert(0, "one", np.ones(X.index.size))
        for i in range(1, self.n_iter+1):
            print(i)

data = MyLineReg(100, 0.1, {1, 2, 3, 4}) 

input = [['John','Pune'],['Bran','Mumbai'],['Peter','Delhi']] 
data_frame = pd.DataFrame(input,columns=['Name','City'], index=[1,2,3])
data_series = pd.Series(['John','Bran','Sam'], index=[1,2,3])
data.fit(data_frame, data_series)