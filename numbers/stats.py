grades = [18,14,8,9.5,3,5,6,12,14,13,20,2,3.5]

def print_grades(grades):
    for grade in grades:
        print(grade)

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(scores, average):
    variance = 0.0
    for score in scores:
        variance += (score - average)**2
    variance = variance / len(scores)
    return variance

def grades_std_deviation(variance):
    return variance ** 0.5

grades_std_deviation(grades_variance(grades,grades_average(grades)))

print_grades(grades)
print("Somme des notes :",grades_sum(grades))
print("Moyenne des notes :",grades_average(grades))
print("Variance des notes :",grades_variance(grades,grades_average(grades)))
print("Écart type des notes :",grades_std_deviation(grades_variance(grades,grades_average(grades))))
