## This repository contains three different algorithms for Mesh Smooting
1. Basic mesh smoothing implementation. 
> The program loads a mesh from a file, smooths the mesh by moving each vertex to the average of its neighbors, and then saves the mesh into another file. Care is taken to update the vertex positions only at the end of an iteration.

2. Weighting schemes. 
> The program provides the alternative weighting scheme using triangle areas.

3. Boundary preservation.
> The program provides an option to preserve the boundaries (holes) of the meshes during smoothing.

##### run instruction - python <filename.py>

![Smooth mesh](https://github.com/tansinjahan/Mesh_Processing/tree/master/GeometryFirstAssign/venv/screenshot)

