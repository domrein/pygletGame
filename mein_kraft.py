import pyglet

window = pyglet.window.Window()

images = {}
def make_image(imageName, scaleFactor):
    image = pyglet.resource.image(imageName + '.png')
    images[imageName] = image
    # resize with nearest neighbor
    texture = image.get_texture()
    pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
    texture.width = image.width * scaleFactor
    texture.height = image.height * scaleFactor

make_image('kevin', 8)
make_image('kevin_socks', 8)

keys = {
    'space': False,
    'left': False,
    'right': False,
    'up': False,
    'down': False
}

kevin = {'x': 0, 'y': 0}

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

# game logic
def update(dt):
    if keys['right']:
        kevin['x'] += 5
    if keys['left']:
        kevin['x'] -= 5
    if keys['up']:
        kevin['y'] += 5
    if keys['down']:
        kevin['y'] -= 5

@window.event
def on_draw():
    window.clear()
    images['kevin_socks'].blit(kevin['x'], kevin['y'])

pyglet.clock.schedule_interval(update, 1 / 60)
pyglet.app.run()
