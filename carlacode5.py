import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import argparse
import datetime
import logging
import math

# global variables for CARLA/Sensor/MyCamera


SensorType= CAMERA
PostProcessing= Depth
ImageSizeX=800
ImageSizeY=600
FOV=90
PositionX=0.30
PositionY=0
PositionZ=1.30
RotationPitch=0
RotationRoll=0
RotationYaw=0 
        
        
camera = carla.sensor.Camera('MyCamera', PostProcessing='Depth')
camera.set(FOV=90.0)
camera.set_image_size(800, 600)
camera.set_position(x=0.30, y=0, z=1.30)
camera.set_rotation(pitch=0, yaw=0, roll=0)
        
carla_settings.add_sensor(camera)







