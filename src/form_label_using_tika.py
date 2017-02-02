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

from extract_images import store_center_image
import os
import sys


if __name__ == '__main__':    
    if len(sys.argv) < 4:
        print "Usage - "
        print "\t python form_label_using_tika.py [v/i] <path/to/(video/image)/dir> <path/to/output/dir>"
        print "\t [v/i] -> v from video, i for images"
        print "<path/to/output/dir> should exist"
        print "\t New images from video will be named same as video name. As of now we generate only one image per video"
        print "\t Output is json with key as video/image name and value as labels"
        sys.exit()
    
    video_image_option = sys.argv[1]
    ip_dir_path = sys.argv[2]
    out_path = sys.argv[3]
    
    if "v" == video_image_option:
        '''
        First store center frame as image file
        ''' 
        for f in os.listdir(ip_dir_path):
            if not f[-3:] == "mp4":
                continue
        
            store_center_image(ip_dir_path+"/"+f, out_path)
        
        print "Stored images from videos"
        video_image_option = "i"
        ip_dir_path = out_path
        
    if "i" == video_image_option:
        '''
        Call tika to get image labels
        '''
        for f in os.listdir(ip_dir_path):
            print ip_dir_path+"/"+f
            
            
