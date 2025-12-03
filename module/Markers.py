import numpy as np
import matplotlib.patches as patches
from matplotlib.patches import Polygon as pol
import matplotlib.pyplot as plt


# --- HELPER FUNCTION ---------------------------------------------------------
def _compute_missile_triangle(x, y, angle_deg, L=12, W=12):
    """
    Computes the rotated and translated missile triangle coordinates.
    """
    # Base triangle (missile initially pointing downward)
    tri = np.array([
        [0, 0],          # Tip of the missile
        [-W / 2, -L],    # Bottom-left
        [W / 2, -L]      # Bottom-right
    ])

    # Rotation
    angle = np.radians(angle_deg)
    R = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)]
    ])

    # Rotate and translate the triangle to (x, y)
    return tri.dot(R) + np.array([x, y])


# --- MISSILE CREATION --------------------------------------------------------
def make_missile(ax, x, y, angle_deg, color, label):
    """
    Creates a missile and adds it to the given axis.
    """
    # Compute rotated triangle
    tri_rot = _compute_missile_triangle(x, y, angle_deg)

    # Create polygon for missile outline
    poly = pol(
        tri_rot,
        closed=True,
        edgecolor="none",
        facecolor=color,
        linewidth=2
    )
    ax.add_patch(poly)

    # Add text label above the missile
    text = ax.text(x - 5, y - 20, label, fontsize=10, color=color)

    return poly, text


# --- MISSILE UPDATE ----------------------------------------------------------
def update_missile(poly, text, x, y, angle_deg):
    """
    Updates the missile's position and orientation.
    """
    # Compute updated triangle coordinates
    tri_rot = _compute_missile_triangle(x, y, angle_deg)

    # Update polygon vertices
    poly.set_xy(tri_rot)

    # Update label position
    text.set_position((x, y + 0.3))

# --- RADAR FUNCTION ----------------------------------------------------------

def make_radar(ax, x, y,
               r1=20,
               r2=50,
               cone_range=150,   # SAFE FOR YOUR Y-LIMITS
               cone_angle=180,
               cone_dir=0,
               color="black",
               label="Radar"):

    # Prevent autoscaling (critical fix)
    ax.autoscale(False)

    # Cross center
    size = 10
    ax.plot([x, x], [y - size, y + size], color=color, linewidth=2)
    ax.plot([x - size, x + size], [y, y], color=color, linewidth=2)
    ax.text(x, y + size + 5, label, fontsize=10, color=color, ha="center")

    # Inner circle
    circle1 = plt.Circle((x, y), r1,
                         edgecolor="gray",
                         facecolor="none",
                         linestyle="--",
                         linewidth=1.5,
                         alpha=0.8)
    ax.add_patch(circle1)

    # Middle circle
    circle2 = plt.Circle((x, y), r2,
                         edgecolor="gray",
                         facecolor="none",
                         linestyle="--",
                         linewidth=1.5,
                         alpha=0.8)
    ax.add_patch(circle2)

    # Cone angles
    theta1 = cone_dir - cone_angle / 2
    theta2 = cone_dir + cone_angle / 2

    wedge = patches.Wedge(
        center=(x, y),
        r=cone_range,
        theta1=theta1,
        theta2=theta2,
        facecolor="#ffddaa",
        edgecolor="orange",
        linestyle="--",
        linewidth=2,
        alpha=0.35
    )
    ax.add_patch(wedge)

    return circle1, circle2, wedge

def make_radar_sweep(ax, x, y, start_angle=0, length=150, color="green"):
    """
    Creates a rotating radar sweep line (PAC-3 style).
    The returned Line2D object can be rotated each frame.
    """
    import numpy as np

    theta = np.radians(start_angle)

    # Compute end of the beam
    x2 = x + length * np.cos(theta)
    y2 = y + length * np.sin(theta)

    # Visual sweep line
    sweep_line, = ax.plot(
        [x, x2], [y, y2],
        color=color,
        linewidth=2,
        alpha=0.7
    )

    return sweep_line

def update_radar_sweep(sweep_line, x, y, angle_deg, length=150):
    """
    Rotates and updates the radar sweep line.
    Called on every animation frame.
    """
    import numpy as np

    theta = np.radians(angle_deg)

    # End of the sweep beam
    x2 = x + length * np.cos(theta)
    y2 = y + length * np.sin(theta)

    sweep_line.set_data([x, x2], [y, y2])


