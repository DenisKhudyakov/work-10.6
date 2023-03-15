
height = int(input('Высота пирамиды: '))
for i in range(1, height + 1):
  for j in range(height*2+1):
    if j == height:
      print('*' * (i * 2 - 1), end='')
      height -= 1
    else:
      print(' ', end='')
  print()
