# question 1: sum nested list of integers
def ques1_ver1(arr):
    return sum(sum(arr, []))

def ques1_ver2(arr):
    sum = 0
    for inner_arr in arr:
        for integer in inner_arr:
            sum += integer
    return sum

# question 2a: return reversed version of a string
def ques2_a_ver1(str):
    return str[::-1]

def ques2_a_ver2(str):
    new_str = ""
    for i in range(len(str), 0, -1):
        new_str += str[i-1]
    return new_str

# question 2b: return reversed version of a loop that may be nested
def ques2_b_ver1(li):
    for thing in li:
        if type(thing) == list:
            thing.reverse()
    li.reverse()
    return li

def ques2_b_ver2(li):
    new_list = li[::-1]
    for thing in new_list:
        if type(thing) == list:
            new_list[new_list.index(thing)] = thing[::-1]
    return new_list

# question 2c: return reversed version of a tuple
def ques2_c_ver1(tup):
    return tup[::-1]

def ques2_c_ver2(tup):
    new_tup = ()
    for i in range(len(tup), 0, -1):
        new_tup += (tup[i-1],)
    return new_tup

# question 3a: return an ordered union of all the sets in a tuple
def ques3_a_ver1(tup): # not allowing double chars or numbers (every element in answer is unique)
    char_set = set() # we can do {*()} to creat an empty set
    num_set = set()
    for i in range(0, len(tup), 1):
        if len(tup[i]) == 0:
            continue
        for a in tup[i]:
            break
        if type(a) == str:
            char_set = char_set.union(tup[i])
        else:
            num_set = num_set.union(tup[i])
    return sorted(list(char_set)) + sorted(list(num_set))

def ques3_a_ver2(tup): # allowing double chars or numbers (may be two identical elements in answer)
    num_list = []
    char_list = []
    for i in range(0, len(tup), 1): 
        if len(tup[i]) == 0:
            continue
        temp_list = list(tup[i])
        if type(temp_list[0]) == str:
            char_list += temp_list
        else:
            num_list += temp_list
    return sorted(char_list) + sorted(num_list)

# question 3b: return a dictionary of all the sets in a tuple (using question 3a)
def ques3_b(tup):
    all_list = ques3_a_ver1(tup)
    all_dic = {}
    for i in range(0, len(all_list), 1):
        all_dic[i] = all_list[i]
    return all_dic

# question 4a: if without if
def ques4_a_ver1(): # with while loop
    x = int(input("please enter a number "))
    y = 9
    while(x > 10):
        y = 6
        break
    return y

def ques4_a_ver2(): # with for loop
    x = int(input("please enter a number "))
    y = 9
    for i in range(10, x, 1):
        y = i - 4   # i = 10, i is constant. we use it to prevent "Unused variable 'i'" warning
        break    
    return y

def ques4_a_ver1_for_assert(x): # function for assert (without input)
    y = 9
    while(x > 10):
        y = 6
        break
    return y

def ques4_a_ver2_for_assert(x): # function for assert (without input)
    y = 9
    for i in range(10, x, 1):
        y = i - 4
        break    
    return y

# question 4b: if in one line
def ques4_b(x):
    y = 6 if x > 10 else 9
    return y

# question 5a: even numbers only with for loop
def ques5_a_ver1():
    num1 = int(input("please enter first number "))
    num2 = int(input("please enter second number "))
    for i in range(0, num1%2, 1):
        num1 += 1 + i   # i = 0, i is constant. we use it to prevent "Unused variable 'i'" warning
    for i in range(0, num2%2, 1):
        num2 -= 1 + i   # i = 0, i is constant. we use it to prevent "Unused variable 'i'" warning
    for i in range(num2, num1 - 1, -2): # descending order
        print(i)
    for i in range(num1, num2 + 1, 2):  # ascending order
        print(i)

def ques5_a_ver1_for_assert(num1, num2): # function for assert (returns list)
    for i in range(0, num1%2, 1):
        num1 += 1 + i 
    for i in range(0, num2%2, 1):
        num2 -= 1 + i   
    return [i for i in range(num2, num1 - 1, -2)] + [i for i in range(num1, num2 + 1, 2)]

# question 5b: even numbers only with while loop
def ques5_b_ver1():
    num1 = int(input("please enter first number "))
    num2 = int(input("please enter second number "))
    while(num1%2 == 1): # make num1 even
        num1 += 1
    while(num2%2 == 1): # make num2 even
        num2 -= 1
    temp2 = num2
    while(num1 <= temp2):   # descending order
        print(temp2)
        temp2 -= 2
    while(num1 <= num2):    # ascending order
        print(num1)
        num1 += 2

def ques5_b_ver1_for_assert(num1, num2): # function for assert (returns list)
    range_list = []
    while(num1%2 == 1): # make num1 even
        num1 += 1
    while(num2%2 == 1): # make num2 even
        num2 -= 1
    temp2 = num2
    while(num1 <= temp2):   # descending order
        range_list += [temp2]
        temp2 -= 2
    while(num1 <= num2):    # ascending order
        range_list += [num1]
        num1 += 2
    return range_list

# question 5c: even numbers only with if statements
def ques5_c(num1, num2):
    return ques5_c2(num1, num2) + ques5_c1(num1, num2)

def ques5_c2(num1, num2):
    if(num1%2 == 1):
        num1 += 1
    if(num1 > num2):
        return []
    return ques5_c2(num1 + 2, num2) + [num1]

def ques5_c1(num1, num2):
    if(num2%2 == 1):
        num2 -= 1
    if(num1 > num2):
        return []
    return ques5_c1(num1, num2 - 2) + [num2]

