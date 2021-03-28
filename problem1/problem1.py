def sum_mults(num1, num2, threshhold):
    sum_nbrs = 0
    for i in range(threshhold):
        if(i % num1 == 0 or i % num2 == 0):
            sum_nbrs += i
    return str(sum_nbrs)


if __name__ == "__main__":
    print(sum_mults(3, 5, 1000))
