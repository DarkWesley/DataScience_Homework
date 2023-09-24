initial_status = {'人': 0, '羊': 0, '狼': 0, '菜': 0}
target_status = {'人': 1, '羊': 1, '狼': 1, '菜': 1}
doneState = [0] * 16
answers = []
route = []
def move(status, item):
    new_status = status.copy()
    new_status['人'] = 1 - new_status['人']
    new_status[item] = 1 - new_status[item]
    return new_status

def boat(status):
    new_status = status.copy()
    new_status['人'] = 1 - new_status['人']
    return new_status

def is_valid(status):
    if (status['狼'] == status['羊'] or status['羊'] == status['菜']) and status['人'] != status['羊']:
        return False
    return True

def DFS(status):
    if (status == target_status):
        answers.append(route[:])
        return
    if not is_valid(status):
        return
    stateIdx = (status['人'] << 3) + (status['羊'] << 2) + (status['狼'] << 1) + status['菜']
    if (doneState[stateIdx] == 1):
        return
    else:
        doneState[stateIdx] = 1

    if (status['人'] == status['羊']):
        new_status = move(status,'羊')
        route.append("sheep " + str(status['羊']) + "->" + str(new_status['羊']))
        DFS(new_status)
        route.pop()
    if (status['人'] == status['狼']):
        new_status = move(status, '狼')
        route.append("wolf " + str(status['狼']) + "->" + str(new_status['狼']))
        DFS(new_status)
        route.pop()
    if (status['人'] == status['菜']):
        new_status = move(status, '菜')
        route.append("vegetable " + str(status['菜']) + "->" + str(new_status['菜']))
        DFS(new_status)
        route.pop()
    new_status = boat(status)
    route.append("empty " + str(status['人']) + "->" + str(new_status['人']))
    DFS(new_status)
    route.pop()

    doneState[stateIdx] = 0


DFS(initial_status)
for answer in answers:
    print(answer)


