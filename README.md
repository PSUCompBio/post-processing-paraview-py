# post-processing-paraview-py
Series of post processing functions that extracts metrics from simulation results

## Move multiViewPort.py and Merged.vtk into ex5, then:

### On windows/linux
pvpython multiViewPorts.py Merged.vtk maxstrain.dat

### On Cloud
xvfb-run pvpython multiViewPorts.py Merged.vtk maxstrain.dat
