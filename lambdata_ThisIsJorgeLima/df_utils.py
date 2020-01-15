"""
utility functions for working with DataFrames
"""

import pandas

TEST_DF = pandas.DataFrame([1,2,3])
"""
Check a dataframe for nulls
Let's check and see if this string is empty 
using not + strip() 
inilializing string 
"""
test_str1 = "" 
test_str2 = "  "
  
# checking if string is empty 
print ("The zero length string without spaces is empty ? : ", end = "") 
if(not (test_str1 and test_str1.strip())): 
    print ("Yes") 
else : 
    print ("No") 
  
# prints Yes 
print ("The zero length string with just spaces is empty ? : ", end = "") 
if(not(test_str2 and test_str2.strip())): 
    print ("Yes") 
else : 
    print ("No") 

#*************************************************************
import sklearn

def data_split(examples, labels, train_frac, random_state=None):
    ''' https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
    param data:       Data to be split
    param train_frac: Ratio of train set to whole dataset

    Randomly split dataset, based on these ratios:
        'train': train_frac
        'valid': (1-train_frac) / 2
        'test':  (1-train_frac) / 2

    Eg: passing train_frac=0.8 gives a 80% / 10% / 10% split
    '''

    assert train_frac >= 0 and train_frac <= 1, "Invalid training set fraction"

    X_train, X_tmp, Y_train, Y_tmp = sklearn.model_selection.train_test_split(
                                        examples, labels, train_size=train_frac, random_state=random_state)

    X_val, X_test, Y_val, Y_test   = sklearn.model_selection.train_test_split(
                                        X_tmp, Y_tmp, train_size=0.5, random_state=random_state)

    return X_train, X_val, X_test,  Y_train, Y_val, Y_test
