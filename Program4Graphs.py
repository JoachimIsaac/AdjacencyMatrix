"""
Name: Joachim Isaac.
Course: CS 2433-101, Fall 19, Dr. Stringfellow.
Purpose: To learned how to solve a problem using a graph:
Using a graph(Acquaintance graph) to find out which
individuals should be introduced to each other.

Important points:(Things I learned):


"""


class Graph(object):

    # Default Constructor.
    def __init__(self,matrix,vertex_values):

        self.__adjacencyMatrix = matrix # 2D list

        self.__vertices = vertex_values # Names

        self.__numNodes = len(matrix) # Number of Nodes of names.


    # Gets the adjacency Matrix.
    def get_adjacencyMatrix(self):
        return self.__adjacencyMatrix

    # Returns an array of the vertices(Names).
    def get_vertices_values(self):
        return self.__vertices

    # Returns the Number of Nodes in the graph.
    def get_numNodes(self):
        return self.__numNodes

    # Sets a new adjacency Matrix (2D array).
    def set_adjacencyMatrix(self, matrix):
        self.__adjacencyMatrix = matrix

    # Sets an array of new vertices.
    def set_vertices_values(self,names):
        self.__vertices = names

    # Sets a new number of nodes.
    def set_numNodes(self,number_of_nodes):
        self.__numNodes = number_of_nodes


    # Adds an edge.
    def addEdge(self, start, end):
        self.__adjacencyMatrix[start][end] = 1


    # Removes an edge.
    def removeEdge(self, start, end):

        if self.__adjacencyMatrix[start][end] == 0:
            outfile.write("There is no edge between %d and %d" % (start, end))
        else:
            self.__adjacencyMatrix[start][end] = 0



    # Returns true if there is an edge at a specific position
    # and it returns false if it doesn't have an edge at that position.
    def containsEdge(self, start, end):

        if int(self.__adjacencyMatrix[start][end]) > 0:

            return True
        else:
            return False



    # Returns a String of the current vertices
    def vertices_to_String(self):
        str_vetices = ""
        for index in range(len(self.__vertices)):
            str_vetices += self.__vertices[index] + " "

        return str_vetices



    # Returns a string of the Adjacency Matrix.
    def ToString(self):
        str_matrix = ""
        temp = ""

        #Iterates through the 2D array.
        for i in range(len(self.__adjacencyMatrix)):
            for j in range(len(self.__adjacencyMatrix[0])):

                # stores value into temp.
                temp = str(self.__adjacencyMatrix[i][j])

                #Stores values with a space into str_matrix.
                str_matrix += temp + " "

                # When we get to the end of a row we as a
                # vertical space "\n".
                if j == len(self.__adjacencyMatrix[i]) - 1:
                    str_matrix += "\n"

        return str_matrix




# Reads all the input from a file and then closes the file.
def read_input_files():
    input_list = []
    file_name = input("Please enter the input file name.\n").strip(" ")

    # Handles both the opening and closing of the file
    # when reading in values.
    with open(file_name, 'r') as read_file:
        for line in read_file:
            input_list.append(line.split())

        return transform_input(input_list)




# This transforms the input into a format that can easily be traversed.
# It changes all single list parts of a matrix into a 2D list form.
def transform_input(input_list):
    result = []
    temp_array = []

    # When the first value in the input list is '0' then
    # it returns the empty array immediately. This means
    # that zero sets have to be checked.
    if input_list[0][0] == '0':
        return result

    # Loops through our input that was read in.
    for position in range(len(input_list)):

        # If the current position has an array with length of 1
        # then we append it to the result array.
        if len(input_list[position]) == 1:
            result.append(input_list[position])

        # if the current position has an array with length of 1 and the following
        # position array is more than 1, append the array of position + 1.
        if len(input_list[position]) == 1 and len(input_list[position + 1]) > 1:
            result.append(input_list[position + 1])
            position += 1

            # Store the following single arrays of matrix values as a 2D array.
            # to form a matrix.
            for index in range(1, int(input_list[position - 1][0]) + 1):
                temp_array.append(input_list[index + position])
            result.append(temp_array)
            temp_array = []

    return result



