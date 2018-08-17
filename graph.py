#way of denoting graph by adjacency list

class graph:
    def __init__(self, graphdict = None):
        if graphdict is None :
            self.graphdict = {}
        else:
            self.graphdict = graphdict
    
    def addvrtx(self,avrtx):
        if avrtx not in self.graphdict:
            self.graphdict[avrtx] = []
    
    def addedge(self,edge):
        edge = set(edge)
        (vrtx1,vrtx2) = tuple(edge)
        if vrtx1 in self.graphdict:
            self.graphdict[vrtx1].append(vrtx2)
        else:
            self.graphdict[vrtx1] = [vrtx2]

    def displayv(self):
        return list(self.graphdict.keys())

    def displaye(self):
        temp = []
        for vrtx in self.graphdict:
            for evrtx in self.graphdict[vrtx]:
                if {vrtx , evrtx} not in temp:
                    temp.append({vrtx , evrtx})
        return temp

g = graph()
g.addvrtx("a")
g.addvrtx("b")
g.addvrtx("c")
g.addvrtx("d")
g.addvrtx("e")


g.addedge(["a","b"])
g.addedge(["b","d"])
g.addedge(["d","e"])
g.addedge(["e","c"])
g.addedge(["c","a"])
g.addedge(["c","b"])
g.addedge(["c","d"])
g.addedge(["e","b"])

print(g.displayv())
print("\n")
print(g.displaye())



