'''
Genre: Platformer

Rule: Start Small

Setting: Science Fiction

Theme: Rich Versus Poor
'''

from ursina import *
from first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader



# Variables
global reset_position
reset_position = (0,4,0)

distance_mouse = 0


app = Ursina()




# Level options
level = 1

# Lights and shaders
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, color = color.rgba(105, 102, 109, 0.01))
amb_light = AmbientLight(parent=pivot, color = color.rgba(145, 132, 39, 0.1), shadows=True)

Entity.default_shader = lit_with_shadows_shader



# Update and Input Functions
pause_handler = Entity(ignore_paused=True)
pause_text = Text('PAUSED - [Press ESC]', origin=(0,0), scale=2, enabled=False) # Make a Text saying "PAUSED" just to make it clear when it's paused.

def pause_handler_input(key):
    if key == 'escape':
        player.enabled = not player.enabled 
        application.paused = not application.paused # Pause/unpause the game.
        pause_text.enabled = application.paused     # Also toggle "PAUSED" graphic.

pause_handler.input = pause_handler_input   # Assign the input funct
        



sky_texture = load_texture("skybox1.png")
Sky(texture=sky_texture)





player = FirstPersonController(model = 'cube',
                               origin = (0, -1, 0),
                               collider = 'box',
                               )


player.camera_pivot.z = -1.5  # move the camera behind the player model
player.camera_pivot.y = 3.5  # move the camera a little higher


def update():
##    q = boxcast(Vec3(0,0,0), direction=(0,0,1), distance=150, thickness=(1,1), traverse_target=scene, ignore=list(), debug=False)
##    if q.hit:
##        print("Reseting")
##        player.position = (0,2,0)
    pass
def input(key):
    global distance_mouse
    
    print(key)
    if key == "k":
        reset()

    if key == 'scroll up':
        
        distance_mouse += 0.5
        print(distance_mouse)

        if distance_mouse >= 5:
            distance_mouse = 5


    if key == 'scroll down':
        distance_mouse -= 0.5
        player.camera_pivot.y = distance_mouse

        if distance_mouse <= -5:
            distance_mouse = -5
    
def generate_lvl1():
    global reset_position
    reset_position = (0,4,0)
    
    ground = Entity(model='plane', texture='grass', collider = 'box', scale=10)

    # Part 1
    block_1 = Entity(model='cube', color = color.red, collider = 'box', scale=3, position=(4, 1, 4))
    block_2 = Entity(model='cube', color = color.green, collider = 'box', scale=2, positions = (0, 0, 4))
    block_3 = Entity(model='cube', color = color.blue, collider = 'box', scale=3.5, position=(6, 2.5, 9))
    block_4 = Entity(model='cube', color = color.orange, collider = 'box', scale=(4,.5,2), position=(9, 3, 9))

    # Part 2
    block_5 = Entity(model='cube', color = color.gray, collider = 'box', scale=(4,.5,2), position=(16, 3, 9))
    block_6 = Entity(model='cube', color = color.gray, collider = 'box', scale=(4,.5,2), position=(17, 3, 14))
    block_7 = Entity(model='cube', color = color.gray, collider = 'box', scale=(4,.5,2), position=(16, 2, 19))
    block_8 = Entity(model='cube', color = color.gray, collider = 'box', scale=(4,.5,2), position=(17, 3, 24))

    #Part 3
    block_9 = Entity(model='cube', color = color.yellow, collider = 'box', scale=(2,.5,2), position=(22, 3, 24))




    trigger_box = Entity(model='wireframe_cube', color=color.gray, scale=150, collider='box', position=Vec3(1,0,2))



def reset():
    if level == 1:
        player.position = reset_position
    

            
if level == 1:
    generate_lvl1()

    
app.run()
