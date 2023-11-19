import bpy


'''
Sets scene to printable world! 
author: JeancaSeven
'''

def main():
    bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
    bpy.context.scene.unit_settings.scale_length = 0.001
    bpy.context.space_data.overlay.grid_scale = 0.001
    bpy.context.space_data.clip_start = 0.1
    bpy.context.space_data.clip_end = 10000

if __name__ == "__main__":
    main()
