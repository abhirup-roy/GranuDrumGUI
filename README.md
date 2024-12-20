# GranuDrum Digital Twin

![GranuDrum-DigitaTwin-Render](/uploads/bbfd74d541b9b84e5c2a2fab6955b600/GranuDrum.png)

## Description
A discrete element method (DEM) Digital Twin of the Granutools' GranuDrum powder characterisation tool built using PICI-LIGGGHTS.
This digital twin allows users to understand in more depth the behaviour of a powder in the GranuDrum. 
Particle properties can be defined and the individual particle data or bulk powder behaviour extracted and analysed.

## Example Usage

The GranuDrum digital twin can be used to extract individual particle data for every particle in the system. This video shows an animation of the GranuDrum digital twin with each particle
coloured by its absolute velocity. From this video, the free flowing active layer can be seen from the rest of the passive material that is following the rotation of the drum. This data 
can then be used to get a velocity profile for the material in the drum.

![GranuDrum Example Video](readme_files/gd_animation_45rpm.mp4)

### Results

![Graph showing the change in cohesive index with different cohesive energy densities](readme_files/ci_vs_ced.png)

The graph above shows an example of results that can be obtained from the GranuDrum digital twin. 
Specifically in this case the change in cohesive index with increasing cohesive energy density at different sliding friction values.
A clear trend showing can be seen showing that as the cohesive energy density increases the cohesive index increases. At the same time 
sliding friction shows very little influence on the cohesive index except at  the highest cohesive energy density.

## Getting Started
To be able to use this digital twin an installation of PICI-LIGGGHTS is required. A step-by-step guide of how to install PICI-LIGGGHTS can be found [here](https://uob-positron-imaging-centre.github.io/InstallingPICI-LIGGGHTS/).

## How to use the Digital Twin
Using the digital twin is very simple but to explore the behaviour of powder in the GranuDrum digital twin the particle properties are required. 
Most of the particle properties can be easily defined by changing the values in the parameters.txt file.
The parameters.txt file allows the sliding friction, rolling friction, restitution, material density, cohesive energy density, drum speed (RPM) and number of particles to be defined.
The particle size distribution also needs to be defined. This is currently done by going into the granudrum_liggghts.sim file and manually changing it.
Previous knowledge of LIGGGHTS is required to do this currently but is planned to be improved in the future.

## Post Processing the Data
The digital twin outputs images in the same way as the real GranuDrum. This images can then be used with the post-processing script to calculate the dynamic angle of repose and cohesive index.
To do this set the 'root' variable in the python file 'run_gd_postprocessing.py' to the folder containing the images and run the script.
The Cohesive Index, Dynamical angle of repose and the 3rd order polynomial fit to the free surface will be saved as a Pandas dataframe in the folder designated in 'df_savepath' variable.

## Roadmap
- [x] Add parameter text input file.
- [ ] Develop way of automatically inputting particle size distribution.
- [ ] Investigate including a compiled version of PICI-LIGGGHTS to the digital twin files to avoid everyone having to compile it themselves.
- [ ] Include finalised post-processing script to calculate dynamic angle of repose and cohesive index from the simulation.
- [ ] Work out a way of calculating number of particles required in a certain volume.

## Issues
If you run into any issues or bugs let us know by raising and issue on the GitLab! If you find a way to fix it raise a pull request!

## Authors and acknowledgment
The development of GranuTools digital-twins was made during the PhD thesis of Ben Jenkins in the framework 
of a collaboration between GranuTools and University of Birmingham under the academic supervision of 
Dr. Kit Windows-Yule and Prof. Jonathan Seville.

## Project status
Actively being worked on!
