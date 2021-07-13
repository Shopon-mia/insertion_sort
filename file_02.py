def insertion_sort(data_list):
    n = len(data_list)

    for i in range(1, n):
        item = data_list[i]

        j = i - 1

        while j >= 0 and data_list[j] < item:
            data_list[j+1] = data_list[j]
            j = j - 1
        data_list[j+1] = item


data_list = [4, 6, 3, 5, 1, 2]
insertion_sort(data_list)
print(data_list)
