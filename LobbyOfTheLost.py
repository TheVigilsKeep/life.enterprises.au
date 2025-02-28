import trimesh
import pyglet
from pyglet.gl import *

def load_and_display_obj(obj_file_path):
    """Loads an OBJ file and displays it in a Pyglet window."""

    try:
        mesh = trimesh.load(obj_file_path)
    except FileNotFoundError:
        print(f"Error: OBJ file not found at {obj_file_path}")
        return
    except Exception as e:
        print(f"Error loading OBJ file: {e}")
        return

    window = pyglet.window.Window(width=800, height=600, resizable=True, caption="OBJ Viewer")
    rotation_x = 0
    rotation_y = 0
    zoom = 1.0

    @window.event
    def on_draw():
        window.clear()
        glEnable(GL_DEPTH_TEST)  # Enable depth testing
        glLoadIdentity()
        glTranslatef(0, 0, -5 * zoom)  # Move the object away from the camera
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)

        # Draw the mesh
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_index in face:
                vertex = mesh.vertices[vertex_index]
                glVertex3f(vertex[0], vertex[1], vertex[2])
        glEnd()

    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        nonlocal rotation_x, rotation_y
        if buttons & pyglet.window.mouse.LEFT:
            rotation_y += dx * 0.5
            rotation_x += dy * 0.5

    @window.event
    def on_mouse_scroll(x, y, dx, dy):
        nonlocal zoom
        zoom += dy * 0.1
        zoom = max(0.1, zoom) #prevent zoom from going negative or 0.

    pyglet.app.run()

if __name__ == "__main__":
    obj_file = "path/to/your/model.obj" # Replace with the actual path to your OBJ file
    load_and_display_obj(obj_file)
