# Helper function for adding a cog and a bottom to create a row
# Keeping in mind, value on bottom will be blocked if the cog number isn't 0
def create_row(cog, bottom):
    array = []
    for i in range(16):
        if (cog[i] != 0):
            array.append(cog[i])
        else:
            array.append(bottom[i])
    return array

def rotate(arr):
    n = len(arr)
    if n <= 1:
        return arr  # Nothing to rotate

    last_element = arr[-1]

    # starts from n - 1 and goes down to 1 (excluding 0) with a step size of -1
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last_element

def check_columns():
    for i in range(16):
        if (row_4[i] + row_3[i] + row_2[i] + row_1[i] != 40):
            return False
    return True

def print_solution():
    print("Solution!\n")
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)
    print("\n")

cog_1 = [10, 0, 10, 0, 10, 0, 6, 0, 13, 0, 3, 0, 3, 0, 6, 0]

bottom_1 = [5, 5, 4, 8, 6, 3, 1, 6, 10, 6, 10, 2, 6, 10, 4, 1]
cog_2 = [15, 0, 14, 0, 5, 0, 10, 0, 2, 0, 22, 0, 2, 0, 17, 0]

bottom_2 = [1, 1, 11, 27, 14, 5, 5, 7, 8, 24, 8, 3, 6, 15, 22, 6]
cog_3 = [9, 0, 16, 0, 17, 0, 2, 0, 2, 0, 10, 0, 15, 0, 6, 0]

bottom_3 = [7, 3, 12, 24, 10, 9, 22, 9, 5, 10, 5, 1, 24, 2, 10, 9]


row_4 = [27, 10, 19, 10, 13, 10, 2, 15, 23, 19, 3, 2, 3, 27, 20, 11,]
row_3 = []
row_2 = []
row_1 = []

for i in range(16):
    row_3 = create_row(cog_3, bottom_3)

    for k in range(16):
        row_2 = create_row(cog_2, bottom_2)

        for z in range(16):
            row_1 = create_row(cog_1, bottom_1)
            if (check_columns()):
                print_solution()
            rotate(cog_1)
        
        rotate(bottom_1)
        rotate(cog_2)

    rotate(bottom_2)
    rotate(cog_3)