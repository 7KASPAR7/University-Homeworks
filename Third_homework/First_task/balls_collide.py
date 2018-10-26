def balls_collide(arg1, arg2):
    if arg1[2] < 0 or arg2[2] < 0:
        raise ValueError('Радиус не может быть отрицательным')
    distance = ((arg1[0] - arg2[0]) ** 2 + (arg2[1] - arg1[1]) ** 2) ** .5
    if distance > arg1[2]+arg2[2]:
        return False
    elif distance < abs(arg2[2] - arg1[2]):
        return False
    else:
        return True