# This function determines who has to be introduced and
# stores the names separated by an 'and' in a string and
# returns that string.
def determine_introductions(graph):
    list_of_vertices = graph.get_vertices_values()
    matrix = graph.get_adjacencyMatrix()
    checked = []
    results = ""

    # Traverse through the matrix
    for rows in range(len(matrix)):
        for cols in range(len(matrix[0])):

            # If there is no connections at a specific position
            # append the position.
            if (not graph.containsEdge(rows,cols)) and rows != cols:
                checked.append([rows, cols])

    # Update the checked list by removing any duplicate relationships.
    checked = was_visited(checked)

    # Stores the relationships in a string to display them nicely.
    for rows in range(len(checked)):
        results += " " + list_of_vertices[checked[rows][0]] + " and " + list_of_vertices[checked[rows][1]] + "\n"

    return results



# This function takes in an array of the positions
# of people to be introduced. It then looks for duplicates
# and removes the duplicates. i.e 'Tina and Richard' and 'Richard and Tina'
# are the same and do not need to be repeated.
def was_visited(positions):
    results = []

    # Helper function which returns true if
    # the row1 == col2 and row2 == col1.
    # ie. if there is already a duplicate position
    # in the list already
    def contains(results, col, row):
        for index in range(len(results)):
            if results[index][0] == col and row == results[index][1]:
                return True
        return False


    for rows in range(len(positions)):

        # If there is no duplicate currently in the results array
        # then append the position into the results array.
        if not contains(results,positions[rows][1], positions[rows][0]):
            results.append(positions[rows])

    return results



# Reads in input file name and returns a file object.
def open_output_file():
    outfile = input("Please enter output file name: \n").strip(" ")
    file = open(outfile, 'w')
    return file



# This prints all the results in a nicely formatted manner.
def print_results(data_read,outfile):

    set_number = 1

    outfile.write("Name: Joachim Isaac\n")
    outfile.write("Program 4 Discrete Structures and Analysis.\n")
    outfile.write("Acquaintance Graph Program.\n")
    outfile.write("Number of sets to be read: %2s \n\n"%(data_read[0][0]))

    if len(data_read) == 0:
        return outfile.write("The number of sets is Zero, nothing to read.\n")

    # Starts from position 3 of the data_read list
    for position in range(3,(int(data_read[0][0]) * 3) + 1):

        if position <= 3:
            # Creates a graph, and loads it with 2D Matrix and the Vertices.
            current_graph = Graph(data_read[position], data_read[position - 1])

            # Prints the set number , the number of vertices
            # and the vertices values(names)
            outfile.write("Acquaintance Graph %2d :%2d Friends - %2s \n\n" %(set_number, current_graph.get_numNodes(),current_graph.vertices_to_String()))

            # Prints the Adjacency Matrix.
            outfile.write(current_graph.ToString()+"\n")


            outfile.write("Introductions to be made:\n")

            # Prints the introductions that have to be made.
            outfile.write(determine_introductions(current_graph)+"\n\n")

            set_number += 1


        if position > 3:

            # If the sub-array's length is equal to 1
            # then we can enter the if statement.
            if len(data_read[position]) == 1:

                # Creates a graph, and loads it with 2D Matrix and the Vertices.
                current_graph = Graph(data_read[position + 2], data_read[position + 1])

                # Prints the set number , the number of vertices
                # and the vertices values(names)
                outfile.write("Acquaintance Graph %2d :%2d Friends - %2s \n\n" %(set_number, current_graph.get_numNodes(),current_graph.vertices_to_String()))

                # Prints the Adjacency Matrix.
                outfile.write(current_graph.ToString()+"\n")


                outfile.write("Introductions to be made:\n")

                # Prints the introductions that have to be made.
                outfile.write(determine_introductions(current_graph)+"\n\n")

                set_number += 1

    outfile.close()





# Main:

data_read = read_input_files()
outfile = open_output_file()
print_results(data_read,outfile)


