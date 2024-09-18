

def is_sum_dict(a,target):
    seen = {}
    
    for num in a:
        
        try:
            need = target - num
            if seen[need] == 1:
                print(need)
                print(num)
                print(target)
                return True
        except:
            seen[num] = 1
        
    else:
        print(seen)
        return False


def is_sum_sorted_array(a,target):
    a = sorted(a)

    left_i = 0
    right_i = len(a) - 1

    while left_i<right_i:
        if (a[left_i] + a[right_i]) == target:
            print(a[left_i] ," ", a[right_i])
            return True
        elif (a[left_i] + a[right_i]) > target:
            right_i -= 1
        elif (a[left_i] + a[right_i]) < target:
            left_i += 1

    return False




arr = [5,2,-1,9,11,5]

print(is_sum_dict(arr,19))

print("sorted array = ", is_sum_sorted_array(arr,10))
