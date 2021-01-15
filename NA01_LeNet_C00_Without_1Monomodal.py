import tensorflow as tf
import numpy as np
from scipy.io import loadmat, savemat

def Test_Augmented_2_Test(y_Deep_NN_Test_Augmented, Num_Augmentation):
    y_Deep_NN_Test = np.zeros((int(y_Deep_NN_Test_Augmented.shape[0] / Num_Augmentation[0]), 2)) # y_Deep_NN_Test = np.zeros((int(672 / 48), 2)) = np.zeros((14, 2))
    Sum_column1 = 0
    Sum_column2 = 0
    for i in range(y_Deep_NN_Test.shape[0]):  # y_Deep_NN_Test.shape[0] = 14 => 0, 1, ..., 13
        row_index = i * Num_Augmentation[0]  # row_index = i*48
        for j in range(Num_Augmentation[0]):  # Num_Augmentation[0] = 48 => 0, 1, ..., 47
            Sum_column1 = Sum_column1 + y_Deep_NN_Test_Augmented[(row_index + j), 0]
            Sum_column2 = Sum_column2 + y_Deep_NN_Test_Augmented[(row_index + j), 1]
        y_Deep_NN_Test[i, 0] = Sum_column1 / Num_Augmentation[0]
        y_Deep_NN_Test[i, 1] = Sum_column2 / Num_Augmentation[0]
        Sum_column1 = 0
        Sum_column2 = 0
    return y_Deep_NN_Test