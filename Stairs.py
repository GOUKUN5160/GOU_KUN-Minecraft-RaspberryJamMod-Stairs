import mcpi.minecraft as minecraft
import math
import time

mc = minecraft.Minecraft()


while True:
    x,y,z = mc.player.getPos()
    distance = 1
    rad = math.radians(mc.player.getRotation())
    x1 = 0-math.sin(rad)*distance
    z1 = math.cos(rad)*distance

    if 0.0006462497831514223 > rad and -0.78485008484511 < rad:
        b=2
        mc.setBlock(x+x1,y,z+z1,53,b)
        time.sleep(0.001)


    if 0.7852897061620548 > rad and 0.0006462497831514223 < rad:
        b=2
        mc.setBlock(x+x1,y,z+z1,53,b)
        time.sleep(0.001)


    if 1.5711064519038362 > rad and 0.7852897061620548 < rad:
        b=1
        mc.setBlock(x+x1,y,z+z1,53,b)
        time.sleep(0.001)


    if 2.3567598792917686 > rad and 1.5711064519038362 < rad:
        b=1
        mc.setBlock(x+x1,y,z+z1,53,b)
        time.sleep(0.001)


    if 3.1414014386235256 > rad and 2.3567598792917686 < rad:
        b=3
        mc.setBlock(x+x1,y,z+z1,53,b)
        time.sleep(0.001)

    if -3.141350838562814 > rad and -2.3557998097187953 < rad:
        b=3
        mc.setBlock(x+x1,y,z+z1,53,b)
        time.sleep(0.001)


    if -1.5708293499924135 > rad and -2.3557998097187953 < rad:
        b=8
        mc.setBlock(x+x1,y,z+z1,53,b)
        time.sleep(0.001)

    if -0.78485008484511 > rad and -1.5708293499924135 < rad:
        b=8
        mc.setBlock(x+x1,y,z+z1,53,b)
        time.sleep(0.001)