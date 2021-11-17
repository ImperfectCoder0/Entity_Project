import math
import glfw
import numpy
import pyrr
from OpenGL.GL import *
from OpenGL.GL.shaders import *

width, height = 500, 500


def draw():
    global shader
    cube = [-0.5, -0.5,  0.5, width/height, 1.0, 0.0, 0.0,
            0.5, -0.5,  0.5, width/height, 0.0, 1.0, 0.0,
            0.5,  0.5,  0.5, width/height, 0.0, 0.0, 1.0,
            -0.5,  0.5,  0.5, width/height, 1.0, 1.0, 1.0,

            -0.5, -0.5, -0.5, width/height, 1.0, 0.0, 0.0,
            0.5, -0.5, -0.5, width/height, 0.0, 1.0, 0.0,
            0.5,  0.5, -0.5, width/height, 0.0, 0.0, 1.0,
            -0.5,  0.5, -0.5, width/height, 1.0, 1.0, 1.0]

    cube = numpy.array(cube, dtype = numpy.float32)

    indices = [0, 1, 2, 3,
               4, 5, 6, 7]

    indices = numpy.array(indices, dtype= numpy.uint32)

    vertex_shader_ = """
        #version 140
        in vec4 position;
        in vec3 color;
        uniform mat4 transform;
        out vec4 out_color;
        void main(){
            
            gl_Position = transform*position;
            out_color = vec4(color.rgb, 1);

        };
    
    """

    fragment_shader_ = """
        #version 140
        in vec4 out_color;
        
        void main(){
        
            gl_FragColor = out_color;
        };
    
    """

    shader = compileProgram(compileShader(vertex_shader_, GL_VERTEX_SHADER),
                            compileShader(fragment_shader_, GL_FRAGMENT_SHADER))
    glUseProgram(shader)

    VBO = glGenBuffers(1)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, cube.nbytes, cube, GL_STATIC_DRAW)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 4, GL_FLOAT, GL_FALSE, 28, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)
    color = glGetAttribLocation(shader, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 28, ctypes.c_void_p(16))
    glEnableVertexAttribArray(color)

    rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time() )
    rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time() )

    transformLoc = glGetUniformLocation(shader, "transform")
    glUniformMatrix4fv(transformLoc, 1, GL_FALSE, rot_x * rot_y)


def Screen():
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glDrawArrays(GL_POLYGON, 0, 70)
    draw()
    glViewport(0, 0, width, height)


def main():
    global width, height
    if not glfw.init():
        return
    window = glfw.create_window(500, 500, "Opengl GLFW Window", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        Screen()
        width, height = glfw.get_window_size(window)

        print(width, height)
        glViewport(0, 0, width, height)
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == '__main__':
    main()
