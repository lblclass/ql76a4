def f_3fc2849(a,b,c,d,e,f):
    return (a*b-c*d*e-f)%10
def f_404f934(a,b,c):
    return (a*b*c+f_3fc2849(a,b,c,795,8,396))%10
def f_4829a46(a,b):
    return (a*b+f_404f934(a,b,245)+f_3fc2849(a,b,164,482,679,900))%10
def f_5e65c19(a,b,c):
    return (a-b-c+f_404f934(a,b,c))%10
def f_3e77575(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c*d-e*f-g+h+i+j+f_404f934(a,b,c)+f_404f934(a,b,c))%10
def f_11e6a4f(a,b,c,d,e,f):
    return (a-b-c-d-e+f+f_4829a46(a,b)+f_4829a46(a,b)+f_3fc2849(a,b,c,d,e,f))%10
