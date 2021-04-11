import selection_sort as sort
print(sort.selection_sort([4,-2,3,-1,5]))
print(sort.selection_sort_key([4,-2,3,-1,5], key=abs))# 절대값을 기준으로 정렬
