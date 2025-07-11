import pya
import math

# Compute offset using 760nm * tan(12 degrees)
offset = 760 * math.tan(math.radians(12))  # ~162.05 nm

# Create a new layout and top-level cell
layout = pya.Layout()
top = layout.create_cell("TOP")

# Load the PCell from the macro system
pcell_lib = "MyPCellLibrary"  # Replace with your actual PCell library name
pcell_name = "MyPCell"  # Replace with your actual PCell name
pcell_params = {"width": 500, "height": 200}  # Modify as needed

# Create an instance of the PCell
pcell = layout.create_cell(SET, TwoDlib, ["1/0","2/0",0.2,True])

# Define instance transformations
#t_center = pya.Trans(pya.Vector(0, 0))  # Center position
t_left = pya.Trans(pya.Vector(-offset, 0))  # Left position
t_right = pya.Trans(pya.Vector(offset, 0))  # Right position

# Insert instances into the layout
top.insert(pya.CellInstArray(pcell.cell_index(), t_left))
#top.insert(pya.CellInstArray(pcell.cell_index(), t_center))
top.insert(pya.CellInstArray(pcell.cell_index(), t_right))

# Save the layout as GDS
layout.write("SET_shadow_test.gds")

# Open in KLayout (optional, if running interactively)
pya.Application.instance().main_window().load_layout("SET_shadow_test.gds", 1)
# Enter your Python code here

