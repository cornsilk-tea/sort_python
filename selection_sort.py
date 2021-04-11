import remove as rm
# selection_sort의 베이스 형태.
# def selection_sort(xs):
#     if xs != []:
#         smallest = min(xs)
#         xs.remove(smallest)
#         return [smallest]+selection_sort(xs)
#     else:
#         return []
#######################################################
def selection_sort(xs):
    ss = []
    while xs != []:
        smallest = min(xs)
        rm.remove_proc(xs,smallest)
        ss.append(smallest)
    return ss

#######################################################
def selection_sort_key(xs, key=(lambda x:x)): # key에 이 람다(향등함수)는 자기가 받은 인수를 그대로 돌려준다.
    ss = [] # xs, ss = xs, []
    while xs != []:
        smallest = min(xs,key=key)
        rm.remove_proc(xs,smallest) #xs.remove(smallest)
        ss.append(smallest)
        # xs, ss = xs, ss
    return ss
