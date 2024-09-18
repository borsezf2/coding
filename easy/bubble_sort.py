
#  i j 
# [4,2,7,5]

def bubble_sort(array):

    for i in range(0,len(array)-1):
        isSorted = True
        # print(isSorted)
        for j in range(0,len(array)-1-i):
            
            if array[j+1] < array[j]:
               temp = array[j]
               array[j] = array[j+1]
               array[j+1] = temp

               isSorted = False
            # print(isSorted)
        # print(array)
        # print("CB= ",isSorted)
        if isSorted==True:
            # print("break")
            break

    return array

test_array = [4,2,7,5]

print(bubble_sort(test_array))