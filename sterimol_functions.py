import numpy as np
from matplotlib.colors import hex2color
import pyvista as pv
from pyvistaqt import BackgroundPlotter
from morfeus.plotting import get_drawing_arrow
from morfeus.data import jmol_colors

def plot_sterimol_3d(sterimol, atom_scale=0.5, show_labels=True):
    """
    Visualize a Sterimol object in 3D with atom spheres and L, B1, B5 arrows.
    """

    p = BackgroundPlotter()
    p.set_background("white")

    # Draw atoms
    for atom in sterimol._atoms:
        color = hex2color(jmol_colors[atom.element])
        if atom.element == 0:
            radius = 0.5 * atom_scale
        else:
            radius = atom.radius * atom_scale
        sphere = pv.Sphere(center=list(atom.coordinates), radius=radius)
        opacity = 0.25 if atom.index in sterimol._excluded_atoms else 1
        p.add_mesh(sphere, color=color, opacity=opacity, name=str(atom.index))

    # Add L arrow
    start_L = sterimol._dummy_atom.coordinates
    length_L = np.linalg.norm(sterimol.L)
    direction_L = sterimol.L / length_L
    L_arrow = get_drawing_arrow(start=start_L, direction=direction_L, length=length_L)
    p.add_mesh(L_arrow, color="steelblue")

    # Add B1 arrow
    start_B = sterimol._attached_atom.coordinates
    length_B1 = np.linalg.norm(sterimol.B_1)
    direction_B1 = sterimol.B_1 / length_B1
    B1_arrow = get_drawing_arrow(start=start_B, direction=direction_B1, length=length_B1)
    p.add_mesh(B1_arrow, color="orange")

    # Add B5 arrow
    length_B5 = np.linalg.norm(sterimol.B_5)
    direction_B5 = sterimol.B_5 / length_B5
    B5_arrow = get_drawing_arrow(start=start_B, direction=direction_B5, length=length_B5)
    p.add_mesh(B5_arrow, color="green")

    # Optionally, add labels at the arrow tips
    if show_labels:
        points = np.vstack([
            start_L + direction_L * length_L,
            start_B + direction_B1 * length_B1,
            start_B + direction_B5 * length_B5
        ])
        labels = ["L", "B1", "B5"]
        p.add_point_labels(points, labels, text_color="black", font_size=30, bold=False, show_points=False, point_size=1)

    return p

def shorten_vector(start, vec, shorten_by=1.0):
    length = np.linalg.norm(vec)
    if length <= shorten_by:
        return start, start  # or handle as you wish
    direction = vec / length
    new_vec = vec - direction * shorten_by
    end = start + new_vec
    return start, end

def build_axes(A, B, C):
    x = (B - A) / np.linalg.norm(B - A)
    tmp = (C - A)
    z = np.cross(x, tmp)
    z /= np.linalg.norm(z)
    y = np.cross(z, x)
    return np.stack([x, y, z]).T  # 3x3 matrix