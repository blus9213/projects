def sort(b):
    n = len(b)
    for i in range(n):
        for j in range(0, n-i-1):
            if b[j] > b[j+1]:
                # Swap elements if they are in the wrong order
                b[j], b[j+1] = b[j+1], b[j]

    return b

c = [5, 3, 4]
c = sort(c)
print(c)
