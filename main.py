print("GPA calculator")
p=input("Enter your grade in the form of a capital letter. e.g. (A+, B- etc. Type N to convert a percentage instead.")
if p =='A+':
    GPA = 4.3
if p =='A':
    GPA = 4.0
if p =='A-':
    GPA = 3.7
if p =='B+':
    GPA = 3.3
if p =='B':
    GPA = 3.0
if p =='B-':
    GPA = 2.7
if p =='C+':
    GPA = 2.3
if p =='C':
    GPA = 2.0
if p =='C-':
    GPA = 1.7
if p =='D+':
    GPA = 1.3
if p =='D':
    GPA = 1.0
if p =='D-':
    GPA = 0.7
if p =='F':
    GPA = 0.0
if p =='N':
    x = int(input("What is the highest achievable GPA? e.g 4 or 5"))
    y = int(input("What percentage did you get? Do not type symbols, only numbers."))
    n = 100/x
    GPA = y/n
print(GPA)
