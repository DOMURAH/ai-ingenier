from collections import deque

def large_name(name):
    return len(name) >= 7

graph = {}
graph['Domurah'] = ['Elinoh','Toussin',"Fitahiana"]
graph['Elinoh'] = ['TenchBoy','Alex','Mouta']
graph['Toussin'] = ['Olivia']
graph['Fitahiana'] = ['Onja','Ryan']
graph['TenchBoy'] = []
graph['Alex'] = []
graph['Mouta'] = []
graph['Olivia'] = []
graph['Onja'] = []
graph['Ryan'] = []

struct = deque()
struct += graph['Domurah']

while struct:
    visited = set()
    person = struct.popleft()
    if person not in visited:
        if large_name(person):
            print(f"Personne avec un nom longue trouvé : {person} !")
            break
        else:
            struct += graph[person]
            visited.add(person)