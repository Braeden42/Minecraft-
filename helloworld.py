#Makes tnt fall and explode, kind of like vanilla. Sadly, only one tnt can be going at a time.

from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep

def init():
    mc = Minecraft.create("10.183.3.25")
    return mc

def init():
    mc = Minecraft.create("10.183.3.25")
    return mc

def tnt(mc,x,y,z):
    for each in range(30):
        for other in range(1):
            mc.setBlock(x,y,z,46)
            sleep(0.1)
            mc.setBlock(x,y,z,80)
            sleep(0.025)
        if mc.getBlock(x,y-1,z)==0:
            mc.setBlock(x,y,z,0)
            y=y-7
    mc.postToChat("BOOM")
    sphere(mc,x,y,z)

def sphere(mc,x,y,z):
    radius=50
    for x1 in range(radius*-1,radius+1):
        for y1 in range(radius*-1,radius+1):
            for z1 in range(radius*-1,radius+1):
                if (x1**2)+(y1**2)+(z1**2)<=(radius+1)**2:
                        mc.setBlocks(x-0, y+0, z+2, x-0, y+0, z+3, 35,15)
                        mc.setBlocks(x-0, y+0, z+4, x-0, y+0, z+4, 35,15)
                        mc.setBlocks(x-0, y+0, z+5, x-0, y+0, z+6, 35,15)
                        mc.setBlocks(x-0, y+0, z+7, x-0, y+0, z+7, 35,15)
                        mc.setBlocks(x-0, y+0, z+8, x-0, y+0, z+9, 35,15)
                        mc.setBlocks(x-0, y+1, z+2, x-0, y+1, z+3, 35,15)
                        mc.setBlocks(x-0, y+1, z+4, x-0, y+1, z+7, 35,15)
                        mc.setBlocks(x-0, y+1, z+8, x-0, y+1, z+9, 35,15)
                        mc.setBlocks(x-0, y+2, z+2, x-0, y+2, z+3, 35,15)
                        mc.setBlocks(x-0, y+2, z+4, x-0, y+2, z+7, 35,15)
                        mc.setBlocks(x-0, y+2, z+8, x-0, y+2, z+9, 35,15)
                        mc.setBlocks(x-0, y+3, z+2, x-0, y+3, z+4, 35,15)
                        mc.setBlocks(x-0, y+3, z+5, x-0, y+3, z+6, 35,15)
                        mc.setBlocks(x-0, y+3, z+7, x-0, y+3, z+9, 35,15)
                        mc.setBlocks(x-0, y+4, z+2, x-0, y+4, z+2, 35,15)
                        mc.setBlocks(x-0, y+4, z+3, x-0, y+4, z+4, 35,2)
                        mc.setBlocks(x-0, y+4, z+5, x-0, y+4, z+6, 35,15)
                        mc.setBlocks(x-0, y+4, z+7, x-0, y+4, z+8, 35,2)
                        mc.setBlocks(x-0, y+4, z+9, x-0, y+4, z+9, 35,15)
                        mc.setBlocks(x-0, y+5, z+2, x-0, y+5, z+2, 35,15)
                        mc.setBlocks(x-0, y+5, z+3, x-0, y+5, z+4, 35,15)
                        mc.setBlocks(x-0, y+5, z+5, x-0, y+5, z+6, 35,15)
                        mc.setBlocks(x-0, y+5, z+7, x-0, y+5, z+8, 35,15)
                        mc.setBlocks(x-0, y+5, z+9, x-0, y+5, z+9, 35,15)
                        mc.setBlocks(x-0, y+6, z+2, x-0, y+6, z+9, 35,15)
                        mc.setBlocks(x-0, y+7, z+2, x-0, y+7, z+9, 35,15)
                        
                        mc.setBlocks(x+0, y+0, z-2, x+0, y+0, z-3, 35)
                        mc.setBlocks(x+0, y+0, z-4, x+0, y+0, z-4, 35)
                        mc.setBlocks(x+0, y+0, z-5, x+0, y+0, z-6, 35)
                        mc.setBlocks(x+0, y+0, z-7, x+0, y+0, z-7, 35)
                        mc.setBlocks(x+0, y+0, z-8, x+0, y+0, z-9, 35)
                        mc.setBlocks(x+0, y+1, z-2, x+0, y+1, z-3, 35)
                        mc.setBlocks(x+0, y+1, z-4, x+0, y+1, z-7, 35)
                        mc.setBlocks(x+0, y+1, z-8, x+0, y+1, z-9, 35)
                        mc.setBlocks(x+0, y+2, z-2, x+0, y+2, z-3, 35,8)
                        mc.setBlocks(x+0, y+2, z-4, x+0, y+2, z-7, 35,8)
                        mc.setBlocks(x+0, y+2, z-8, x+0, y+2, z-9, 35)
                        mc.setBlocks(x+0, y+3, z-2, x+0, y+3, z-4, 35)
                        mc.setBlocks(x+0, y+3, z-5, x+0, y+3, z-6, 35)
                        mc.setBlocks(x+0, y+3, z-7, x+0, y+3, z-9, 35)
                        mc.setBlocks(x+0, y+4, z-2, x+0, y+4, z-2, 35)
                        mc.setBlocks(x+0, y+4, z-3, x+0, y+4, z-4, 35,8)
                        mc.setBlocks(x+0, y+4, z-5, x+0, y+4, z-6, 35)
                        mc.setBlocks(x+0, y+4, z-7, x+0, y+4, z-8, 35,8)
                        mc.setBlocks(x+0, y+4, z-9, x+0, y+4, z-9, 35)
                        mc.setBlocks(x+0, y+5, z-2, x+0, y+5, z-2, 35)
                        mc.setBlocks(x+0, y+5, z-3, x+0, y+5, z-4, 35)
                        mc.setBlocks(x+0, y+5, z-5, x+0, y+5, z-6, 35)
                        mc.setBlocks(x+0, y+5, z-7, x+0, y+5, z-8, 35)
                        mc.setBlocks(x+0, y+5, z-9, x+0, y+5, z-9, 35)
                        mc.setBlocks(x+0, y+6, z-2, x+0, y+6, z-9, 35)
                        mc.setBlocks(x+0, y+7, z-2, x+0, y+7, z-9, 35) 
 
                        
def checkBlock(mc):
    blockEvent=mc.events.pollBlockHits()
    for each in blockEvent:
        x=each.pos.x
        y=each.pos.y
        z=each.pos.z
        if mc.getBlock(x,y,z)==46:
            tnt(mc,x,y,z)

def main():
    mc=init()
    while True:
        checkBlock(mc)

main()

  
# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
