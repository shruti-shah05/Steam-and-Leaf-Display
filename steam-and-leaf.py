# DSC 430 : Python Programming
# Assignment 0202 : steam-and-leaf plot
# Name : Shruti Shah
# Data : 09/28/2020


import sys

# The greetUser() function prints a message to greet the user.
def greetUser():
    # Greeting the user
    print("\nHello.")
    print("Stem-and-leaf plot is a device for presenting quantitative data in a graphical")
    print("format, to assist in visualizing the shape of a distribution.")
    print("Please follow the instructions, the program will read appropriate data file")
    print("and display steam-and-leaf plot based on the number you enter.\n")


#The getInputs() function ask the user to enter either 1,2,3 or to type exit to end the program and it return the user input.
def getInputs():
    # Ask the user to input 1,2, or 3
    userInput = input('Please enter either 1,2, and 3 or type exit to exit the program: ')
    return userInput
   

def fileHandler(value):
    """
    The fileHandler() function will exit out of the program is the user enters "exit" in lower or upper case. 
    It will open and read the file data depending on what the user enters in getInputs() function and it will return the fileData.

    """
    if value.lower() == "exit":
        print("Exiting the program..")
        sys.exit()
   
    if(value == "1"):               #if the user enters 1
        filename = "C:/Users/shruti/source/repos/Hw2/StemAndLeaf1.txt"                      #file path for SteamAndLeaf1.txt file
        with open(filename) as f:
            fileData = f.read().splitlines()            #reads the file data
       

    if(value == "2"):
        filename = "C:/Users/shruti/source/repos/Hw2/StemAndLeaf2.txt"
        with open(filename) as f:
            fileData = f.read().splitlines()
       
    if(value == "3"):
        filename = "C:/Users/shruti/source/repos/Hw2/StemAndLeaf3.txt"
        with open(filename) as f:
            fileData = f.read().splitlines()
       

    return fileData
   
 
# The numberbasedleafSize() function adds zeros to one depending on the leafsize and returns num
def numberbasedleafsize(leafsize):
    num = str(1)
    for i in range(leafsize):
         num = str(num) + str(0)
    return num

# The unique() returns the unique numbers from a list. ex.=> [1,1, 2,2,2,2,5,5,5] to [1,2,5]
def unique(data):  
    setList = set(data)
    return (list(setList))

# The sortingData() function sorts the data
def sortingData(fileData):
    fileData.sort(key=int)
    return fileData


# The getLeafSize() function Checks the size of minimum data and compares with the maximum data based on the result, it determines the leaf size. 
def getLeafSize(data):
    minLenofnumber = len(str(min(data)))
    maxLenofnumber = len(str(max(data)))
    if(int(minLenofnumber) == 1 and int(maxLenofnumber) == 1) or (int(minLenofnumber) == 2 and int(maxLenofnumber) == 2):
        return 1
    elif(int(minLenofnumber) == 2 and int(maxLenofnumber) == 3) or (int(minLenofnumber) == 3 and int(maxLenofnumber) == 2) or (int(minLenofnumber) == 3 and int(maxLenofnumber) == 4) or (int(minLenofnumber) == 4 and int(maxLenofnumber) == 3):
        return 2
    elif(int(minLenofnumber) == 4 and int(maxLenofnumber) == 5) or (int(minLenofnumber) == 5 and int(maxLenofnumber) == 4):
        return 3

# The getStems() function gerenates stem from the sorted list and returns the stem values. ex.-> [421, 428, 429, 430, 433, 455, 458, 459] to [42, 42, 42, 43, 43, 45, 45,45]    
def getStems(data, leafSize):
    stems = []
    num = numberbasedleafsize(leafSize)
     
    for i in range(len(data)):
        stem = int(data[i]) // int(num)   
        stems.append(stem)
    return stems

# The getLeaves() function creates list of list which contains the leaves values from sorted list. ex. => [421, 428, 429, 430, 433, 455, 458, 459] -> [[1, 8, 9],[0, 3],[5, 8, 9]]
def getLeaves(data, stems, leafSize):        
    temp = []  #temp = [[1, 8, 9]]
    skip = 0
    num = numberbasedleafsize(leafSize)
   
    for i in range(len(data)):    #first loop - creates empty brackets and adds it to temp list
       temp.append([])
       if(int(data[i])//int(num) == stems[i]):          
            for j in range(len(data)):    #second loop - appends leafs as list to temp list
                j = skip              
                temp[i].append(int(data[j]) % int(num))
                if(j ==len(data)-1):   #checks last index and returns temp list
                    return temp        
                elif(int(data[j])//int(num) != int(data[j+1])//int(num)):  #compares the current element stem  to next element stem
                    skip = skip + 1
                    break
                skip = skip + 1  
       else:
           continue
 
# The displayStemAndLeafPlot() displays the plot
def displayStemAndLeafPlot(unique_stems, listsOfLeaves):
    unique_stems = unique(unique_stems)
    for i in range(len(unique_stems)):
        if(i == len(unique_stems)-1):     #covers out of index error -
           
            print(str(unique_stems[i]) + "|", end="")              #prints the stem value for the current iteration 

            # for the current iteration, prints the leaf value
            for a in listsOfLeaves[i]:
                print(str(a) + " " , end="")
            print("")
            return
        if(unique_stems[i] == unique_stems[i+1] - 1):  #check if current element and next element is one difference away and if so, print the current element and moves to next iteration
           
            print(str(unique_stems[i]) + "|", end="")
            for a in listsOfLeaves[i]:
                print(str(a) + " " , end="")
            print("")
        else:  #prints empty stems -> subtracts next element to current ele and iterates over the result value to print the empty stems
           
            print(str(unique_stems[i]) + "|", end="")
            for a in listsOfLeaves[i]:
                print(str(a) + " " , end="")
            print("")
            temp = 1
            while(temp != (unique_stems[i+1] - unique_stems[i])):
                 print(str(unique_stems[i] + temp) + "| ", end="")
                 print("")
                 temp = temp + 1
       

#This is the master function which calls all the functions
def main():
    while(True):
        greetUser()
        userValue = getInputs()             #calling the getInput() function
        data = fileHandler(userValue)       #caling fileHandler() function
        sortedData = sortingData(data)            #calling sortingData() function
        leafSize = getLeafSize(sortedData)        #calling helper function()
        stems = getStems(sortedData, leafSize) 
        listsOfLeaves = getLeaves(sortedData, stems, leafSize) 
        displayStemAndLeafPlot(stems, listsOfLeaves)        # calling displayStemandLeafPlot() function

    
main()

