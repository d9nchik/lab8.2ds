from operator import itemgetter


def get_data():
    data = []
    with open("input.txt") as iFile:
        while True:
            line = iFile.readline()
            if not line:
                break
            temp = list(map(int, (line[:len(line)] + line[len(line) + 1:]).split()))
            data.append(temp)
    number_of_heights = data[0][0]
    del data[0]
    return sorted(data, key=itemgetter(2)), number_of_heights  # Sort for priority queue


def node_note_updater(node_note, start_node, finish_node):
    if start_node > finish_node:
        temp = start_node
        start_node = finish_node
        finish_node = temp
    start_position = -1
    for x in range(len(node_note)):
        if start_node in node_note[x] and finish_node in node_note[x]:
            return False
        if start_node in node_note[x]:
            start_position = x
        elif finish_node in node_note[x]:
            node_note[start_position].extend(node_note[x])
            del node_note[x]
            return True


def crascal_algorithm(e_data, number_of_heights):
    size = number_of_heights
    node_note = []
    for x in range(size):
        node_note.append([x + 1])
    list_of_connection = []
    for connection in e_data:
        if node_note_updater(node_note, connection[0], connection[1]):
            list_of_connection.append(connection)
    return list_of_connection


def show_list_of_connection(list_of_connection):
    print("Список ребер, які залишаться в кістяковому дереві")
    for connection in list_of_connection:
        print("%d->%d з вагою %d" % (connection[0], connection[1], connection[2]))


data, numberOfHeights = get_data()
listOfConnection = crascal_algorithm(data, numberOfHeights)
show_list_of_connection(listOfConnection)
