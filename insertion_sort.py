# 삽입정렬
# **리스트 xs를 삽입정렬하려면,**
# - **(반복조건) xs!=[]**
#     - xs의 후미리스트인 xs[1:]을 재귀로 정렬하고,
#     - xs의 선두원소인 xs[0]을 정렬한 리스트의 적절한 위치에 끼워서 리턴한다.
# - **(종료조건) xs == []**
#     - 정렬할 원소가 없으므로 []를 그대로 리턴한다.

import insert as ins
def insertion_sort(xs):
    if xs != []:
        return ins.insert(xs[0], insertion_sort(xs[1:]))
    else:
        return []

def insertion_sort_tail(xs):
    pass
