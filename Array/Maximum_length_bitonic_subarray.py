l = int(input())
arr = list(map(int, input().split()))
  i, count, maxm = 1, 1, 1
   while i < l:
        if arr[i] == 0 or arr[i] == arr[i-1]:
            i += 1
            count = 1
            continue
        while i < l and arr[i] > arr[i-1]:
            count += 1
            i += 1
        if count > maxm:
            maxm = count
        while i < l and arr[i] < arr[i-1]:
            count += 1
            i += 1
        if count > maxm:
            maxm = count
        count = 1
    print(maxm)
