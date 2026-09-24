import cv2
import numpy as np
from analyzer.video_info import video_infos
from numpy import random

def contrast(vid,sample_count=100):
    video_result=video_infos(vid)
    fram=video_result['Frame']
    cap=cv2.VideoCapture(vid)
    contrast_score=[]
    print("Calculating Contrast of frame")
    sample_count = min(sample_count, fram)
    frame_numbers = np.random.choice(fram,size=sample_count,replace=False)
    for frame_num in frame_numbers:
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
        ret,frame =cap.read()
        if not ret:
            continue
        # Converting to Grayscale, grayscale are better for computations
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        contrast=np.std(gray_frame)
        contrast_score.append(contrast)
    cap.release()
    if not contrast_score:
        return None
    return{     
        'avg_contrast':np.mean(contrast_score),
        'max_contrast':np.max(contrast_score),
        'min_contrast':np.min(contrast_score)
    }