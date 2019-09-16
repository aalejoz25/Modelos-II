def rev(l):
    if len(l) == 0:
        return []
    return [l[-1]] + rev(l[:-1]);

print(rev([1,2,3,4,5]))
