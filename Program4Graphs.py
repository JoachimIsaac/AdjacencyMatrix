"""



"""


class Graph(object):

    def __init__(self,matrix,vertex_values):
        self.__adjacencyMatrix = matrix  # 2D list
        self.__vertices = vertex_values
        self.__numNodes = len(matrix)

    def get_adjacencyMatrix(self):
        return self.__adjacencyMatrix

    # adds an edge.
    def addEdge(self, start, end):
        self.__adjacencyMatrix[start][end] = 1

    # removes an edge
    def removeEdge(self, start, end):
        if self.__adjacencyMatrix[start][end] == 0:
            print("There is no edge between %d and %d" % (start, end))
        else:
            self.__adjacencyMatrix[start][end] = 0

    def containsEdge(self, start, end):
        if int(self.__adjacencyMatrix[start][end]) > 0:
            return True
        else:
            return False

    def get_vertices_values(self):
        return self.__vertices

    def vertices_to_String(self):
        str_vetices = ""
        for index in range(len(self.__vertices)):
            str_vetices += self.__vertices[index] + " "
        return str_vetices

    def ToString(self):
        str_matrix = ""
        temp = ""
        for i in range(len(self.__adjacencyMatrix)):
            for j in range(len(self.__adjacencyMatrix[0])):

                temp = str(self.__adjacencyMatrix[i][j])

                str_matrix += temp + " "

                if j == len(self.__adjacencyMatrix[i]) - 1:
                    str_matrix += "\n"
        return str_matrix


    def get_numNodes (self):
        return self.__numNodes


def read_input_files():
    input_list = []
    file_name = input("Please enter the input file name.\n")

    # Handles both the opening and closing of the file
    # when reading in values.
    with open(file_name, 'r') as read_file:
        for line in read_file:
            input_list.append(line.split())

        return transform_input(input_list)


def transform_input(input_list):
    result = []
    temp_array = []

    if input_list[0][0] == '0':
        return result

    for position in range(len(input_list)):
        if len(input_list[position]) == 1:
            result.append(input_list[position])
        if len(input_list[position]) == 1 and len(input_list[position + 1]) > 1:
            result.append(input_list[position + 1])
            position += 1

            for index in range(1, int(input_list[position - 1][0]) + 1):
                temp_array.append(input_list[index + position])
            result.append(temp_array)
            temp_array = []

    return result


def print_matrix(matrix):
    str_matrix = ""
    temp = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            temp = str(matrix[i][j])

            str_matrix += temp + " "

            if j == len(matrix[i]) - 1:
                str_matrix += "\n"
    print(str_matrix)


def determine_introductions(graph):
    list_of_vertices = graph.get_vertices_values()
    matrix = graph.get_adjacencyMatrix()
    checked = []
    results = ""

    for rows in range(len(matrix)):
        for cols in range(len(matrix[0])):
            if (not graph.containsEdge(rows,cols)) and rows != cols:
                checked.append([rows, cols])

    checked = was_visited(checked)

    for rows in range(len(checked)):
        results += " "+ list_of_vertices[checked[rows][0]] + " and " + list_of_vertices[checked[rows][1]] + "\n"

    return results


def was_visited(postions):
    results = []

    def is_in(results, col, row):
        for index in range(len(results)):
            if results[index][0] == col and row == results[index][1]:
                return True
        return False

    for rows in range(len(postions)):
        if not is_in(results,postions[rows][1], postions[rows][0]):
            results.append(postions[rows])
    return results


# def was_visited(postions,current_r,current_c):
#     for rows in range(len(postions)):
#         if int(postions[rows][0]) == current_r and int(postions[rows][1]) == current_c:
#             return True
#         if int(postions[rows][0]) == current_c and int(postions[rows][1]) == current_r:
#             return True
#         else:
#             return False








def print_results(data_read):
    set_number = 1
    print("Name: Joachim Isaac")
    if len(data_read) == 0:
        return print("The number of sets is Zero, nothing to read.")


    for position in range(3,len(data_read)):
        if position <= 3:
            current_graph = Graph(data_read[position], data_read[position - 1])

            print("Acquaintance Graph %2d :%2d Friends - %2s \n" % (set_number, current_graph.get_numNodes(),current_graph.vertices_to_String()))
            print(current_graph.ToString())
            print("Introductions to be made: ")
            print(determine_introductions(current_graph)+"\n\n")
        if position > 3:
            if len(data_read[position]) == 1:
                current_graph = Graph(data_read[position + 2], data_read[position + 1])
                print("Acquaintance Graph %2d :%2d Friends - %2s \n" % (set_number, current_graph.get_numNodes(), current_graph.vertices_to_String()))
                print(current_graph.ToString())
                print("Introductions to be made: ")
                print(determine_introductions(current_graph))




        #introductions:




        set_number += 1


        #then loop...






data_read = read_input_files()
print_results(data_read)


