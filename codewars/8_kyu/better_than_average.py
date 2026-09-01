def better_than_average(class_points, your_points):
    a = 0

    for i in class_points:
        a = a + i

    sr = a / len(class_points)

    if your_points > sr:
        return True
    else:
        return False
