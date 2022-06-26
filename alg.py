import numpy as np

def get_gradient(x, y, w, b):

    m, n = x.shape
    dj_dw = np.zeros(w.shape)
    dj_db = 0
    for i in range(m):
        z = 0
        z += np.dot(x[i], w)+b
        f_wb = 1.0/(1.0+np.exp(-z))
        err = f_wb-y[i]
        for j in range(n):
            dj_dw_ij = err*x[i][j]
            dj_dw[j] += dj_dw_ij
        dj_db = dj_db + err
    dj_dw = dj_dw / m
    dj_db = dj_db / m





