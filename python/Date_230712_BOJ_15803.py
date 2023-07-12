team = []
for i in range(3):
    a,b = map(int, input().split())
    team.append([a,b])

x_change = team[0][0] - team[1][0]
y_change = team[0][1] - team[1][1]

x_change2 = team[1][0] - team[2][0]
y_change2 = team[1][1] - team[2][1]

x_change3 = team[0][0] - team[2][0]
y_change3 = team[0][1] - team[2][1]

if x_change == 0:
    if x_change2 == 0:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")
elif y_change == 0:
    if y_change2 == 0:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")
else:
    if x_change / y_change == x_change2 / y_change2:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")
