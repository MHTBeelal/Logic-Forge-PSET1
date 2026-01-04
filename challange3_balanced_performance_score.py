def medianoftwo(scoreA, scoreB):
    i = j = 0
    m, n = len(scoreA), len(scoreB)
    total = m + n
    mid1 = total // 2
    mid2 = mid1 - 1
    

    count = 0
    prev = curr = 0

    while count <= mid1:
        prev = curr

        if i < m and (j >= n or scoreA[i] <= scoreB[j]):
            curr = scoreA[i]
            i += 1
        else:
            curr = scoreB[j]
            j += 1
        count += 1
    
    if total % 2 == 1:
        return float(curr)
    else:
        return(prev + curr) / 2

print("Input:")
scoreA = list(map(int, input().split(',')))
scoreB = list(map(int, input().split(',')))

print("Output:", medianoftwo(scoreA, scoreB))