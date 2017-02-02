#!/usr/bin/env python
# 
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cv2
import os
import sys
import ntpath

def path_leaf(path):
    '''
    Returns file name from path. Path should not end with slash(/)
    '''
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def store_center_image(video_path, image_dir="."):
    '''
    Traverse till half of video and saves center snapshot
    '''
    cap = cv2.VideoCapture(video_path)
    
    length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    
    success,image = cap.read()
    count = 0
    
    while(success and count < length/2):
        success,image = cap.read()
        count += 1 
    
    name = path_leaf(video_path)
    
    print image_dir+"/" + name[:-3]  + "jpg"
    
    print "Created Images- ", cv2.imwrite(image_dir+"/" + name[:-3]  + "jpg", image)
    


if __name__ == '__main__':    
    if len(sys.argv) < 3:
        print "Usage -"
        print "\t python extract_images.py <path/to/video/dir> <path/to/output/dir>"
        print "<path/to/output/dir> should exist"
        print "New images will be named as video name. As of now we generate only one image per video"
        sys.exit()
    
    video_dir_path = sys.argv[1]
    out_path = sys.argv[2]
    
    for f in os.listdir(video_dir_path):
        if not f[-3:] == "mp4":
            continue
    
        store_center_image(video_dir_path+"/"+f, out_path)
        
    print "Stored images from videos"
    
    


