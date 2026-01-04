def medianoftwo(scoreA, scoreB):
    if len(scoreA) % 2 != 0:
        medianA = scoreA[len(scoreA) // 2]
    else:
        medianA = (scoreA[len(scoreA) // 2] + scoreA[len(scoreA) // 2 - 1]) / 2
    

    if len(scoreB) % 2 != 0:
        medianB = scoreB[len(scoreB) // 2]
    else:
        medianB = (scoreB[len(scoreB) // 2] + scoreB[len(scoreB) // 2 - 1]) / 2
    
    return (medianA + medianB) / 2

print("Input:")
scoreA = list(map(int, input().split(',')))
scoreB = list(map(int, input().split(',')))

print("Output:", medianoftwo(scoreA, scoreB))