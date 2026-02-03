# Time-Frequency Transform Based Cross-Subject EEG Data Augmentation  

📰 News: We've released a new version of DWTaug, namely DWTaug-reverse, which is more effective for within-subject data augmentation. By reverse the inputs, DWTaug-reverse augments EEG signals by three times. More information can see in [code](https://github.com/wzwvv/CSDA/blob/main/DWTaug-reverse.py).


This repository contains the original Python code for our paper [**Time-Frequency Transform Based Cross-Subject EEG Data Augmentation**](https://www.sciencedirect.com/science/article/pii/S0950705125001212) (KBS, 2025), featuring three key implementations:  
- **DWTaug**: Discrete Wavelet Transform-based EEG data augmentation.  
- **HHTaug**: Hilbert-Huang Transform-based EEG data augmentation.  
- **DWTaug-ML**: A multi-level version of DWTaug.
- **DWTaug-reverse**: A more effective way of implementation, for the within-subject scenario.

<img width="908" alt="image" src="https://github.com/user-attachments/assets/92343b72-8a22-4075-91fe-9765f0f8955f" />


## Overview  
This work aims to tackle key challenges in BCI applications, including **data scarcity**, **EEG signal non-stationarity**, as well as **individual differences**. The proposed DWTAug and HHTAug follow three steps: time-frequency domain signal decomposition, cross-subject sub-signal reassembling, and time domain reconstruction. Augmenting data expands the pool of labeled training samples, alleviating the data scarcity problem; time-frequency decomposition captures the non-stationary properties of EEG signals more effectively; finally, cross-subject reassembling of sub-signals handles individual differences.

## Applications  
The proposed approaches are effective for **motor imagery (MI)**, **P300**, and **SSVEP**, especially when significant individual difference exists. Notably, DWTaug and HHTaug demonstrate high effectiveness in the SSVEP paradigm, particularly on Benchmark dataset, achieving an accuracy improvement exceeding 10%.

## Results  
The proposed methods have been tested on **17 EEG datasets** across multiple BCI paradigms, consistently outperforming existing data augmentation approaches.

<img width="970" alt="image" src="https://github.com/user-attachments/assets/cfdb26e9-fb84-405f-a3dc-e8214109b308" />

## Visualizations 
(1) Visualizations of EEG trials before (blue lines) and after (orange lines) ten different data augmentation approaches:

<img width="701" alt="image" src="https://github.com/user-attachments/assets/a55d7dbf-3c07-4bab-b309-bb69cfdcda2f" />

(2)  $t$-SNE feature visualizations of the original, DWTaug, and HHTaug data from the source and target subjects on four MI datasets.

<img width="653" alt="image" src="https://github.com/user-attachments/assets/33fc7789-aedc-4194-b6c6-87b69c00c88e" />

## Citation
If you find this repo helpful, please cite our work:
```
@Article{Wang2025CSDA,
  title={Time-frequency transform based EEG data augmentation for brain-computer interfaces},
  author={Wang, Ziwei and Li, Siyang and Chen, Xiaoqing and Wu, Dongrui},
  journal={Knowledge-Based Systems},
  pages={113074},
  year={2025},
  volume={311}
}
```

## Contact
For any questions or collaborations, please feel free to reach out via **vivi@hust.edu.cn** or open an issue in this repository.
