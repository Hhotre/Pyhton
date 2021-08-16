n1 = float(input('Type a number: '))
eq = input('Type what you wish to do: /,*,-,+ ')
n2 = float(input('Type the second number: '))
if (eq == '/'):
  print('Your result for that equation is: {}'.format(n1/n2))

if (eq == '*'):
  print('Your result for that equation is: {}'.format(n1*n2))

if (eq == '-'):
  print('Your result for that equation is: {}'.format(n1-n2))

if (eq == '+'):
  print('Your result for that equation is: {}'.format(n1+n2))

