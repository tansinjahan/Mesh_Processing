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

facesOnBoundary = []
for faces_V in range(len(listOfFaces)):
    listOfAdjacentFaces = mesh.get_face_adjacent_faces(faces_V)
    if len(listOfAdjacentFaces) < 3:
        facesOnBoundary.append(faces_V)

print(facesOnBoundary)

boundaryVertices = []
for faceIdx in facesOnBoundary:
    face = listOfFaces[faceIdx]
    degree1 = len(mesh.get_vertex_adjacent_vertices(face[0]))
    degree2 = len(mesh.get_vertex_adjacent_vertices(face[1]))
    degree3 = len(mesh.get_vertex_adjacent_vertices(face[2]))
    highest = max(degree1, degree2, degree3)
    print(str(highest) + ": " + str(degree1) + ", " + str(degree2) + ", " + str(degree3))
    if highest == degree1:
        boundaryVertices.append(face[1])
        boundaryVertices.append(face[2])
    elif highest == degree2:
        boundaryVertices.append(face[0])
        boundaryVertices.append(face[2])
    else:
        boundaryVertices.append(face[0])
        boundaryVertices.append(face[1])

print(boundaryVertices)

# list of faces gives you an array of face_row consist of vertec positions
#
# [[1,2,3],
# [2,3,5]]
# adjacent face of 0, output: [1 6 7 8 9] consist of indexes in face array

#print(listOfAdjacentFaces)

for i in range(1,12):
    positions = [];
    for vertex_V in range(len(listOfVertices)):
        if vertex_V in boundaryVertices:
            continue

        xPosition = 0
        yPosition = 0
        zPosition = 0
        vertex_new = []
        adjacentOfVertex = mesh.get_vertex_adjacent_vertices(vertex_V)

        for vertex_U in adjacentOfVertex:
            print(vertex_U)
            adjacentList = (listOfVertices[vertex_U]);

            xPosition += adjacentList[0];
            yPosition += adjacentList[1];
            zPosition += adjacentList[2];

        xPosition = xPosition/len(adjacentOfVertex)
        yPosition = yPosition/len(adjacentOfVertex)
        zPosition = zPosition/len(adjacentOfVertex)

        vertex_new.append(xPosition);
        vertex_new.append(yPosition);
        vertex_new.append(zPosition);

        listOfVertices[vertex_V] = vertex_new


new_mesh = pymesh.form_mesh(listOfVertices, mesh.faces)
pymesh.meshio.save_mesh("new_bunny.obj", new_mesh)


