def st(n):
    if(n.startswith('ls')):
        return n
    else:
        return 'ls'+n
n=input('Enter the string:')
print(st(n))
