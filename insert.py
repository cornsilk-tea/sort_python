# 종료조건: SS == [] 또는  x <= ss[0]
#   종료조건을 만족하면 [x] + ss를 리턴
# 반복조건: 종료조건이 아닐때 즉 ss != [] and x > ss[1]
#   [ss[0]] + insert(x,ss[1:])

def insert(x,ss):
    if ss == [] or x <= ss[0]:
        return [x] + ss
    else:
        return [ss[0]] + insert(x,ss[1:])

def insert_tail(x,ss):
    def loop(ss,left):
        if ss == [] or x <= ss[0]:
            left.append(x)
            left.extend(ss) # 리스트 뒤에 리스트 삽입
            return left
            # return left +  ss
            # # return left + [x] + ss
        else:
            left.append(ss[0])
            return loop(ss[1:], left)
    return loop(ss,[])

#################################################################
# 교재에 나오는 코드 틀을 따라 만든 함수목록
# def insert(x,ss):
#     if ss != []:
#         if x <= ss[0]:
#             return [x] + ss
#         else:
#             return [ ss[0]] + insert(x,ss[1:]) # x>ss[0]인경우
#     else:
#         return [x] # ss == []인경우

# def insert_tail(x,ss):
#     def loop(ss,left):
#         if ss != []:
#             if x <= ss[0]:
#                 left.append(x)
#                 return left + ss
#             else:
#                 left.append(ss[0])
#                 return loop(ss[1:],left)
#         else:
#             left.append(x)
#             return left
#     return loop(ss,[])
