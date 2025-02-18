from bisect import bisect_left, bisect_right

a = [1,2,3,4,4,4,5,6]
leftResult = bisect_left(a,4)
rightResult = bisect_right(a,4)

print(f"leftResult:{leftResult}")
print(f"rightResult:{rightResult}")




# 직접 구현
def lower_bound_binary_search(ary, x): # 왼 -> 오 방향
    start = 0
    end = len(ary)-1

    while start <=end:
        mid = (start+end)//2
        print(f"    start:{start},end :{end}, mid:{mid}")
        if ary[mid] < x : # 확실히 커야 start 업뎃
            start = mid + 1

        else :
            end = mid -1

    print(f" lower_bound_binary_search : result : {start}, start : {start}, end: {end}")
    return start


def upper_bound_binary_search(ary, x): # 오 -> 왼
    start = 0
    end = len(ary)-1

    while start <=end:
        mid = (start+end)//2
        print(f"    start:{start},end :{end}, mid:{mid}")
        if ary[mid] <= x : # 같은값일떄도 start 업뎃
            start = mid + 1
        else :
            end = mid -1
    print(f" upper_bound_binary_search : result : {start}, start : {start}, end: {end}")
    return start

lower_bound_binary_search(a,4)
upper_bound_binary_search(a,4)
