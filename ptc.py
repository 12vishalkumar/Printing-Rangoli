import string
def print_rangoli(size):
    # your code goes here
    case = string.ascii_lowercase
    lt = []
    for i in range(n):
        st = '-'.join(case[i:n])
        lt.append((st[::-1]+st[1:]).center(4*n-3, '-'))
    print('\n'.join(lt[:0:-1] + lt))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)