from granudrum_analysis import AnalyseGranuDrum
import numpy as np

path = 'Example Data'  # Path to data
filename = 'gd_rtd_'  # Common string used in all images
n = 50  # Number of images to use in the analysis


# Run analysis
analysis = AnalyseGranuDrum(crop_percentage=10,
                            images_path=path,
                            common_filename=filename,
                            number_of_images=n,
                            processing_diameter=400)

interfaces, horizontal_shift = analysis.extract_interface(binary_threshold=1)  # Get x,y coordinates of all interface
data = analysis.average_interface(interfaces)

# Extract bulk measurements
cohesive_index = analysis.cohesive_index(data.derotated_averaged_interface, data.interfaces)
angle_data = analysis.dynamic_angle_of_repose(data.derotated_averaged_interface)
poly_3 = analysis.polynomial_fit(data.derotated_averaged_interface, 3)

print(f'Cohesive Index: {cohesive_index}')
print(f'Dynamic Angle of Repose: {angle_data.dynamic_angle_degrees}')


analysis.plot_interface(interfaces, average_interface=data.derotated_averaged_interface, polynomial=poly_3) # Plot interfaces

