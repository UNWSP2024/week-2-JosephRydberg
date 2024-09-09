#Joseph Rydberg, 9/9/2024, ItemCost
def calculate_total_purchase():
    i1 = int(input("enter item 1 cost"))
    i2 = int(input("enter item 2 cost"))
    i3 = int(input("enter item 2 cost"))
    i4 = int(input("enter item 4 cost"))
    i5 = int(input("enter item 5 cost"))

    total = (i1 + i1 + i3 + i4 + i5)
    print(total)
    totalTax = (i1 + i1 + i3 + i4 + i5) * .07
    print(totalTax)

    print(total + totalTax)

calculate_total_purchase()