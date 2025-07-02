from pymol import cmd, cgo
import numpy as np

def draw_arrow(start, end, color=(0.5, 0.5, 0.5), width=0.1, cap_scale=2.5, alpha=0.8, name="sterimol_arrow"):
    """
    Draw an arrow in PyMOL from start to end (absolute coordinates), with a cap.
    start, end: (x, y, z) coordinates in the same frame as your molecule.
    color: (r, g, b) tuple.
    width: shaft radius (in Angstroms).
    cap_scale: cone radius is width*cap_scale, cone length is width*cap_scale*2.
    alpha: transparency.
    name: name for the CGO object.
    """
    start = np.array(start)
    end = np.array(end)
    direction = end - start
    length = np.linalg.norm(direction)
    if length == 0:
        return
    direction /= length

    cone_length = width * cap_scale * 2
    cone_radius = width * cap_scale
    shaft_end = end - direction * cone_length

    arrow = [
        cgo.CYLINDER, *start, *shaft_end, width, *color, *color,
        cgo.CONE, *shaft_end, *end, cone_radius, 0.0, *color, *color, 1.0, 0.0,
    ]
    cmd.load_cgo(arrow, name)
    cmd.set("cgo_line_width", width*10, name)  # optional, for lines

cmd.extend("draw_arrow", draw_arrow)