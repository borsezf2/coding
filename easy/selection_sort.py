

# [2,4,7,5]

i = 2
s = 3
j = 3

def selection_sort(array):
    
    for i in range(0, len(array)-1):
        smallest = i

        for j in range(i+1,len(array)):
            if array[j] < array[smallest]:
                smallest = j

        array[i] , array[smallest] = array[smallest], array[i]

    return array

test_array = [4,2,7,5]

print(selection_sort(test_array))