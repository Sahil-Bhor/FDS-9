def insertion_Sort(arr):
 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':

    array = []
    total = int(input("How many elements you want to insert: "))
    for i in range(total):
        num = float(input(f"Enter the percentage of student {i+1} : "))
        array.append(num)
    
    insertion_Sort(array)
    print(f"\n(Insertion sort)\nSorted array is : ",array)

    merge_sort(array)
    print(f"\n(Merge sort)\nSorted array is : ",array)