# start tests
def test_ques1():
    assert(ques1_ver1([[3, 2], [1], [4, 12]]) == 22)
    assert(ques1_ver1([[0]]) == 0)
    assert(ques1_ver1([[1, 2], [3]]) == 6)
    assert(ques1_ver2([[3, 2], [1], [4, 12]]) == 22)
    assert(ques1_ver2([[0]]) == 0)
    assert(ques1_ver2([[1, 2], [3]]) == 6)

def test_ques2_a():
    assert(ques2_a_ver1("abcd\"") == "\"dcba")
    assert(ques2_a_ver1("abcd") == "dcba")
    assert(ques2_a_ver1("") == "")
    assert(ques2_a_ver2("abcd\"") == "\"dcba")
    assert(ques2_a_ver2("abcd") == "dcba")
    assert(ques2_a_ver2("") == "")

def test_ques2_b():
    assert(ques2_b_ver1([[3, 2], 1, [4, 12]]) == [[12, 4], 1, [2, 3]])
    assert(ques2_b_ver1([1, 2, 3, 4]) == [4, 3, 2, 1])
    assert(ques2_b_ver1([[1, [2, 3], 4], [5, [6, 7], 8]]) == [[8, [6, 7], 5], [4, [2, 3], 1]])
    assert(ques2_b_ver2([[3, 2], 1, [4, 12]]) == [[12, 4], 1, [2, 3]])
    assert(ques2_b_ver2([1, 2, 3, 4]) == [4, 3, 2, 1])
    assert(ques2_b_ver2([[1, [2, 3], 4], [5, [6, 7], 8]]) == [[8, [6, 7], 5], [4, [2, 3], 1]])

def test_ques2_c():
    assert(ques2_c_ver1((1, 2, 3)) == (3, 2, 1))
    assert(ques2_c_ver1((1, [2, 3])) == ([2, 3], 1))
    assert(ques2_c_ver1(()) == ())
    assert(ques2_c_ver2((1, 2, 3)) == (3, 2, 1))
    assert(ques2_c_ver2((1, [2, 3])) == ([2, 3], 1))
    assert(ques2_c_ver2(()) == ())

def test_ques3_a():
    assert(ques3_a_ver1((({1, 2, 3, 3}, {}, {"d", "g", "z"}, {3}, {3.4, 1.2, 0.3, 6.4}, {'a', 'd', 'c', 'b'}))) == ['a', 'b', 'c', 'd', 'g', 'z', 0.3, 1, 1.2, 2, 3, 3.4, 6.4])
    assert(ques3_a_ver1(({*[]})) == [])
    assert(ques3_a_ver1(()) == [])
    assert(ques3_a_ver2((({1, 2, 3, 3}, {}, {"d", "g", "z"}, {3}, {3.4, 1.2, 0.3, 6.4}, {'a', 'd', 'c', 'b'}))) ==['a', 'b', 'c', 'd', 'd', 'g', 'z', 0.3, 1, 1.2, 2, 3, 3, 3.4, 6.4])
    assert(ques3_a_ver2(({*[]})) == [])
    assert(ques3_a_ver2(()) == [])

def test_ques3_b():
    assert(ques3_b((({1, 2, 3, 3}, {}, {"d", "g", "z"}, {3}, {3.4, 1.2, 0.3, 6.4}, {'a', 'd', 'c', 'b'}))) == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'g', 5: 'z', 6: 0.3, 7: 1, 8: 1.2, 9: 2, 10: 3, 11: 3.4, 12: 6.4})
    assert(ques3_b(({*[]})) == {})
    assert(ques3_b(()) == {})

def test_ques4_a():
    assert(ques4_a_ver1_for_assert(4) == 9)
    assert(ques4_a_ver1_for_assert(10) == 9)
    assert(ques4_a_ver1_for_assert(15) == 6)
    assert(ques4_a_ver2_for_assert(4) == 9)
    assert(ques4_a_ver2_for_assert(10) == 9)
    assert(ques4_a_ver2_for_assert(15) == 6)

def test_ques4_b():
    assert(ques4_b(4) == 9)
    assert(ques4_b(10) == 9)
    assert(ques4_b(15) == 6)

def test_ques5_a():
    assert(ques5_a_ver1_for_assert(6, 14) == [14, 12, 10, 8, 6, 6, 8, 10, 12, 14])
    assert(ques5_a_ver1_for_assert(5, 15) == [14, 12, 10, 8, 6, 6, 8, 10, 12, 14])
    assert(ques5_a_ver1_for_assert(0, 0) == [0, 0])
    assert(ques5_a_ver1_for_assert(5, 5) == [])

def test_ques5_b():
    assert(ques5_b_ver1_for_assert(6, 14) == [14, 12, 10, 8, 6, 6, 8, 10, 12, 14])
    assert(ques5_b_ver1_for_assert(5, 15) == [14, 12, 10, 8, 6, 6, 8, 10, 12, 14])
    assert(ques5_b_ver1_for_assert(0, 0) == [0, 0])
    assert(ques5_b_ver1_for_assert(5, 5) == [])

def test_ques5_c():
    assert(ques5_c(6, 14) == [14, 12, 10, 8, 6, 6, 8, 10, 12, 14])
    assert(ques5_c(5, 15) == [14, 12, 10, 8, 6, 6, 8, 10, 12, 14])
    assert(ques5_c(0, 0) == [0, 0])
    assert(ques5_c(5, 5) == [])

if __name__ == "__main__":
    test_ques1()
    test_ques2_a()
    test_ques2_b()
    test_ques2_c()
    test_ques3_a()
    test_ques3_b()
    test_ques4_a()
    test_ques4_b()
    test_ques5_a()
    test_ques5_b()
    test_ques5_c()
