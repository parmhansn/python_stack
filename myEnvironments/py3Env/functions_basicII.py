countdown = 5
for i in range(countdown, -1, -1):
    print(i)


def a(arr):
    print (arr[0])
    return(arr[1])
a([2,5])


def a(arr):
    return arr[0] + len(arr)
a([1,2,3,4,5])


def greaterthan(arr):
    newArr = []
    for idx in range (0, len(arr)):
        if arr[idx] > arr[1]:
            newArr.append(arr[idx])
    if len(newArr) == 1:
        return false
    else:
        print(len(newArr))
        return newArr

print(greaterthan([50,23,26,10,1,7]))


