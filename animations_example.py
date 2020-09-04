import qutip as qt
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig, azim=-40, elev=30)
sphere = qt.Bloch(axes=ax)

n_qbits = 8
ts = 200
T2 = 150

sx = np.zeros((n_qbits, ts))
sy = np.zeros((n_qbits, ts))
sz = np.zeros((n_qbits, ts))

w = 0.2*np.random.rand(n_qbits)

for t in range(ts):
    for i in range(n_qbits):
        sx[i, t] = np.exp(-t/T2)*np.cos(w[i]*t)
        # print(sx[i, t])
        sy[i, t] = np.exp(-t/T2)*np.sin(w[i]*t)
        sz[i, t] = 0


def animate(i):
    sphere.clear()
    # sphere.add_vectors([[sx[i], sy[i], sz[i]], [sx[i], 0, 0]])
    vec_tot = [0, 0, 0]
    vec = []
    for n in range(n_qbits):
        vec.append([sx[n, i], sy[n, i], sz[n, i]])
        vec_tot[0] += sx[n, i]
        vec_tot[1] += sy[n, i]
        vec_tot[2] += sz[n, i]
    vec_tot[0] = vec_tot[0]/n_qbits
    vec_tot[1] = vec_tot[1]/n_qbits
    vec_tot[2] = vec_tot[2]/n_qbits
    # print(vec)
    sphere.vector_color = ['blueviolet']
    sphere.vector_width = 2
    sphere.add_vectors(vec)
    sphere.vector_color = ['indigo']
    sphere.vector_width = 7
    sphere.add_vectors(vec_tot)
    # sphere.add_points([sx[:i+1], sy[:i+1], sz[:i+1]])
    sphere.make_sphere()
    return ax


def init():
    sphere.zlabel = ["|0><0|", "|1><1|"]
    sphere.point_size = [20]
    sphere.point_color = ['blueviolet']
    sphere.point_marker = ['o']
    sphere.view = [-40, 30]

    return ax


ani = animation.FuncAnimation(fig, animate, np.arange(len(sx[0, :])),
                              init_func=init, repeat=False)
# ani.save('T2_with_proy.mp4', fps=20)
ani.save('T2_multi.mp4', fps=20)
