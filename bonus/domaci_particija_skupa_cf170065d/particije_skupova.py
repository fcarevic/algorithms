initial_set = [1,2,3,4,5,6,7,8,9,10]
counter = 0 #counts number of partitions
counter_of_iterations=0 #counts number of recursive calls
IS_TEST=False  #indicator for printing partitions

def print_solution(arr, number_of_subsets, initial_set):
    global counter
    counter=counter+1
    if IS_TEST == False : #if funciton test() is called then print all partitions
       return
    print(str(counter) + "\t\t\t", end=" ") #prints serial number of current partition
    for i in range(number_of_subsets): #prints partition
        for j in range(len(arr)):
            if arr[j]==i:
                print(initial_set[j], end=" ")
        print(" | ", end = " ")
    print(arr)
    print("\n")



def get_next_position(hashmap,arr, position): #gets  position of next element for changing its current partition
    position=position+1
    while position < len(arr) and hashmap[arr[position]]==1: #if there is only one element in partition with serial number of hashmap[arr[position]] , then it can not be moved, so it is passed
        position=position+1
    return position


def partitiion(arr , position,  right,number_of_subsets, initial_set, hashmap):

        global counter_of_iterations
        counter_of_iterations = counter_of_iterations + 1
        if position==len(arr): #for edge case K==1
            print_solution(arr=arr, number_of_subsets=number_of_subsets, initial_set=initial_set)
            return

        arr = arr.copy()
        hashmap=hashmap.copy()


        if right: #if current element should be added to partitions on the right side
            while arr[position] <= (
            min((max(arr[0:position]) + 1), position if position < number_of_subsets - 1 else number_of_subsets - 1)):


                new_position = get_next_position(hashmap, arr, position) #get position of the next element to be moved
                if new_position >= len(arr): #if there are no elemenets that can be moved
                    print_solution(arr=arr, number_of_subsets=number_of_subsets, initial_set=initial_set)

                else:
                    partitiion(arr, new_position, False, number_of_subsets, initial_set, hashmap) #move next element
                    partitiion(arr, new_position, True, number_of_subsets, initial_set, hashmap)  #move next element

                hashmap[arr[position]] = hashmap[arr[position]] - 1
                arr[position] = arr[position] + 1 #move current element to the right
                if(arr[position] >= len(hashmap)):
                    continue
                hashmap[arr[position]] = hashmap[arr[position]] + 1


        else: #if current element should be added to partitions on the left side
            while arr[position] >= 0:

                hashmap[arr[position]] = hashmap[arr[position]] - 1
                arr[position] = arr[position] - 1  #move current element to the left
                if (arr[position] < 0):
                    continue
                hashmap[arr[position]] = hashmap[arr[position]] + 1
                new_position = get_next_position(hashmap, arr, position)
                if new_position >= len(arr):
                    print_solution(arr=arr, number_of_subsets=number_of_subsets, initial_set=initial_set)

                else:
                    partitiion(arr, new_position, False, number_of_subsets, initial_set, hashmap)
                    partitiion(arr, new_position, True, number_of_subsets, initial_set, hashmap)



def initialize(number_of_subsets, initial_set):
    global  counter
    global counter_of_iterations
    counter_of_iterations = 0
    counter=0

    length = len(initial_set)
    initial_partition = []
    initial_hashmap = [0 for x in range(number_of_subsets)]
    for i in range(length):
        set_index = 0 if i < length - number_of_subsets else number_of_subsets - (length - i) #initial partition, eq. S=4, K=3  initial partition =[0,0,1,2]
        initial_hashmap[set_index]= initial_hashmap[set_index] +1  #stores number of elements in kth partition
        initial_partition.append(set_index)
    return {"initial_partition" : initial_partition , "initial_hashmap" : initial_hashmap}


def main():
    global IS_TEST
    IS_TEST = False
    matrix =[[-1 for x in range(len(initial_set))] for y in range(len(initial_set))]
    arr_k = [x+1 for x in range(len(initial_set))]
    for s in arr_k:
        for number_of_subsets in range(1,s+1):
            dict= initialize(number_of_subsets, initial_set[0:s])
            initial_partition = dict["initial_partition"]
            initial_hashmap = dict["initial_hashmap"]

            partitiion(initial_partition, 1, True, number_of_subsets, initial_set[0:s], initial_hashmap)
            #print("LENGTH = " + str(k) + " K =   "+ str(number_of_subsets) +  "  Counter = " + str(counter), end="  ")
            matrix[s-1][number_of_subsets-1] = counter
            #print("Iterations\t" + str(counter_of_iterations))

    print("***************************")
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if(matrix[i][j]!= -1):
             print("S = " + str(i+1) + "\tK = " + str(j+1) + "\tCounter = " + str(matrix[i][j]))
        print()



def test():
    global IS_TEST
    IS_TEST=True
    number_of_subsets=2
    s=4
    dict = initialize(number_of_subsets, initial_set[0:s])
    initial_partition = dict["initial_partition"]
    initial_hashmap = dict["initial_hashmap"]

    partitiion(initial_partition, 1, True, number_of_subsets, initial_set[0:s], initial_hashmap)
    print("LENGTH = " + str(s) + " K =   " + str(number_of_subsets) + "  Counter = " + str(counter))
    #print("Iterations\t" + str(counter_of_iterations))


test()
main()