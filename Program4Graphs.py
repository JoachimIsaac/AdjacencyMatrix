"""



"""


class Graph(object):
    # def __init__(self, numNodes):
    #     self.adjacencyMatrix = []  # 2D list
    #     for i in range(numNodes):
    #         self.adjacencyMatrix.append([0 for i in range(numNodes)])
    #     self.numNodes = numNodes

    def __init__(self, matrix):
        self.adjacencyMatrix = matrix # 2D list
        self.numNodes = len(matrix)

    def addEdge(self, start, end):
        self.adjacencyMatrix[start][end] = 1

    def removeEdge(self, start, end):
        if self.adjacencyMatrix[start][end] == 0:
            print("There is no edge between %d and %d" % (start, end))
        else:
            self.adjacencyMatrix[start][end] = 0

    def containsEdge(self, start, end):
        if self.adjacencyMatrix[start][end] > 0:
            return True
        else:
            return False

    def __len__(self):
        return self.numNodes






def read_input_files():
    input_list = []
    file_name = input("Please enter the input file name.\n")

    # Handles both the opening and closing of the file
    # when reading in values.
    with open(file_name, 'r') as read_file:
        for line in read_file:
            input_list.append(line.split())

        return transform_input(input_list)


def transform_input(array):
    result = []
    temp_array = []

    for position in range(len(array)):
        if len(array[position]) == 1:
            result.append(array[position])
        if len(array[position]) == 1 and len(array[position + 1]) > 1:
            result.append(array[position + 1])
            position += 1

            for index in range(1, int(array[position - 1][0]) + 1):
                print(index)
                temp_array.append(array[index + position])
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


arr = read_input_files()

print(arr[6])
print_matrix(arr[6])
