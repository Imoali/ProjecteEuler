def even_fibonacci():
    Un, Un_1, sum_evens = 1, 2, 0
    while(Un_1 <= 4000000):
        if(Un_1 % 2 == 0):
            sum_evens += Un_1
        Un, Un_1 = Un_1, Un + Un_1

    return str(sum_evens)


if __name__ == "__main__":
    print(even_fibonacci())
