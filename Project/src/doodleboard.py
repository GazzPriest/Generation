data = [['NAME', 'AGE', 'HANDEDNESS', 'SCORE (%)'],
        ['Martin', 38, 'L', 54.123],
        ['Marty', 33, 'L', 32.438],
        ['Martine', 25, 'R', 71.128],
        ['Martyn', 59, 'R', 50.472],
        ['Mart', 23, 'L', 2.438],
        ['Martyne', 15, 'R', 71.128],
        ['Marlyn', 101, 'R', 0.472],
        ['Marti', 2, 'L', 55.438],
        ['Mardi', 9, 'R', 81.128],
        ['Martyne', 49, 'R', 24.472],
        ['Marteen', 91, 'L', 1.128]]

dash = '-' * 40

for i in range(len(data)):
    if i == 0:
      print(dash)
      print('{:<10s}{:>4s}{:>12s}{:>12s}'.format(data[i][0],data[i][1],data[i][2],data[i][3]))
      print(dash)
    else:
      print('{:<10s}{:>4d}{:^12s}{:>12.1f}'.format(data[i][0],data[i][1],data[i][2],data[i][3]))
