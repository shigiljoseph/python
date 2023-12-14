#Square
n=int(input('Enter the length square:'))
a1=lambda n:n**2
print('Area of square:',a1(n))
#Triangle

n=list(map(int,(input('Enter the length and breadth of triangle:').split())))
a2=lambda a,b:0.5*a*b
print('Area of triangle:',a2(n[0],n[1]))

#Rectangle
n=list(map(int,(input('Enter the length and breadth of rectangle:').split())))
a3=lambda a,b:a*b
print('Area of triangle:',a3(n[0],n[1]))
