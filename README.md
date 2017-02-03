# video-recognition
This repo takes advantage of Tika and TensorFlow imagenet to understand a video file. It selects frame of video and saves it as image file. It then uses  Inception-V3 model from Tensorflow integrated with Tika to generate description of that image.

How to use?
1. `cd src`
2. `python form_label_using_tika.py`
```
Usage - 
	 python form_label_using_tika.py [v/i] <path/to/(video/image)/dir> <path/to/output/dir>
	 [v/i] -> v from video, i for images
	 <path/to/output/dir> should exist
	 New images from video will be named same as video name. As of now we generate only one image per video
	 Output is json with key as video/image name and value as labels
```

## Requirements
- OpenCV with python support
- Tika and Tensor flow running as per https://wiki.apache.org/tika/TikaAndVision#Step_1._Setup_REST_Server
