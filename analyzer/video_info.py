import cv2
import os
from math import gcd

def video_infos(vid):
    cap=cv2.VideoCapture(vid)
    if not cap.isOpened():
        print("Error video cant be opened.")
        cap.release()
        return None
    # Video Properties
    file_name=os.path.splitext(os.path.basename(vid))[0]
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fram=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps=cap.get(cv2.CAP_PROP_FPS)
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

    codec = (
        chr(fourcc & 0xFF) +
        chr((fourcc >> 8) & 0xFF) +
        chr((fourcc >> 16) & 0xFF) +
        chr((fourcc >> 24) & 0xFF)
    )

    cap.release()
    g = gcd(width, height)
    aspect_ratio = f"{width // g}:{height // g}"
    # c_time=os.path.getctime(vid)
    # d_date=os.path.get
    if fps>0:
        total_duration=fram/fps
    else:
        total_duration=0
    return {
        "File_Name":file_name,
        'Height':height,
        'Width':width,
        'Resulution':f"{height}x{width}",
        'Codec':codec,
        "Aspect Ratio":aspect_ratio,
        'Frame':fram,
        "FPS":fps,
        'Total_Duration':total_duration

    }