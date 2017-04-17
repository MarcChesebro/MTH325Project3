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

#class object holding the label
class vertex(object):
    def __init__(self, label):
        self.label = label

#checks if there is a relation from vert1 to vert2
def isRelated(vert1, vert2, edges):
    for e in edges:
        if e.A == vert1 and e.B == vert2:
            return True
    return False

#checks if every vertex is related to itself
def isReflexive(verts, edges):
    for v in verts:
        if not isRelated(v.label, v.label, edges):
            return False
    return True

#checks if every edge has a reverse counterpart
def isSymmetric(edges):
    for e in edges:
        if not isRelated(e.B, e.A, edges):
            return False
    return True

#checks to see if the graph is antisymmetric
def isAntisymmetric(edges):
    for e in edges:
        if isRelated(e.B, e.A, edges) and not e.A == e.B:
            return False
    return True

#checks to see if the graph is transitive
def isTransitive(edges):
    for e in edges:
        isTran = False
        for e2 in edges:
            if e.B == e2.A and not isRelated(e.A, e2.B, edges):
                return False
    return True

#finds the adjacency matrix of the transitive enclosure of the graph
def findTransitiveEnclosure(verts, edges):
    m = [[0 for x in range(len(verts))] for x in range(len(verts))]
    for x in range(len(verts)):
        for y in range(len(verts)):
            if isRelated(verts[x].label, verts[y].label, edges):
                m[x][y] = 1
    for k in range(len(verts)):
        for x in range(len(verts)):
            for y in range(len(verts)):
                if m[x][y] == 1:
                    for i in range(len(verts)):
                        if m[y][i] == 1:
                            m[x][i] = 1

    print("")
    print("Transitive enclosure:")
    for x in range(len(verts)):
        print(verts[x].label, m[x])

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
print("Transitive: ", isTransitive(edges))
print("Antisymmetric: ", isAntisymmetric(edges))
findTransitiveEnclosure(verts, edges)