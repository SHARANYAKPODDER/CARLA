# -*- coding: utf-8 -*-
"""carlacode2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UV7GLe0Lau6Pkfk0uNuBhnOLX-6MKdcs
"""

import glob
import os
import sys
import cv2
import random
import matplotlib.pyplot as plt
import time
import numpy as np
import argparse
import carla

try:
  sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
      sys.version_info.major,
      sys.version_info.minor,
      'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
  pass

actor_list = []
try:
  client = carla.Client("localhost",2000)
  client.set_timeout(2.0)

  world = client.load_world("town02")

  blueprint_library = world.get_blueprint_library()

  bp = blueprint_library.filter("cybertruck")[0]
  print(bp)

  spawn_point = random.choice(world.get_map().get_spawn_points())

  vehicle = world.spawn_actor(bp, spawn_point)
  vehicle.apply_control(carla.VehicleControl(throttle = 1.0, steer = 0.0))
  actor_list.append(vehicle)

  time.sleep(50)

  # for destroying after server off

finally:
  print('destroying actors')
  for actor in actor_list:
    actor.destroy()
  print('done.')
