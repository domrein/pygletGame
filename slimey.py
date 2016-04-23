import pyglet

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

make_image('slimey', 16)
make_image('tiny_baby', 16)

slimey = {'x': 0, 'y': 0}
tiny_baby = {'x': 0, 'y': 500, 'fall_rate': 1}

window = pyglet.window.Window()

keys = {
    'right': False,
    'left': False
}

score = 0

def update(dt):
    if keys['right']:
        slimey['x'] += 5
    if keys['left']:
        slimey['x'] -= 5
    tiny_baby['fall_rate'] += .2

    tiny_baby['y'] -= tiny_baby['fall_rate']
    if tiny_baby['y'] < 0:
        tiny_baby['y'] = 500
        tiny_baby['fall_rate'] = 0
    aSquared  = (tiny_baby['x'] - slimey['x']) ** 2
    bSquared  = (tiny_baby['y'] - slimey['y']) ** 2
    dist = (aSquared + bSquared) ** .5
    if dist < 50:
        global score
        score += 1
        print(score)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        keys['left'] = True
    if symbol == pyglet.window.key.RIGHT:
        keys['right'] = True

@window.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        keys['left'] = False
    if symbol == pyglet.window.key.RIGHT:
        keys['right'] = False

@window.event
def on_draw():
    window.clear()
    images['slimey'].blit(slimey['x'], 0)
    images['tiny_baby'].blit(tiny_baby['x'], tiny_baby['y'])

pyglet.clock.schedule_interval(update, 1 / 60)
pyglet.app.run()
