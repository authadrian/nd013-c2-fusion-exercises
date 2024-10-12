"""

Created by Adrian as a sandbox to help inspect and solve things,
without cluttering the codebase with it.

"""


from PIL import Image
import io
import sys
import os
import cv2
import numpy as np
import zlib

## Add current working directory to path
sys.path.append(os.getcwd())

## Waymo open dataset reader
from tools.waymo_reader.simple_waymo_open_dataset_reader import dataset_pb2


# Adrian created function for experinments
def print_dataset_labels(frame):
    """
    prints labels in the dataset to help me understand how to interact with it.

    args:
    single frame of waymo dataset in .tfrecord format.

    out:
    print something to the terminal. I keep changing it.
    """
    
    # camera labels printed
    """
    for i, label in enumerate(frame.camera_labels):
        print("Camera_label number #",i ,"looks like this: \n", label)
    """
    
    ## lidar = [obj for obj in frame.lasers if obj.name == lidar_name][0]

    for i, label in enumerate(frame.laser_labels):
        print("Laser / Lidar label number #",i ,"looks like this: \n", label)


def print_laser_calibs(frame):
    
    # load lidar structure
    lidar_name = dataset_pb2.LaserName.TOP
    calib_lidar = [obj for obj in frame.context.laser_calibrations if obj.name == lidar_name][0]

    # print to terminal for inspection
    print("Calib_lidar print test: \n", calib_lidar)


# Lidar 2.8 _ Count the beams in the TOP Lidar sensor
def print_laser_beamcount(frame):

    # load lidar structure
    lidar_name = dataset_pb2.LaserName.TOP
    calib_lidar = [obj for obj in frame.context.laser_calibrations if obj.name == lidar_name][0]
    
    beamcount = 0
    for beam in calib_lidar.beam_inclinations:
        beamcount += 1


    print("number of LEDs in TOP Lidar = " + str(beamcount))


# Lidar 2.8 _ Print out the calibration matrix of a lidar sensor
def print_lidar_callib_matrix(frame, lidar_name):

    # get lidar calibration data
    calib_lidar = [obj for obj in frame.context.laser_calibrations if obj.name == lidar_name][0]

    # print extrinsic callib matrix
    print("\n", "Extrinsic callib matrix: \n", np.reshape(calib_lidar.extrinsic.transform, (4,-1)), "\n")
    
