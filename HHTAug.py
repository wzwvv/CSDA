'''
=================================================
coding:utf-8
@Time:      2024/10/17 10:35
@File:      HHTAug.py
@Author:    Ziwei Wang
@Function: Key code of HHTAug
=================================================
'''

import numpy as np
from alg_utils import EA, HHTFilter

# Xs: The training data from each source subject
# X_tar_t: The training data from target subject
# X_tar_e: The test data of target subject
# X_tar_e is solely used for testing and remains unaugmented.
# Xs and X_tar_t have the same shape and the same category

# Euclidean alignment
if align:
    Xs = EA(Xs)
    X_tar_t = EA(X_tar_t)

Xs_aug = []
Xt_aug = []
# HHTAug is performed on channel-level (different from DWTAug)
for s in range(X_tar_t.shape[0]):  # X_tar_t.shape[0]
    chns = []
    chnt = []
    for chn in range(X_tar_t.shape[1]):
        # Signal decomposition
        imfs_tar = HHTFilter(X_tar_t[s][chn])
        imfs_src = HHTFilter(Xs[s][chn])
        components_most_src = list(range(0, len(imfs_src) - 1, 1))
        components_less_src = [len(imfs_src) - 1]
        components_most_tar = list(range(0, len(imfs_tar) - 1, 1))
        components_less_tar = [len(imfs_tar) - 1]
        # Cross-subject sub-signal reassembling and reconstruction
        chns_aug = np.sum(imfs_src[components_most_src] + imfs_tar[components_less_tar], axis=0)
        chnt_aug = np.sum(imfs_tar[components_most_tar] + imfs_src[components_less_src], axis=0)
        chns.append(chns_aug)
        chnt.append(chnt_aug)
    chns = np.array(chns)
    chnt = np.array(chnt)
    Xs_aug.append(chns)
    Xt_aug.append(chnt)

# Expand the training set: Final = [Original Xs & Augmented Xs & Augmented Xt]
Xs = np.concatenate((Xs, Xt_aug[:, :, :Xs.shape[-1]], Xs_aug[:, :, :Xs.shape[-1]]), axis=0)
ys = np.concatenate((ys, ys, ys), axis=0)  # Three parts have the same category
