def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name) as file:
        data1 = file.read()
        print(data1)
        return data1
    raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name) as file:
        data2 = file.readlines()
        return data2
    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    file_contents_split = file_contents.split("\n")[0]
    with open(output_filename, "w") as file:
        file.write(file_contents_split)
    return
    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE
    data4 = []
    with open(file_name) as file:
        data3 = file.readlines()
        x = 1
        for i in data3:
            if (x % 2 == 0):
                data4.append(i)
            x +=1
    return data4
    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    data6 = []
    with open(file_name) as file:
        data5 = file.readlines()
        for x in range(len(data5)-1,-1,-1):
            data6.append(data5[x])
    return data6
    raise NotImplementedError()

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("week-2/errorExceptionFiles/sampletext.txt")
    print(read_file_into_list("week-2/errorExceptionFiles/sampletext.txt"))
    write_first_line_to_file(file_contents, "week-2/errorExceptionFiles/online.txt")
    print(read_even_numbered_lines("week-2/errorExceptionFiles/sampletext.txt"))
    print(read_file_in_reverse("week-2/errorExceptionFiles/sampletext.txt"))

if __name__ == "__main__":
    main()