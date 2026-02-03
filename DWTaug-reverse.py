'''
=================================================
coding:utf-8
@Time:      2026/2/4 01:43
@File:      DWTaug-reverse.py
@Author:    Ziwei Wang
@Function:  DWTaug-reverse augments EEG signals by three times
=================================================
'''

import numpy as np
import pywt

def DWTAug_reverse(Xs, Xt, ys, yt):
    # Euclidean alignment
    # if align:
    #     Xs = EA(Xs)
    #     X_tar_t = EA(X_tar_t)

    # Define wavelet function (optional)
    wavename = 'db4'

    # Signal decomposition
    ScA, ScD = pywt.dwt(Xs, wavename)
    TcA, TcD = pywt.dwt(Xt, wavename)

    # Cross-subject sub-signal reassembling and time domain reconstruction
    Xs_aug = pywt.idwt(ScA, TcD, wavename, 'smooth')  # Src approximated component + Tar detailed component
    Xt_aug = pywt.idwt(TcA, ScD, wavename, 'smooth')  # Tar approximated component + Src detailed component

    # Expand the training set: Final = [Original Xs & Augmented Xs & Augmented Xt]
    X_aug = np.concatenate((Xt_aug[:, :, :Xs.shape[-1]], Xs_aug[:, :, :Xs.shape[-1]]), axis=0)
    y_aug = np.concatenate((ys, yt), axis=0)  # Three parts have the same category

    return X_aug, y_aug



# EEGData_Train: np.array of raw EEG signals
# EEGLabel_Train: np.array of the corresponding labels

# split data by categories
N = 32
C = 18
T = 1000
n_classes = 2
EEGData_Train = np.random.rand(N, C, T)  # replace this line with your own data
EEGLabel_Train = np.random.randint(low=0, high=n_classes, size=N)  # replace this line with your own label
mask_0 = EEGLabel_Train == 0  # class 0 mask
mask_1 = EEGLabel_Train == 1  # class 1 mask
X0 = EEGData_Train[mask_0]  # class 0 data
X1 = EEGData_Train[mask_1]  # class 1 data
y0 = EEGLabel_Train[mask_0]  # class 0 label
y1 = EEGLabel_Train[mask_1]  # class 1 label
X0_R = X0[::-1, :, :]  # X0_R is the reverse of X0 along the time axis
X1_R = X1[::-1, :, :]  # X1_R is the reverse of X1 along the time axis
aug_inputs_source_0, aug_labels_source_0 = DWTAug_reverse(X0, X0_R, y0, y0)  # class 0 augmentation
aug_inputs_source_1, aug_labels_source_1 = DWTAug_reverse(X1, X1_R, y1, y1)  # class 1 augmentation
aug_inputs_source = np.concatenate((EEGData_Train, aug_inputs_source_0, aug_inputs_source_1), axis=0)  # data concatenation, DWTaug-reverse augments EEG signals by three times.
aug_labels_source = np.concatenate((EEGLabel_Train, aug_labels_source_0, aug_labels_source_1), axis=0)  # data concatenation, DWTaug-reverse augments EEG signals by three times.

