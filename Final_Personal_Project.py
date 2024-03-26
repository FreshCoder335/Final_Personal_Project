import bpy
from math import radians

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create a cube
bpy.ops.mesh.primitive_cube_add(size=2)
cube = bpy.context.object

# Set up material for the cube
mat = bpy.data.materials.new(name="CubeMaterial")
cube.data.materials.append(mat)
mat.diffuse_color = (0.8, 0.2, 0.2, 1)

# Set up animation
cube.rotation_mode = 'XYZ'
cube.rotation_euler = (0, 0, 0)

# Define animation frames
frame_start = 1
frame_end = 100

# Set keyframes for rotation
cube.keyframe_insert(data_path="rotation_euler", index=2, frame=frame_start)
cube.rotation_euler = (0, 0, radians(360))
cube.keyframe_insert(data_path="rotation_euler", index=2, frame=frame_end)

# Set up camera
bpy.ops.object.camera_add(location=(6, -6, 6))
camera = bpy.context.object
camera.rotation_euler = (radians(45), 0, radians(45))

# Set camera as active and add tracking constraint
bpy.context.scene.camera = camera
track_constraint = camera.constraints.new(type='TRACK_TO')
track_constraint.target = cube
track_constraint.track_axis = 'TRACK_NEGATIVE_Z'
track_constraint.up_axis = 'UP_Y'

# Set up lighting
bpy.ops.object.light_add(type='SUN', location=(10, -10, 10))
light = bpy.context.object
light.data.energy = 2

# Set up the scene
scene = bpy.context.scene
scene.frame_start = frame_start
scene.frame_end = frame_end

# Render settings
scene.render.engine = 'CYCLES'
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = "//output.png"
scene.cycles.samples = 100

# Render the scene
bpy.ops.render.render(write_still=True)

# Print statement
print("Script execution completed.")

# Add a text object
bpy.ops.object.text_add(location=(0, 0, 3))
text = bpy.context.object
text.data.body = "Blender Script"

# Scale the text
text.scale = (2, 2, 2)

# Add modifier to the text
bpy.ops.object.modifier_add(type='SUBSURF')
text.modifiers["Subdivision"].levels = 2

# Set text material
text_mat = bpy.data.materials.new(name="TextMaterial")
text.data.materials.append(text_mat)
text_mat.diffuse_color = (0.2, 0.8, 0.2, 1)

# Add a sphere
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 4))
sphere = bpy.context.object

# Set up sphere material
sphere.data.materials.append(mat)

# Add a torus
bpy.ops.mesh.primitive_torus_add(location=(4, 4, 2))
torus = bpy.context.object

# Set up torus material
torus.data.materials.append(mat)

# Add a plane
bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
plane = bpy.context.object

# Set up plane material
plane.data.materials.append(mat)

# Add a cylinder
bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, location=(-4, -4, 1))
cylinder = bpy.context.object

# Set up cylinder material
cylinder.data.materials.append(mat)

# Add a cone
bpy.ops.mesh.primitive_cone_add(radius1=1, depth=2, location=(4, -4, 1))
cone = bpy.context.object

# Set up cone material
cone.data.materials.append(mat)

# Add a monkey head
bpy.ops.mesh.primitive_monkey_add(location=(-4, 4, 2))
monkey = bpy.context.object

# Set up monkey material
monkey.data.materials.append(mat)

# Add a lamp
bpy.ops.object.light_add(type='POINT', location=(0, 0, 5))
lamp = bpy.context.object

# Set lamp energy
lamp.data.energy = 10

# Add a floor grid
bpy.ops.mesh.primitive_grid_add(size=10, subdivisions=10, location=(0, 0, 0))
floor = bpy.context.object

# Set up floor material
floor.data.materials.append(mat)

# Add a UV sphere
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 6))
uv_sphere = bpy.context.object

# Set up UV sphere material
uv_sphere.data.materials.append(mat)

# Add a text object
bpy.ops.object.text_add(location=(0, 0, 7))
text2 = bpy.context.object
text2.data.body = "Extra Text"

# Scale the text
text2.scale = (2, 2, 2)

# Add modifier to the text
bpy.ops.object.modifier_add(type='SUBSURF')
text2.modifiers["Subdivision"].levels = 2

# Set text material
text2.data.materials.append(text_mat)

# Add a bezier curve
bpy.ops.curve.primitive_bezier_circle_add(radius=3, location=(0, 0, 8))
bezier_curve = bpy.context.object

# Set up bezier curve material
bezier_curve.data.materials.append(mat)

# Add a camera constraint
track_constraint2 = camera.constraints.new(type='TRACK_TO')
track_constraint2.target = uv_sphere
track_constraint2.track_axis = 'TRACK_NEGATIVE_Z'
track_constraint2.up_axis = 'UP_Y'

# Add a path curve
bpy.ops.curve.primitive_bezier_curve_add(radius=1, location=(0, 0, 9))
path_curve = bpy.context.object

# Set up path curve material
path_curve.data.materials.append(mat)
