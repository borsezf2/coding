
# [2,4,5,7]

# key=3 , key_val= 5
# i = 2


def insertion_sort(array):

    for key in range(1,len(array)):
        key_val = array[key]
        i = key - 1
        while i >=0 and array[i]>array[key]:
            array[i+1] = array[i]
            i = i-1
        i = i+1
        array[i] = key_val

    return array


test_array = [4,2,7,5]

print(insertion_sort(test_array))
        
    

