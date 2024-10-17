# Time-Frequency Transform-Based Cross-Subject EEG Data Augmentation  

This repository contains the original Python code for **Time-Frequency Transform-Based Cross-Subject EEG Data Augmentation**, featuring three key implementations:  
- **DWTAug**: Discrete Wavelet Transform-based EEG data augmentation.  
- **HHTAug**: Hilbert-Huang Transform-based EEG data augmentation.  
- **DWTAug-ML**: A multi-level version of DWTAug.  

## Overview  
This work aims to tackle key challenges in BCI applications, including **data scarcity**, **EEG signal non-stationarity**, as well as **individual differences**. The proposed DWTAug and HHTAug follow three steps: time-frequency domain signal decomposition, cross-subject sub-signal reassembling, and time domain reconstruction. Augmenting data expands the pool of labeled training samples, alleviating the data scarcity problem; time-frequency decomposition captures the non-stationary properties of EEG signals more effectively; finally, cross-subject reassembling of sub-signals handles individual differences.

## Applications  
The proposed approaches are effective for **motor imagery (MI)**, **P300**, and **SSVEP**, especially when significant individual difference exists.

## Results  
The proposed methods have been tested on **17 EEG datasets** across multiple BCI paradigms, consistently outperforming existing data augmentation approaches.  
