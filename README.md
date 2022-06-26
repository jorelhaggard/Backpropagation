# Backpropagation
 ## A backpropagation algorithm for binary classification written using Numpy.  
 *This algorithm is applicable to data sets of size (m, n), but will not generalize to networks with hidden layers.*
 
 When called, this function will iterate over each training example in m, then return the computed values of dJ/dw and dJ/db. 
  
 >dJ/dw is an array of size (n, 1) containing the values of the gradient of the cost, J, with respect to each w[j].
 
 >dJ/db is a scalar with value equivalent to the gradient of the cost, J, with respect to the bias, b. 
 
