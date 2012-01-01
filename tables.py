import random

class KoffinNode:
    def __init__(self, letter):
        self.letter = letter
        self.count = 0
        self.dict = {}

    def add(self, remainder):
        self.count = self.count + 1
        if remainder:
            l = remainder[0]
            if not l in self.dict:
                self.dict[l] = KoffinNode(l)
            self.dict[l].add(remainder[1:])

    def dump(self,prefix):
        print prefix+self.letter+" "+str(self.count)
        for l in self.dict:
            self.dict[l].dump(prefix+self.letter)

    def getNext(self,prefix):
        if prefix:
            l = prefix[0]
            if l in self.dict:
                return self.dict[l].getNext(prefix[1:])
            else:
                print "fail?"
                return "-"
        s = sum([v.count for v in self.dict.values()])
        v = random.randint(0,s-1)
        for (l,n) in self.dict.items():
            if v < n.count:
                return l
            else:
                v = v - n.count
        print "faaaail"
        return "!"

class koffinState:
    def __init__(self, root, start):
        self.s = start
        self.root = root
    def next(self):
        l = root.getNext(self.s)
        self.s = self.s[1:] + l
        return l

def buildKoffin(path,depth):
    f = open(path)
    text = f.read().replace("\n","").replace("\t","")
    root = KoffinNode("-")
    for i in range(0,len(text)-depth):
        clip = text[i:i+depth]
        root.add(clip)
    return root

import sys
path = sys.argv[1]
root = buildKoffin(path,4)
state = koffinState(root,"tho")
a = "tho"
for i in range(100):
    a = a + state.next()

print a


