li = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input(f"Enter element : "))
    li.append(ele)
def selection_sort(li):
        for i in range(len(li)):
            min_ind = i
            for j in range(i + 1, len(li)):
                if li[j] < li[min_ind]:
                    min_ind = j
            li[i], li[min_ind] = li[min_ind], li[i]

        return print(li)
selection_sort(li)
# '''Recursive way'''
# li = []
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     ele = int(input(f"Enter element : "))
#     li.append(ele) 
# def recursive_selection_sort(li, start=0):
#     if start < len(li):
#         min_ind = start
#         for j in range(start + 1, len(li)):
#             if li[j] < li[min_ind]:
#                 min_ind = j
#         li[start], li[min_ind] = li[min_ind], li[start]
#         recursive_selection_sort(li, start + 1)

# def selection_sort(li):
#     recursive_selection_sort(li)
#     print(li)
# selection_sort(li)
# li =[]


