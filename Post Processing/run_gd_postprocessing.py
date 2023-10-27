import numpy as np
import pandas as pd
import pyarrow.feather as feather
import os
import gd_postprocessing as pp

# Paths
root = ""  # Dir path to GranuDrum digital twin generated images
df_savepath = ""  # Save path for the data

# User input
number_of_images_to_use = 50  # Number of images to use for postprocessing
number_of_attempts = 5  # Number of times to run postprocessing and average over

# Setup empty arrays
dynamic_angle = []
cohesive_index = []
poly_3 = []
poly_5 = []

try:
    print(f'Reading data from: {root}')

    cohesiveindex_array = []
    dynamicangle_array = []

    # Average data over n calculations
    for o in range(number_of_attempts):
        interface_data = pp.process_images(root, 'gd_rtd_', n=number_of_images_to_use)
        data = pp.dynamic_angle_of_repose(interface_data)
        ci = pp.cohesive_index(interface_data, data.averaged_interface)

        cohesiveindex_array.append(ci)
        dynamicangle_array.append(data.dynamic_angle_degrees)

    polynomial = pp.fit_polynomial(data.averaged_interface)
    polynomial = polynomial.convert().coef
    polynomial_5th = pp.fit_polynomial(data.averaged_interface, order=5)
    polynomial_5th = polynomial_5th.convert().coef

    avgci = np.mean(cohesiveindex_array)
    avg_da = np.mean(dynamicangle_array)
    print(f'Success!')
except:
    print('Error reading data')
    avgci = np.NAN
    avg_da = np.NAN
    polynomial = np.NAN
    polynomial_5th = np.NAN

cohesive_index.append(avgci)
dynamic_angle.append(avg_da)
poly_3.append(polynomial)
poly_5.append(polynomial_5th)

# Convert to dataframe and save
data = {'cohesive_index': cohesive_index,
        'dynamic_angle_of_repose': dynamic_angle,
        '3rd_order_polynomial': poly_3,
        '5th_order_polynomial': poly_5
        }
df = pd.DataFrame(data)

if not os.path.isdir(df_savepath):
    os.makedirs(df_savepath)
df.to_feather(f'{df_savepath}/gd_data')
