
# Importing libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings( "ignore" )
# to compare our model's accuracy with sklearn model
from sklearn.linear_model import LogisticRegression
# Logistic Regression
class LogitRegression(): # Logistic Regression class
    def __init__( self, learning_rate, iterations ) :       #Initialization of model
        self.learning_rate = learning_rate
        self.iterations = iterations
        
    # Function for model training
    def fit( self, X, Y ) :
        # no_of_training_examples, no_of_features
        self.m, self.n = X.shape         # Calculates shape of X matrix and save it in m and n
        # weight initialization
        self.W = np.zeros( self.n )
        self.b = 0
        self.X = X
        self.Y = Y
        
        # gradient descent learning
        for i in range( self.iterations ) :  # Looping on the basis of provided iterations
            self.update_weights()    # Calculating optimal value of W(weight) and b(bias).
        return self

    def update_weights( self ) :     # Helper function to update weights in gradient descent
        A = 1 / ( 1 + np.exp( - ( self.X.dot( self.W ) + self.b ) ) )

        # calculate gradient
        tmp = ( A - self.Y.T )
        tmp = np.reshape( tmp, self.m )
        dW = np.dot( self.X.T, tmp ) / self.m    #Calculate dW (derivative)
        db = np.sum( tmp ) / self.m  #Calculate db(derivative)

        # update weights
        self.W = self.W - self.learning_rate * dW
        self.b = self.b - self.learning_rate * db

        return self

    # Sigmoid function  h( x )
    def predict( self, X ) :
        Z = 1 / ( 1 + np.exp( - ( X.dot( self.W ) + self.b ) ) )
        Y = np.where( Z > 0.5, 1, 0 )
        return Y , Z

def find():  #To split the dataset into X and Y
    df = pd.read_csv("D:\PythonProject\HeartDiseasePrediction_LogisticRegresstion\predictor\heartdata.csv")
    X = df.iloc[:,:-1].values
    Y = df.iloc[:,-1:].values
    return X,Y


