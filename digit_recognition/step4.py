# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 04:10:49 2017

@author: Emrick
"""

#get the boonding box target
import numpy as np
top1 = []
top2 = []
top3 = []
top4 = []
top5 = []
left1 =[]
left2 =[]
left3 =[]
left4 =[]
left5 =[]
height1 = []
height2 = []
height3 = []
height4 = []
height5 = []
width1 = []
width2 = []
width3 = []
width4 = []
width5 = []

for i in range(29929):
    n = len(metadata["top"][i])
    if n<5:    
        z = np.zeros(5-n)
        top = metadata["top"][i] + z.tolist()
    else:
        top = metadata["top"][i]
    top1.append(top[0])
    top2.append(top[1])
    top3.append(top[2])
    top4.append(top[3])
    top5.append(top[4])
    n = len(metadata["left"][i])
    if n<5:    
        z = np.zeros(5-n)
        left = metadata["left"][i] + z.tolist()
    else:
        left = metadata["left"][i]
    left1.append(left[0])
    left2.append(left[1])
    left3.append(left[2])
    left4.append(left[3])
    left5.append(left[4])
    if n<5:    
        z = np.zeros(5-n)
        height = metadata["height"][i] + z.tolist()
    else:
        height = metadata["height"][i]
    height1.append(height[0])
    height2.append(height[1])
    height3.append(height[2])
    height4.append(height[3])
    height5.append(height[4])
    if n<5:    
        z = np.zeros(5-n)
        width = metadata["width"][i] + z.tolist()
    else:
        width = metadata["width"][i]
    width1.append(width[0])
    width2.append(width[1])
    width3.append(width[2])
    width4.append(width[3])
    width5.append(width[4])
  
left1 = np.array(left1)
left2 = np.array(left2)
left3 = np.array(left3)
left4 = np.array(left4)
left5 = np.array(left5)
top1 = np.array(top1)
top2 = np.array(top2)
top3 = np.array(top3)
top4 = np.array(top4)
top5 = np.array(top5)
height1 = np.array(height1)
height2 = np.array(height2)
height3 = np.array(height3)
height4 = np.array(height4)
height5 = np.array(height5)
width1 = np.array(width1)
width2 = np.array(width2)
width3 = np.array(width3)
width4 = np.array(width4)
width5 = np.array(width5)
#%%
#
reg_labels = [left1,left2,left3,left4,left5,
               height1,height2,height3,height4,height5,
               top1,top2,top3,top4,top5,
               width1,width2,width3,width4,width5]

















