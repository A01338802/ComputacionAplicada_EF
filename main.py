# Ejercicio 1
import numpy as np

def f(x):
  f = np.sin(1/x)
  return f

def simpson():
  a = 1/(2*np.pi)
  b = 2
  n = 3*3000
  h = (b-a)/n
  integral = 0
  for i in range(1,n):
    integral += f(a+h*i)
  integral *= 3
  for i in range(1,n//3):
    integral -= f(a+3*i*h)

  integral += f(a)+f(b)
  integral = 3*h/8*integral
  print(integral)
simpson()
# Ejercicio 2
def g(x,y):
  g = 1+y**2
  return g

def rk4():
  h = 0.1
  xf = 1.4
  x = 0
  y = 0

  while x<=xf:
    k1 = g(x,y)
    k2 = g(x+h/2,y+k1/2*h)
    k3 = g(x+h/2,y+k2/2*h)
    k4 = g(x+h,y+k3*h)
    y += h/6*(k1+2*k2+2*k3+k4)
    x += h

  print(y)

rk4()

# Ejercicio 3
def rutamascorta():
    nodes = '12345678'
    x = '-'

    # 1 2 3 4 5 6 7 8
    M = [[x, 1, 2, x, x, x, x, x], \
         [x, x, 1, 5, 2, x, x, x], \
         [x, x, x, 2, 1, 4, x, x], \
         [x, x, x, x, 3, 6, 8, x], \
         [x, x, x, x, x, 3, 7, x], \
         [x, x, x, x, x, x, 5, 2], \
         [x, x, x, x, x, x, x, 6], \
         [x, x, x, x, x, x, x, x]]

    menor = [[0, 0, 0]] * len(M)
    dists = [0] * len(M)
    for j in range(1, len(M)):
        pos = []
        for i in range(0, len(M)):
            if M[i][j] != x:
                dis = dists[i] + M[i][j]
                pos.append([dis, nodes[i], nodes[j]])

        menor[j] = min(pos)
        dists[j] = menor[j][0]

    s = '8'
    l = menor[-1]
    while l[1] != '1':
        l = menor[int(l[1]) - 1]
        s = (l[2]) + '-' + s
    s = '1-' + s

    print("Nodos de la ruta más corta: ", s)
    print("Distancia total: ", menor[-1][0], "unidades")

rutamascorta()