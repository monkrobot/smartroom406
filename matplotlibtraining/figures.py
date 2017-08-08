from pylab import *
import matplotlib.gridspec as gridspec

G = gridspec.GridSpec(3, 3)

axes_1 = subplot(G[0, :])
xticks([1, 2, 3, 4]), yticks([1, 2, 3, 4])
text(0.5,0.5, 'Axes 1',ha='center',va='center',size=24,alpha=.5)
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c,s = np.cos(x), np.sin(x)

plt.plot(x,c, color="blue", linewidth=2.0, linestyle="-", label="my_cos")

axes_2 = subplot(G[1,:-1])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)
plt.plot(x,c, color="blue", linewidth=2.0, linestyle="-", label="my_cos")
plt.plot(x,s, color="green", linewidth=1.0, linestyle="--", label="my_sin")

axes_3 = subplot(G[1:, -1])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 3',ha='center',va='center',size=24,alpha=.5)

axes_4 = subplot(G[-1,0])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 4',ha='center',va='center',size=24,alpha=.5)

axes_5 = subplot(G[-1,-2])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 5',ha='center',va='center',size=24,alpha=.5)

#plt.savefig('../figures/gridspec.png', dpi=64)
show()