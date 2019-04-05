import pymesh
import pymesh.meshio
import pymesh.meshutils
import pymesh.triangulate
import numpy as np

mesh=pymesh.load_mesh("/home/tansin/Downloads/noisy_models/noisy_bunny.obj")
mesh.enable_connectivity()

listOfVertices = mesh.vertices
listOfFaces = mesh.faces
print(listOfFaces)
print(listOfVertices)
mesh.add_attribute('face_area')
listOfFacesAreas = mesh.get_attribute('face_area')
#print(mesh.get_attribute('face_area')[0])

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

for i in range(1,50):
    positions = [];
    for vertex_V in range(len(listOfVertices)):
        if vertex_V in boundaryVertices:
            continue

        xPosition = 0
        yPosition = 0
        zPosition = 0
        vertex_new = []
        totalweight = 0;

        adjacentOfVertex = mesh.get_vertex_adjacent_vertices(vertex_V)
        adjacentfaces_of_vertex_V = mesh.get_vertex_adjacent_faces(vertex_V)

        twoFaceIncidentWeight = 0;
        for vertex_U in adjacentOfVertex:

            adjacentfaces_of_vertex_U = mesh.get_vertex_adjacent_faces(vertex_U)

            common = np.intersect1d(adjacentfaces_of_vertex_V, adjacentfaces_of_vertex_U)
            print(common)
            for faceIdx in common:
                twoFaceIncidentWeight += listOfFacesAreas[faceIdx]

            adjacentList = (listOfVertices[vertex_U])

            xPosition += adjacentList[0] * twoFaceIncidentWeight
            yPosition += adjacentList[1] * twoFaceIncidentWeight
            zPosition += adjacentList[2] * twoFaceIncidentWeight
            totalweight += twoFaceIncidentWeight

        xPosition = xPosition/totalweight
        yPosition = yPosition/totalweight
        zPosition = zPosition/totalweight

        vertex_new.append(xPosition)
        vertex_new.append(yPosition)
        vertex_new.append(zPosition)

        listOfVertices[vertex_V] = vertex_new


new_mesh = pymesh.form_mesh(listOfVertices, mesh.faces)
pymesh.meshio.save_mesh("output/new_bunny_boundary.obj", new_mesh)


