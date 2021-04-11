def remove(xs,v):
    if xs==[]:
        return []
    else:
        if xs[0]==v:
            return xs[1:]
        else:
            return [xs[0]]+remove(xs[1:],v)