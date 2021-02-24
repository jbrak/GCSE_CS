def math(n1,n2,operation = '*' or '/' or '+' or '-'):
    switch = {
    '*' : n1*n2,
    '/' : n1/n2,
    '+' : n1+n2,
    '-' : n1-n2}
    return switch[operation]

print(math(7,6,'+'))
