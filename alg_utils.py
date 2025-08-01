# -*- coding: utf-8 -*-
# @Time    : 2024/04/10
# @Author  : Ziwei Wang
# @File    : alg_utils.py
from scipy.linalg import fractional_matrix_power
import numpy as np
from pyhht import EMD

def EA(x):
    """
    Parameters
    ----------
    x : numpy array
        data of shape (num_samples, num_channels, num_time_samples)

    Returns
    ----------
    XEA : numpy array
        data of shape (num_samples, num_channels, num_time_samples)
    """
    cov = np.zeros((x.shape[0], x.shape[1], x.shape[1]))
    for i in range(x.shape[0]):
        cov[i] = np.cov(x[i])
    refEA = np.mean(cov, 0)
    sqrtRefEA = fractional_matrix_power(refEA, -0.5)
    XEA = np.zeros(x.shape)
    for i in range(x.shape[0]):
        XEA[i] = np.dot(sqrtRefEA, x[i])
    return XEA


def EA_online(x, R, sample_num):
    """
    Parameters
    ----------
    x : numpy array
        sample of shape (num_channels, num_time_samples)
    R : numpy array
        current reference matrix (num_channels, num_channels)
    sample_num: int
        previous number of samples used to calculate R

    Returns
    ----------
    refEA : numpy array
        data of shape (num_channels, num_channels)
    """

    cov = np.cov(x)
    refEA = (R * sample_num + cov) / (sample_num + 1)
    return refEA


def EA_ref(x):
    """
    Parameters
    ----------
    x : numpy array
        data of shape (num_samples, num_channels, num_time_samples)

    Returns
    ----------
    XEA : numpy array
        data of shape (num_samples, num_channels, num_time_samples)
    """
    cov = np.zeros((x.shape[0], x.shape[1], x.shape[1]))
    for i in range(x.shape[0]):
        cov[i] = np.cov(x[i])
    refEA = np.mean(cov, 0)
    sqrtRefEA = fractional_matrix_power(refEA, -0.5)
    XEA = np.zeros(x.shape)
    for i in range(x.shape[0]):
        XEA[i] = np.dot(sqrtRefEA, x[i])
    return XEA, refEA



# 定义HHT的滤波函数，提取部分EMD组分
def HHTFilter(eegRaw):
    # 进行EMD分解
    decomposer = EMD(eegRaw)
    # 获取EMD分解后的IMF成分
    imfs = decomposer.decompose()
    return imfs
