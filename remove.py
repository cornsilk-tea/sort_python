# xs에서 v를 제거한 새로운 리스트를 만들어내는 재귀함수
def remove(xs,v):
    if xs==[]:
        return []
    else:
        if xs[0]==v:
            return xs[1:]
        else:
            return [xs[0]]+remove(xs[1:],v)

##############################################################
# 프로시저로 xs에서 실제로 v를 제거하는 xs.remove(v)와 같이 동작하도록
# 간단히 remove 함수를 이용해서 만들어보기
# 단 이 방법은 remove 메소드보다는 당연히 비효율적이다.
def remove_proc(xs,v):
    # xs = remove(xs,v)  이것은 실패한 시도다. 원래 리스트는 그대로 있고 새로운 리스트를 xs에 저장
    xs[:] = remove(xs,v)