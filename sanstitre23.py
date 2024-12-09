# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:46:53 2024

@author: pc
"""

import cv2
import numpy as np
from scipy.optimize import least_squares

# Fonction de triangulation 3D
def triangulate_points(points_cam1, points_cam2, P1, P2):
    points_3d = cv2.triangulatePoints(P1, P2, points_cam1.T, points_cam2.T)
    return points_3d[:3] / points_3d[3]

# Charger les flux de deux caméras
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

# Matrices de projection simulées
P1 = np.eye(3, 4)
P2 = np.array([[1, 0, 0, -0.5], [0, 1, 0, 0], [0, 0, 1, 0]])

while cap1.isOpened() and cap2.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    if not ret1 or not ret2:
        break
    
    # Détection des points clés avec SIFT
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY), None)
    kp2, des2 = sift.detectAndCompute(cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY), None)
    
    # Association des points
    matcher = cv2.BFMatcher()
    matches = matcher.knnMatch(des1, des2, k=2)
    good_matches = [m[0] for m in matches if len(m) == 2 and m[0].distance < 0.75 * m[1].distance]
    
    points_cam1 = np.float32([kp1[m.queryIdx].pt for m in good_matches])
    points_cam2 = np.float32([kp2[m.trainIdx].pt for m in good_matches])
    
    # Triangulation 3D
    points_3d = triangulate_points(points_cam1, points_cam2, P1, P2)
    print("Points 3D:", points_3d)
