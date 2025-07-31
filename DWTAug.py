'''
=================================================
coding:utf-8
@Time:      2024/10/17 10:17
@File:      DWTAug.py
@Author:    Ziwei Wang
@Function: Key code of DWTAug
=================================================
'''

import numpy as np
import pywt
from alg_utils import EA

# Xs: The training data from each source subject
# X_tar_t: The training data from target subject
# X_tar_e: The test data of target subject
# X_tar_e is solely used for testing and remains unaugmented.
# Xs and X_tar_t have the same shape and the same category

# Euclidean alignment
if align:
    Xs = EA(Xs)
    X_tar_t = EA(X_tar_t)

# Define wavelet function (optional)
wavename = 'db4'

# Signal decomposition
ScA, ScD = pywt.dwt(Xs, wavename)
TcA, TcD = pywt.dwt(X_tar_t, wavename)

# Cross-subject sub-signal reassembling and time domain reconstruction
Xs_aug = pywt.idwt(ScA, TcD, wavename, 'smooth')  # Src approximated component + Tar detailed component
Xt_aug = pywt.idwt(TcA, ScD, wavename, 'smooth')  # Tar approximated component + Src detailed component

# Expand the training set: Final = [Original Xs & Augmented Xs & Augmented Xt]
Xs = np.concatenate((Xs, Xt_aug[:, :, :Xs.shape[-1]], Xs_aug[:, :, :Xs.shape[-1]]), axis=0)
ys = np.concatenate((ys, ys, ys), axis=0)  # Three parts have the same category

