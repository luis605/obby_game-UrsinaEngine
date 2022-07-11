'''
Genre: Platformer

Rule: Start Small

Setting: Science Fiction

Theme: Rich Versus Poor
'''

from ursina import *
from first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

from random import uniform
import math 

from ursina.prefabs.editor_camera import EditorCamera

# Variables
global reset_position
reset_position = (0,4,0)

distance_mouse = 0


app = Ursina()

window.borderless = False

# Classes

class MovingBlock(Entity):
    def __init__(self, position=(0,2,0), movement = (42, 75)):
        super().__init__(
            model='cube',
            color = color.yellow,
            collider = 'box',
            scale=(2,.5,2),
            position=position
            ) # stuff

        self.position = position
        self.direction = 3
        self.movement = movement



    def update(self):

        
        i = 0
        
        self.x -= self.direction * time.dt

        go_left_value = self.position[0] + abs(self.x)

        if math.isclose(abs(go_left_value), int(self.movement[1]), abs_tol = 0.9):
            print("\n\n\n\n\n\n\n\n\n\n\Left")
            self.direction = 3


        if math.isclose(abs(go_left_value), int(self.movement[0]), abs_tol = 0.9):
            print("\n\n\n\n\n\n\n\n\n\n\Right")
            self.direction = -3

    

        if player.intersects(self):
            print("oi")

            player.x -= self.direction * time.dt














class VerticalMovingBlock(Entity):
    def __init__(self, position=(0,2,0), extreme=10, duration=5):
        super().__init__(
            model='cube',
            color = color.yellow,
            collider = 'box',
            scale=(2,.5,2),
            position=position
            ) # stuff

        self.extreme = extreme
        self.duration = duration

        self.animate('y', self.extreme, duration=self.duration, loop=True, curve=curve.in_out_cubic_boomerang)


    def update(self):
        print(self.position)
        if player.intersects(self):
            print("oi")

            player.position = self.position


        




class CheckPoint(Entity):
    def __init__(self, position=(-4,2,-4)):
        super().__init__(
            model='cube',
            color = color.black,
            collider = 'box',
            scale=(2,.25,2),
            position=position
            ) # stuff

        self.position = position



    def update(self):
        global reset_position

        if player.intersects(self):
            print("CheckPoint - Activated at pos {}".format(self.position))

            reset_position = self.position



# TELEPORT CLASS



class Teleport(Entity):
    def __init__(self, position=(-4,2,-4), to_where = (0,0,0)):
        super().__init__(
            model='cube',
            color = color.gold,
            collider = 'box',
            scale=(2,.25,2),
            position=position
            ) # stuff

        self.position = position
        self.to_where = to_where


    def update(self):
        if player.intersects(self):
            print("Teleport - Activated at pos {} to pos {}".format(self.position, self.to_where))
            player.position = self.to_where

















###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############
###############






# Level options
level = 1

# Lights and shaders
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, color = color.rgba(105, 102, 109, 0.01))
amb_light = AmbientLight(parent=pivot, color = color.rgba(145, 132, 39, 0.1), shadows=True)

Entity.default_shader = lit_with_shadows_shader


# Levels

reset_position = (0,4,0)



# Level 1
ground = Entity(model='plane', texture='grass', collider = 'box', scale=10)

# Part 1
lvl0_block_1 = Entity(model='cube', color = color.red, collider = 'box', scale=3, position=(4, 1, 4))
lvl0_block_2 = Entity(model='cube', color = color.green, collider = 'box', scale=2, positions = (0, 0, 4))
lvl0_block_3 = Entity(model='cube', color = color.blue, collider = 'box', scale=3.5, position=(6, 2.5, 9))

CheckPoint(position=(6, 4.25, 9))

lvl0_block_4 = Entity(model='cube', color = color.orange, collider = 'box', scale=(4,.5,2), position=(9, 3, 9))

