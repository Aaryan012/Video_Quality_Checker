import cv2
import numpy as np
from analyzer.video_info import video_infos
from numpy import random
# Calculating brightness / exposureof frames
def brightness(vid,sample_count=100,black_frame_threshold=5.0):
    video_result=video_infos(vid)
    fram=video_result['Frame']
    cap=cv2.VideoCapture(vid)
    brightness_score=[]
    black_frame_count=0
    print("Calculating Brightness of frame")
    sample_count = min(sample_count, fram)
    frame_numbers = np.random.choice(fram,size=sample_count,replace=False)
    for frame_num in frame_numbers:
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
        ret,frame =cap.read()
        if not ret:
            continue
        # Converting to Grayscale, grayscale are better for computations
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        bright=np.mean(gray_frame)
        if bright < black_frame_threshold:
            black_frame_count += 1
            continue
        brightness_score.append(bright)
    cap.release()
    if not brightness_score:
        return None
    return{
        "avg_brightness":np.mean(brightness_score),
        'min_brightness':np.min(brightness_score),
        'max_brightness':np.max(brightness_score),
        "Black_Frames": black_frame_count
    }   