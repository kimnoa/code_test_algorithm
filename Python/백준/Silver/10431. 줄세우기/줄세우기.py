import sys

numOfCase = int(input())

for _ in range(numOfCase):

    arr_input = list(map(int, sys.stdin.readline().split()))

    arr_sort = [0 for _ in range(20)]

    steps_total=0

    for idx, height in enumerate(arr_input):

        if not idx :

            continue

        steps=0

        for i in range(1,idx):

            if height < arr_sort[idx-i-1]:

                arr_sort[idx-i] = arr_sort[idx-i-1]

                steps+=1

        arr_sort[idx-1-steps]=height

        steps_total+=steps

    print(arr_input[0], steps_total)