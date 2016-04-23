import pyglet

window = pyglet.window.Window()

# enable alpha
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

images = {}
def make_image(imageName, scaleFactor):
    image = pyglet.resource.image(imageName + '.png')
    images[imageName] = image
    # resize with nearest neighbor
    texture = image.get_texture()
    pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
    texture.width = image.width * scaleFactor
    texture.height = image.height * scaleFactor

# load images
make_image('gruby', 8)
make_image('grubaby', 8)

# define actors, all the things in our game
actors = []
def make_actor(imageName, x, y, collisionType):
    actor = {'image': imageName, 'x': x, 'y': y, 'collisionType': collisionType}
    actors.append(actor)
    return actor

player = make_actor('gruby', 0, 0, 'player')

make_actor('grubaby', 300, 400, 'baby')

keys = {
    'space': False,
    'left': False,
    'right': False,
    'up': False,
    'down': False
}

# game logic
def update(dt):
    if keys['right']:
        player['x'] += 5
    if keys['left']:
        player['x'] -= 5
    if keys['up']:
        player['y'] += 5
    if keys['down']:
        player['y'] -= 5
    for i in range(actors.len):
        print("hey")

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        keys['space'] = True
    if symbol == pyglet.window.key.LEFT:
        keys['left'] = True
    if symbol == pyglet.window.key.RIGHT:
        keys['right'] = True
    if symbol == pyglet.window.key.UP:
        keys['up'] = True
    if symbol == pyglet.window.key.DOWN:
        keys['down'] = True

@window.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        keys['space'] = False
    if symbol == pyglet.window.key.LEFT:
        keys['left'] = False
    if symbol == pyglet.window.key.RIGHT:
        keys['right'] = False
    if symbol == pyglet.window.key.UP:
        keys['up'] = False
    if symbol == pyglet.window.key.DOWN:
        keys['down'] = False

@window.event
def on_draw():
    window.clear()
    for actor in actors:
        images[actor['image']].blit(actor['x'], actor['y'])

pyglet.clock.schedule_interval(update, 1 / 60)
pyglet.app.run()
