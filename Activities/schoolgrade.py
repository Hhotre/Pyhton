studen = input('What the name of the student? ')
s1 = float(input('Please type his first grade(1 to 10): '))
s2 = float(input('Please type his secong grade(1 to 10): '))
s3 = float(input('Please type his third and final grade(1 to 10): '))
res = ((s1+s2+s3)/3)
if (res <= 6):
    print('{} reproved!'.format(studen))

if (res >= 7):
    print('{} aproved!'.format(studen))

