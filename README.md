# pymol_sterimol_visualization
Visualization of MORFEUS sterimol arrows in PyVista and PyMOL

<img width="512" alt="Screenshot 2025-07-02 at 5 16 07 PM" src="https://github.com/user-attachments/assets/65410da3-2154-4c2b-8658-bc35466dbdd7" />

This repository contains an .ipynb notebook for the calculation of [Sterimol parameters L, B1, and B5](https://digital-chemistry-laboratory.github.io/morfeus/) from .xyz coordinate files. These vectors can be visualized in PyVista (opened with .ipynb notebook) or printed for use with PyMOL. 

# Anaconda Environment
A .yml file containing all required packages is provided. 
# Running Notebook
The Sterimol Visualization notebook can be opened and run using Visual Studio Code, Jupyter Notebooks, or any other notebook program. Run Imports section. 
Add the path to your .xyz file and modify the atom numbers (1-indexed) to reflect the first and second atoms used to calculate sterimol. 

These sterimol vectors can be visualized in 3D with PyVista in section 3 (opens secondary application) or printed as coordinates for visualization in PyMOL in sections 4 and 5.
Note: MORFEUS uses Van der Waals radii to compute sterimol vector lengths. If the atom radii used for visualization in PyMOL is smaller than Van der Waals radii, these sterimol errors will appear to be longer than they should be. The length of these arrows can be reduced in section 5- treat this with caution, the modified sterimol vector length is ONLY for graphic purposes and not the true vector length. 

Both cells 4 and 5 print a line of code for Sterimol L, B1, and B5. These can be directly copied and pasted into PyMOL. This code is in the format:
```
draw_arrow([vector start x coordinate, vector start y coordinate, vector start z coordinate], [vector end x coordinate, vector end y coordinate, vector end z coordinate], color=(RGB), name='Sterimol_Name')
```
# PyMOL scripts 
Sterimol arrow visuals require the pymol_sterimol.py script be run in current PyMOL session. 
The ['visualize.py' script from the Paton Lab](https://github.com/patonlab/wSterimol/blob/master/wsterimol/visualize.py) can also be loaded for graphics similar to the ones shown here.

These scripts can be added to the PyMOL pymolrc file for automatic activation for each session. Navigate to File > Edit pymolrc, then add the following text:
```
run FilePath/pymol_sterimol.py
run FilePath/visualize.py
```
If using the visualize.py script, run
```
BallnStick all
```
once your molecule is loaded. 

To generate the Sterimol arrow, paste the draw_arrow code from notebook sections 4 or 5 and run in PyMOL. Arrow must first be deleted before rendering a new arrow. 