# Part 2
lvl0_block_5 = Entity(model='cube', color = color.gray, collider = 'box', scale=(4,.5,2), position=(16, 3, 9))
lvl0_block_6 = Entity(model='cube', color = color.gray, collider = 'box', scale=(4,.5,2), position=(17, 3, 14))
lvl0_block_7 = Entity(model='cube', color = color.gray, collider = 'box', scale=(4,.5,2), position=(16, 2, 19))
lvl0_block_8 = Entity(model='cube', color = color.gray, collider = 'box', scale=(4,.5,2), position=(17, 3, 24))

MovingBlock(position=(40, 3, 24))

# Part 3
lvl0_block_9 = Entity(model='cube', color = color.gray, collider = 'box', scale=(4,.5,8), position=(42, 3, 24))

CheckPoint(position=(42, 3.25, 24))

lvl0_slope_10 = Entity(model='cube', collider='box', position=(42,3,16), scale=6, rotation=(45,0,0), texture='brick', texture_scale=(8,8))
lvl0_slope_11 = Entity(model='cube', collider='box', position=(42,3,4), scale=6, rotation=(45,0,0), texture='brick', texture_scale=(8,8))
lvl0_slope_12 = Entity(model='cube', collider='box', position=(42,3,-8), scale=6, rotation=(45,0,0), texture='brick', texture_scale=(8,8))


# Part 4 MAZE
lvl0_block_13 = Entity(model='cube', color = color.gray, collider = 'box', scale=(4,.5,2), position=(46,5,-8))
lvl0_block_14 = Entity(model='cube', color = color.gray, collider = 'box', scale=(2.75,.5,2), position=(48.5,5,-8))

CheckPoint(position=(46,5.35,-8))

lvl0_block_15 = Entity(position=Vec3(57.5, 3, -7), scale=Vec3(12, 1.5, 1), model='cube', color=Color(0.15, 0.15, 0.15, 1), collider='box', )
lvl0_block_16 = Entity(position=Vec3(64.75, 3, -7), scale=Vec3(2.5, 1.5, 1), model='cube', color=Color(0.5, 0.5, 0.5, 1), collider='box', )
lvl0_block_17 = Entity(position=Vec3(67, 3, -7), scale=Vec3(2, 1.5, 19), model='cube', color=Color(0.35, 0.35, 0.35, 1), collider='box', )

lvl0_block_17 = Entity(position=Vec3(67, 3, 10), scale=Vec3(2, 1.5, 6), model='cube', color=Color(0.35, 0.35, 0.35, 1), collider='box', )
lvl0_block_18 = Entity(position=Vec3(80, 8, 20), scale=Vec3(2, 1.5, 6), model='cube', color=Color(0.35, 0.35, 0.35, 1), collider='box', )

Teleport(position = (67, 4, 10), to_where = lvl0_block_18.position) 

lvl0_block_19 = Entity(position=Vec3(67, 3, -23), scale=Vec3(2, 1.5, 6), model='cube', color=Color(0.35, 0.35, 0.35, 1), collider='box', )
lvl0_block_20 = Entity(position=Vec3(80, 8, -27), scale=Vec3(2, 1.5, 6), model='cube', color=Color(0.35, 0.35, 0.35, 1), collider='box', )

Teleport(position = (67, 4, -23), to_where = lvl0_block_20.position) 
VerticalMovingBlock(position = (85, 8, -27), extreme=20)

lvl0_block_21 = Entity(position=Vec3(90, 20, -27), scale=Vec3(2, 1.5, 6), model='cube', color=Color(0.35, 0.35, 0.35, 1), collider='box', )

# Last Part
lvl0_block_22 = Entity(position=Vec3(95, 20, -24), scale=Vec3(2, 1.5, 2), model='cube', color=color.orange, collider='box', )
lvl0_block_25 = Entity(position=Vec3(100, 20, -27), scale=Vec3(2, 1.5, 2), model='cube', color=color.orange, collider='box', )
lvl0_block_26 = Entity(position=Vec3(105, 20, -28), scale=Vec3(2, 1.5, 2), model='cube', color=color.orange, collider='box', )
lvl0_block_27 = Entity(position=Vec3(110, 20, -24), scale=Vec3(2, 1.5, 2), model='cube', color=color.orange, collider='box', )
lvl0_block_28 = Entity(position=Vec3(115, 20, -28), scale=Vec3(2, 1.5, 2), model='cube', color=color.orange, collider='box', )
lvl0_block_29 = Entity(position=Vec3(120, 20, -25), scale=Vec3(2, 1.5, 2), model='cube', color=color.orange, collider='box', )


