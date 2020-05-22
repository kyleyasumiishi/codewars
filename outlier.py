def find_outlier(integers):
    outlier = None
    
    # determine if integers array contains even or odd integers
    even, odd = 0, 0
    for i in range(3):
        if integers[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    
    # if even, outlier is odd. else, outlier is even.
    if even > odd:
        for i in integers:
            if i % 2 != 0:
                outlier = i
                break
    else:
        for i in integers:
            if i % 2 == 0:
                outlier = i
                break
    
    return outlier


print(find_outlier([-4624276, -5341093, 5892496, 2595232, -1047484, -6148778, -5940596, 9429086, -7476938, -1295272, 5938612, 6690034, 4203432, -6966066, 7670764, -8855944, -9546314, 8064004, -6628382, 706832, -4661230, 6608184, -5792994, 6461024, 9572088, -9237974, -8104462, 9671136, -2891048, -2168958, 7595876, -3828316, 6299228, -9781862, -4930462, 9077836]))