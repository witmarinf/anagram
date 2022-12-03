import itertools
def createAnagrams(name):
    lista = ["".join(perm) for perm in itertools.permutations(str(name))]
    setOfAnagrams = set(lista)
    return setOfAnagrams

def setToFile(name):
    with open("zadania.txt", "w") as file:
        setA = createAnagrams(name)
        listA = list(setA)
        for x in listA:
            file.write(str(x)+"\n")

setToFile("anagram")
