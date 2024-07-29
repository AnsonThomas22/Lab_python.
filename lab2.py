def module_ListFunction(L):
    print('The maximum value of the list is:', max(L))  
    print('The minimum value of the list is:', min(L))
    sum1 = 0 
    
    for i in L:
        sum1 += i  
    
    
    print('The sum of the list is:', sum1)
    avg = sum1 / len(L)
    print('The average value of the list is:', avg)
    
    sorted_lst = sorted(L)
    n = len(sorted_lst)
    if n % 2 == 1:
        t = sorted_lst[n // 2]
    else:
        middle1 = sorted_lst[n // 2 - 1]
        middle2 = sorted_lst[n // 2]
        t = (middle1 + middle2) / 2
    
   
    print(f"The median is: {t}")


def add_element(s, element):
    s.add(element)
    return s

def remove_element(s, element):
    s.discard(element)
    return s

def union_and_intersection(s1, s2):
    union = s1.union(s2)
    intersection = s1.intersection(s2)
    return union, intersection

def difference(s1, s2):
    return s1.difference(s2)

def is_subset(s1, s2):
    return s1.issubset(s2)

def set_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    return s1.symmetric_difference(s2)

def power_set(s):
    from itertools import chain, combinations
    s = list(s)
    power_set = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    return [set(x) for x in power_set]

def unique_subsets(s):
    from itertools import chain, combinations
    s = list(s)
    subsets = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    return [set(x) for x in subsets]



def merging_Dict(*args):
    
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

def common_keys(*args):
    
    if not args:
        return set()
    common_keys_set = set(args[0].keys())
    for d in args[1:]:
        common_keys_set.intersection_update(d.keys())
    return common_keys_set

def invert_dict(d):
    
    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict

def common_key_value_pairs(*args):
    if not args:
        return {}
    common_pairs = set(args[0].items())
    for d in args[1:]:
        common_pairs.intersection_update(d.items())
    return dict(common_pairs)
