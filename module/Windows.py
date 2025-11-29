from module import imports
from matplotlib.gridspec import GridSpec
import matplotlib

matplotlib.use('TkAgg')

# get only np and Callable
plt = imports().plt


def windows(title="Hypersonic Interceptor vs Incoming Missile Simulation"):
    """
    Creates a window with the following layout:

    - First row:
        • A large subplot occupying columns [0, 0:2]
        • A smaller subplot in column [0,2]
        • Column [0,3] remains empty

    - Second row:
        • Four standard-size subplots occupying columns [1,0], [1,1], [1,2], and [1,3]

    Returns:
        fig : the main figure window
        ax_list : a list of axes in the following order:
            [large_subplot, small_subplot, row2_col1, row2_col2, row2_col3, row2_col4]
    """
    fig = plt.figure(figsize=(20, 10))
    fig.canvas.manager.set_window_title(title)

    gs = GridSpec(2, 4, figure=fig)

    ax1 = fig.add_subplot(gs[0, 0:2])
    ax2 = fig.add_subplot(gs[0, 2])

    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])
    ax5 = fig.add_subplot(gs[1, 2])
    ax6 = fig.add_subplot(gs[1, 3])

    ax_list = [ax1, ax2, ax3, ax4, ax5, ax6]
    return fig, ax_list


def update_subplot(ax, x_data, y_data, label="", title="", xlabel="", ylabel=""):
    ax.plot(x_data, y_data, label=label)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    if label:
        ax.legend()
