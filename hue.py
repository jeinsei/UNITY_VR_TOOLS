from phue import Bridge

#192.168.1.50
b = Bridge("192.168.1.50")
# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()
# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

lights = b.lights

# Print light names
for l in lights:
    print(l.name)
    l.on = True
    

# Set brightness of each light to 127
for l in lights:
    l.brightness = 200
    l.saturation = 254
    # l.hue = 6200 # jaune
    l.hue = 60000 # jaune
    # l.hue = 6200

    # 1 rouge
    # 500 orange
    # 10000 jaune 
    # 20000 vert
    # 30000 vert turquoise
    # 40000 bleu claire
    # 50000 violet
    # 60000 rose



