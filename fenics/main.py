from dolfin import *

# Create mesh and define function space
mesh = UnitSquareMesh(64, 64)
V = FunctionSpace(mesh, "Lagrange", 1)

# Define Dirichlet boundary (x = 0 or x = 1)
def boundary(x):
    return x[0] < DOLFIN_EPS*pow(10,8) or x[0] > 2 - DOLFIN_EPS*pow(10,8)
print(DOLFIN_EPS)
# Define boundary condition
u0 = Constant(0.0)
bc = DirichletBC(V, u0, boundary)

# Define variational problem
u = TrialFunction(V)
v = TestFunction(V)
#f = Expression("10*exp(-(pow(x[0] - 0.5, 2) + pow(x[1] - 0.5, 2)) / 0.02)", degree=2)
f = Expression("x[1]*sin(x[0])", degree=2)
g = Expression("exp(-100*(x[0]*x[0]+x[1]*x[1]))", degree=2)
g = Expression("exp(-100*(x[0]*x[0]+x[1]*x[1]))", degree=2)
a = inner(grad(u), grad(v))*dx
L = f*v*dx + g*v*ds

# Compute solution
u = Function(V)
solve(a == L, u, bc)

# Save solution in VTK format
file = File("poisson_new/poisson_new.pvd")
file << u

# Plot solution
import matplotlib.pyplot as plt
plot(u)
plt.show()