# Level 1
lvl1_block_1 = Entity(position=Vec3(1120, 120, -125), scale=Vec3(2, 1.5, 2), model='cube', color=color.orange, collider='box', )

Teleport(position = (125, 4, -25), to_where = lvl1_block_1.position)

# World/Game
sky_texture = load_texture("skybox1.png")
Sky(texture=sky_texture)


ec = EditorCamera(rotation_smoothing=10, enabled = False)




player = FirstPersonController(model = 'sphere',
                               origin = (0, -.5, 0),
                               collider = 'box',
                               )


player.camera_pivot.z = -1.5  # move the camera behind the player model
player.camera_pivot.y = 3.5  # move the camera a little higher



outline_box = Entity(model='wireframe_cube', color=color.gray, scale=150, position=Vec3(0,0,0))



# Update and Input Functions
pause_handler = Entity(ignore_paused=True)
pause_text = Text('PAUSED - [Press ESC]', origin=(0,0), scale=2, enabled=False) # Make a Text saying "PAUSED" just to make it clear when it's paused.

def pause_handler_input(key):
    if key == 'escape':
        player.enabled = not player.enabled 
        application.paused = not application.paused # Pause/unpause the game.
        pause_text.enabled = application.paused     # Also toggle "PAUSED" graphic.

pause_handler.input = pause_handler_input   # Assign the input funct
        





# Functions
def reset():
    player.position = reset_position


def update():

        
    if player.y <= -150:
        reset()

        
    pass
def input(key):
    global distance_mouse
    
    print(key)
    if key == "k":
        reset()

    if key == "t":
        player.disable()
        ec.enable()

    if key == "h":
        player.enable()
        ec.disable()

    if key == "l":
        def submit():
            teleport_position = eval(position_field.text)

            print(teleport_position)
            player.enable()
            player.position = teleport_position
            
        player.disable()

        position_field = InputField(y=-.12, limit_content_to='0123456789,- ', color=color.gray.tint(-.4))
        Button('Teleport', scale=.1, color=color.cyan.tint(-.4), y=-.26, on_click=submit).fit_to_text()


    if key == 'scroll up':
        
        distance_mouse += 0.5
        print(distance_mouse)

        if distance_mouse >= 5:
            distance_mouse = 5

        player.camera_pivot.y = distance_mouse


    if key == 'scroll down':
        distance_mouse -= 0.5

        if distance_mouse <= -5:
            distance_mouse = -5

        player.camera_pivot.y = distance_mouse
    




if level == 1:

    tutorial_introduction = Text("Hello. I'm happy to see you here!", origin=(0,0), scale=2, enabled = True, visible = False) # Make a Text saying "PAUSED" just to make it clear when it's paused.
    tutorial_introduction.fade_out(0, duration = 0)
    tutorial_introduction.fade_in(1, duration = 1)
    
    tutorial_whereAmI = Text("You are in the first level, level number 0,\nalso known as the Tutorial Level", origin=(0,0), scale=2, enabled=False) # Make a Text saying "PAUSED" just to make it clear when it's paused.
    tutorial_wasd = Text('To Move Around You Can Press [ WASD ] keys on your keyboard', origin=(0,0), scale=2, enabled=False) # Make a Text saying "PAUSED" just to make it clear when it's paused.

    def tutorial_introduction_init():
        tutorial_introduction.fade_in(value=1, duration=.5)   

    def tutorial_introduction_end():
        tutorial_introduction.enabled=False
##        
##    invoke(tutorial_introduction_init, delay = 2)
##    invoke(tutorial_introduction_end, delay = 5)
app.run()
