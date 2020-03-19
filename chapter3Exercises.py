
def make_grid():
    print("+----+----+")
    print("|    |    |")
    print("|    |    |")
    print("|    |    |")
    print("|    |    |")
    print("+----+----+")
    print("|    |    |")
    print("|    |    |")
    print("|    |    |")
    print("|    |    |")
    print("+----+----+")





def make_row():
    x = "+----+----+"
    return x



def make_column():
    y = "|         |"
    return y

def make_grid_n_by_n(x,y):

    for l in range(x):
        print(make_row()*x)
        for i in range(y):
            print(make_column()*x)

    print(make_row()*x)


val1, val2 = (input().split())
make_grid_n_by_n(int(val1),int(val2))




