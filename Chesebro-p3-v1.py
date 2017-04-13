#########################################################
#
# Python 3.6
# Author: Marc Chesebro
#
#########################################################


#edge object containing the start and end point
class edge(object):
    def __init__(self, vertA, vertB):
        self.A = vertA
        self.B = vertB

class vertex(object):
    def __init__(self, label):
        self.label = label

#function to find the degree of a vertex given a name
#and list of edges
def findDegree(vert, edgeList):
    deg = 0
    for e in edgeList:
        if(e.A == vert or e.B == vert):
            deg = deg + 1
    return deg

#checks if val is in the list
def contains(val, list):
    for i in list:
        if i == val:
            return True
    return False

def labelToVertex(label, vertList):
    for v in vertList:
        if v.label == label:
            return v
    return -1

def isReflexive(verts, edges):
    for v in verts:
        hasLoop = False
        for e in edges:
            if e.A == v.label and e.B == v.label:
                hasLoop = True
                break
        if not hasLoop:
            return False
    return True


def isSymmetric(edges):
    for e in edges:
        hasSym = False
        for e2 in edges:
            if e.A == e2.B and e.B == e2.A:
                hasSym = True
                break
        if not hasSym:
            return False
    return True


#get user input
userVerts = input("enter the vertices(a, b, c): \n")
userEdges = input("enter the edges((a,b), (b,c)): \n")

#get rid of spaces and split on commas
userVerts = userVerts.replace(" ", "")
userEdges = userEdges.replace(" ", "")
userEdges = userEdges.replace("(", "")
userEdges = userEdges.replace(")", "")

vertsStr = userVerts.split(',')
edgesStr = userEdges.split(',')

verts = []
for str in vertsStr:
    verts.append(vertex(str))

#turn the edge strings into a list of edge objects
edges = []
x = 0
p = edgesStr[0]
for str in edgesStr:
    if not (x == 0):
        edges.append(edge(p, str))
        x = 0
    else:
        x = 1
    p = str

print("Reflexive: ", isReflexive(verts, edges))
print("Symmetric: ", isSymmetric(edges))

