while True:
    print("GPA calculator")
    p=input("Enter your grade in the form of a capital letter. e.g. (A+, B- etc. Type a number to convert a percentage instead.")
    x = float(input("What is the highest achievable GPA? e.g 4 or 5"))
    y = 0
    if p =='A+':
        GPA = 4.3
    elif p =='A':
        GPA = 4.0
    elif p =='A-':
        GPA = 3.7
    elif p =='B+':
        GPA = 3.3
    elif p =='B':
        GPA = 3.0
    elif p =='B-':
        GPA = 2.7
    elif p =='C+':
        GPA = 2.3
    elif p =='C':
        GPA = 2.0
    elif p =='C-':
        GPA = 1.7
    elif p =='D+':
        GPA = 1.3
    elif p =='D':
        GPA = 1.0
    elif p =='D-':
        GPA = 0.7
    elif p =='F':
        GPA = 0.0
    else:
        y = float(p)
        n = 100/x
        percentGPA = y/n
        print(percentGPA)
    if y == 0:
        GPA = GPA/4
        GPA = GPA * x
        print(GPA)
    input("Press ENTER to run again")
