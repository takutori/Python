import sys



def main():
    i = 0
    while i < 5:
        print('apple')
        j = 0
        while j <= i:
            sys.stdout.write(' ')
            j = j + 1
        i  = i + 1
if __name__ == '__main__':
    main()
