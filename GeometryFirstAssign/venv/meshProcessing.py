import pymesh
import pymesh.meshio
import pymesh.meshutils
import pymesh.triangulate
import numpy as np

mesh=pymesh.load_mesh("/home/tansin/Downloads/noisy_bunny.obj");
mesh.enable_connectivity();


listOfVertices = mesh.vertices;
listOfFaces = mesh.faces;
print(listOfFaces);
print(listOfVertices);

for i in range(1,12):
    positions = [];
    for vertex_V in range(len(listOfVertices)):
        xPosition = 0;
        yPosition = 0;
        zPosition = 0;
        vertex_new = [];
        print (vertex_V);
        adjacentOfVertex = mesh.get_vertex_adjacent_vertices(vertex_V);
        adjacentFacesOfV = mesh.get_vertex_adjacent_faces(vertex_V);
        print (adjacentOfVertex);

        count = 0;
        for vertex_U in adjacentOfVertex:
            print(vertex_U)
            adjacentList = (listOfVertices[vertex_U]);
            adjacentFacesOfU = mesh.get_vertex_adjacent_faces(vertex_U);
            commonFaces = np.intersect1d(adjacentFacesOfV,adjacentFacesOfU);

            if len(commonFaces) == 1:
                continue
            xPosition += adjacentList[0];
            yPosition += adjacentList[1];
            zPosition += adjacentList[2];
            count = count + 1;

        xPosition = xPosition/count;
        yPosition = yPosition/count;
        zPosition = zPosition/count;

        vertex_new.append(xPosition);
        vertex_new.append(yPosition);
        vertex_new.append(zPosition);

        listOfVertices[vertex_V] = vertex_new
        #positions.append(vertex_new);


    #mesh.vertices = positions;
    new_mesh = pymesh.form_mesh(listOfVertices, mesh.faces)
pymesh.meshio.save_mesh("new_bunny.obj", new_mesh)
#print (listOfVertices);

#print(mesh.num_vertices,mesh.num_faces,mesh.num_voxels);