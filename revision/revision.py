def count_pairs(list,desired_sum):
    return_val = []
    for num in list:
        for second_num in list:
            if (num + second_num) == desired_sum and list.index(num) != list.index(second_num):
                return_val.append(tuple(sorted((num,second_num))))
    return set(return_val)

def print_list(list):
    list_lentgh = len(list)
    if list_lentgh != 0:
        print(str(list_lentgh) +" items in list")
    else:
        print("List does not contain any items")



if __name__ == "__main__":
    list = [5,4,3,6]
    x = count_pairs(list,10)
    print(x)
    print_list(x)
