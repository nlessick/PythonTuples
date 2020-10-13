def average_scores(*args, **kwargs):
    # takes each value and adds them up
    score = 0
    for value in args[0:5]:
        score += value

    # prints each string item
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

    # calculates the average score and prints it
    score = score / 4
    print("Average GPA: ", score)




if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Nate', last_name='Essick', major='Computer Science'))

