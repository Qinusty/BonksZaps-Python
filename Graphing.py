import matplotlib
import pygame
from mpl_toolkits.mplot3d import Axes3D
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg

import pylab


def graphData(data, display, size):
    fig = pylab.figure(figsize=[7, 7],  # Inches
                       dpi=100,  # 100 dots per inch, so the resulting buffer is 600x600 pixels
                       )
    ax = fig.gca(projection='3d')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Cycle duration in ms")
    ax.set_zlabel("Total Bonks")
    ax.plot(data[0], data[1], data[2], label="Comparison of cycle duration and total bonk count to cycle count")
    ax.view_init(elev=18, azim=-27)  # camera elevation and angle
    ax.dist = 14  # camera distance
    fig.tight_layout()
    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    surf = pygame.image.fromstring(raw_data, canvas.get_width_height(), "RGB")
    display.blit(surf, (50, 50))
