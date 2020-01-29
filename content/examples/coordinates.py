# -*- coding: utf-8 -*-
"""
A module for working with coordinates.
Uses numpy arrays.
"""

import math

import numpy


def rotate(coords, angle):
    """Rotates a matrix of x,y coordinates.

    Arguments:
        coords: numpy array of coordinates, with n rows and 2 columns (x,y).
        angle: Angle of rotation, in degrees.

    Returns: numpy array of rotated coordinates.
    """

    theta = math.radians(angle)

    rotation_matrix = numpy.array([[math.cos(theta), math.sin(theta)],
                                   [-math.sin(theta), math.cos(theta)]])

    return numpy.matmul(coords, rotation_matrix)
