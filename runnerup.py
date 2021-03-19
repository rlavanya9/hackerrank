def runnerup(arr_lst):
    # n = int(input())
    # arr = map(int, input().split())
    # arr_lst = list(arr)
    srt_lst = sorted(arr_lst)
    maxm = srt_lst[-1]
    for item in range(len(srt_lst)-1,-1,-1):
        if srt_lst[item] < maxm:
            runner = srt_lst[item]
            print(runner)
            break
    

runnerup([2, 3, 6, 6, 5])