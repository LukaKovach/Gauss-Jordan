n = int(input("Veličina matrice: "))
matrica = [[0]*(n+1) for i in range(n)]


def zbrajanje(red_1, red_2):
    for i in range(n+1):
        matrica[red_2-1][i] += matrica[red_1-1][i]
    return matrica


def mnozenje(red, broj):
    for i in range(n+1):
        matrica[red-1][i] *= broj
    return matrica


def dijeljenje(red, broj):
    for i in range(n+1):
        matrica[red-1][i] /= broj
        if matrica[red-1][i] == -0:
            matrica[red - 1][i] = 0
    return matrica


def mnozi_zbroji(red1, red2, broj):
    for i in range(n+1):
        matrica[red2-1][i] = matrica[red1-1][i] * broj + matrica[red2-1][i]


def zamjena(red1, red2):
    for i in range(n+1):
        matrica[red1-1][i], matrica[red2-1][i] = matrica[red2-1][i], matrica[red1-1][i]


for i in range(n):
    for j in range(n+1):
        print("Unesite element u ", i+1, ". redu i ", j+1, ". stupcu: ")
        a = int(input())
        matrica[i][j] = a


mnozi_zbroji(1, 2, -2)

zbrajanje(1, 3)

mnozenje(3, 0.5)

zbrajanje(3, 1)

mnozi_zbroji(3, 2, -3)

dijeljenje(2, -6)

mnozi_zbroji(2, 3, -1)

mnozi_zbroji(2, 1, -2)

zamjena(2, 3)

for i in matrica:
    print(i)

print("X = ", matrica[0][3])
print("Y = ", matrica[1][3])
print("Z = ", matrica[2][3])
