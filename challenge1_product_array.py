def product_list(contribution):
    impact = []

    for i in range(len(contribution)):
        product = 1
        for j in range(len(contribution)):
            if i != j:
                product *= contribution[j]
        impact.append(product)
    return impact

 
lists = list(map(int,input("").split(",")))
lists = product_list(lists)
print(lists)