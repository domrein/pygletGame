import pyglet

window = pyglet.window.Window()

pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

images = {}
def make_image(imageName, scaleFactor):
    image = pyglet.resource.image('%s.png'%(imageName))
    images[imageName] = image
    # resize with nearest neighbor
    texture = image.get_texture()
    pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
    texture.width = image.width * scaleFactor
    texture.height = image.height * scaleFactor

make_image('pineapple_man', 8)
make_image('kylo_trump', 8)

keys = {
    'space': False,
    'left': False,
    'right': False,
    'up': False,
    'down': False
}

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
    images['pineapple_man'].blit(player['x'], player['y'])
    images['kylo_trump'].blit(100, 100)

player = {'x': 0, 'y': 0}

def update(dt):
    if keys['right']:
        player['x'] += 5
    if keys['left']:
        player['x'] -= 5
    if keys['up']:
        player['y'] += 5
    if keys['down']:
        player['y'] -= 5

pyglet.clock.schedule_interval(update, 1 / 60)

pyglet.app.run()
