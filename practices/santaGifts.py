def gift_distribution(count, names, gifts, order):
    first = names.index(order[0])
    second = names.index(order[1])
    cwise = True
    if (second == first % count):
        print("CLOCKWISE")
    else:
        print("ANTICLOCKWISE")
        cwise = False

    distrib = {i: 0 for i in range(count)}
    k = first

    for i in range(gifts):
        k %= count
        distrib[k] += 1
        if i != gifts-1:
            if cwise:
                k += 2
            else:
                k -= 2
    max_gifts = list(
        filter(lambda val: val[1] == distrib[0], distrib.items()))
    for i in reversed(max_gifts):
        print(f"{names[i[0]]}:{i[1]}")
    print(names[k])


gift_distribution(5, ["nick", "joe", "john", "noah", "damon"],
                  gifts=13, order=["damon", "john"])
