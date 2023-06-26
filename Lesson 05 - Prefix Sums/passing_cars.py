def solution(A):
    east_cars = 0
    passing_cars = 0

    for car in A:
        if car == 0:
            east_cars += 1
        else:
            passing_cars += east_cars

    if passing_cars > 1e9:
        return -1
    else:
        return passing_cars
