numx=int(input("Ingrese un número: "))
for x in range(2, numx+1):
    print(x)
    funcionx= x**3+x**2-5
    print("f(", x, ") = ", funcionx)