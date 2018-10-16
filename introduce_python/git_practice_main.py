from practice_def import plus,vector_space



def main():
    """
    x = 1
    y = 3
    print(plus(x,y))
    """
    x = 2
    y = 3
    X = vector_space(2,3)
    print(x,y)
    print(X.plus())
    print(X.mainus())
    print(X.tiems())


if __name__ == '__main__':
    main()
