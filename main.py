# ==========================================================
# 🚀 Rocket Laplace Test
# ==========================================================
#
# Minimal test for Laplace_function module.
# Demonstrates computing Laplace transform of a target signal.
#
# Features:
#  - Define a target function Y(t)
#  - Compute Laplace transform F(s) for a range of s values
#  - Save |F(s)| plot to PNG (no GUI required)
#
# Author: Adrian Szklarski
# Date: 2025-11-28
# ==========================================================

from module import imports
from module.Math_Laplace import Laplace_function as Lf
from module.Windows import windows as Win, update_subplot
from module.Markers import make_missile, make_radar, make_radar_sweep
from module.Target import random_target_spawn
import matplotlib.pyplot as plt

np = imports().np

if __name__ == "__main__":
    try:
        # --- Example target function ---
        target_y = lambda t: np.sin(t) + 0.1 * np.random.randn(len(t))  # small noise

        # --- s points in Laplace domain ---
        s_values = np.linspace(0.1, 5, 50)

        # --- Call Laplace_function ---
        F_s = Lf(
            func=target_y,
            s_points=s_values,
            t_max=6.0,
            dt=0.001
        )

        # --- Print results ---
        print("F(s) =", F_s)

        # --- Create window (2x4 layout) ---
        fig, axes = Win(title="Hypersonic Interceptor vs Incoming Missile Simulation")

        # Set the visible X & Y range of the main subplot
        axes[0].set_xlim(-250, 250)
        axes[0].set_ylim(-180, 180)
        axes[0].grid(True)

        # Create and draw the interceptor missile (blue)
        # Parameters: axis, initial X position, initial Y position, rotation angle,
        # edge color, and label text

        # --- INTERCEPTOR (PAC-3) placed at radar coordinates (0,0) ---
        rocket_x, rocket_y = 8, 0
        rocket_angle = 90  # Rakieta startuje pionowo do góry (można zmienić)

        interceptor, interceptor_text = make_missile(
            axes[0],
            rocket_x,
            rocket_y,
            angle_deg=rocket_angle,
            color="blue",
            label="Rocket"
        )

        # Create and draw the target missile (red)
        # Same parameters as above but with different position and rotation

        tgt_x, tgt_y = random_target_spawn()

        # kierunek rakiety przeciwnika (później można to zmieniać dynamicznie)
        target_angle = 90

        target, target_text = make_missile(
            axes[0],
            tgt_x,
            tgt_y,
            angle_deg=target_angle,
            color="red",
            label="Target"
        )

        # --- ADD RADAR AT (0,0) ---
        make_radar(axes[0], 0, 0)

        # --- ADD RADAR AT (0,0) ---
        make_radar(axes[0], 0, 0)

        # Create sweep line (required for animation)
        sweep = make_radar_sweep(axes[0], 0, 0)
        current_angle = 0

        # --- Update the third subplot (first in second row) ---
        update_subplot(
            ax=axes[2],
            x_data=s_values,
            y_data=np.abs(F_s),
            label="|F(s)|",
            title="Laplace Transform of Target Position",
            xlabel="s",
            ylabel="|F(s)|",
            clear=False
        )

        # --- Save and show ---
        fig.savefig("laplace_test.png")
        print("Plot saved as laplace_test.png")

        fig.savefig("laplace_test.png")
        print("Plot saved as laplace_test.png")

        # --- Minimal radar sweep animation ---
        from matplotlib.animation import FuncAnimation
        from module.Markers import update_radar_sweep


        def animate(frame):
            global current_angle
            current_angle = (current_angle + 2) % 360
            update_radar_sweep(sweep, 0, 0, current_angle)
            return []


        ani = FuncAnimation(fig, animate, interval=30)

        plt.show()

        plt.show()

    except Exception as e:
        print("Error during Laplace test:", e)
