def isBadVersion(version):
    if version == 1 :
        return True
    return False

def firstBadVersion(n: int) -> int:
    i,j = 0,n
    result =1
    if n==1:
        return n
    while i<j:
        mid = i + ((j-i)//2)
        if isBadVersion(mid):
            j = mid-1
            result = mid
        else:
            i = mid+1
    return result

print(firstBadVersion(1))