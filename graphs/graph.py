from collections import deque

graph = {}

graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'johnny']
graph['anuj'] = []
graph['thom'] = []
graph['peggy'] = []
graph['johnny'] = []


def person_name_is_three_lettered(person):
    return len(person) == 3


def person_is_seller(person):
    return person[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller")
                return True

            else:
                search_queue += graph[person]
                searched.append(person)
    
    return False


search('you')