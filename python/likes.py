def likes(names):
    message = ""
    num_likes = len(names)
    if num_likes == 0:
        message = "no one likes this"
    elif num_likes == 1:
        message = str(names[0]) + " likes this"
    elif num_likes == 2:
        message = str(names[0]) + " and " + str(names[1]) + " like this"
    elif num_likes == 3:
        message = str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) + " like this"
    else:
        message = str(names[0]) + ", " + str(names[1]) + " and " + str(num_likes - 2) + " others like this"
    return message
