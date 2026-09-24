import cv2
import numpy as np
from analyzer.video_info import video_infos
from numpy import random
def sharpness_and_motion_blur(vid, sample_count=100, blur_threshold=20, anisotropy_threshold=2.5):
    video_result = video_infos(vid)
    fram = video_result['Frame']

    print("Calculating Sharpness and Motion Blur")
    sharpness_scores = []
    anisotropy_scores = []

    cap = cv2.VideoCapture(vid)
    sample_count = min(sample_count, fram)
    frame_numbers = np.random.choice(fram,size=sample_count,replace=False)
    for frame_num in frame_numbers:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()
        if not ret:
            continue

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # General sharpness
        sharp = cv2.Laplacian(gray_frame, cv2.CV_64F).var()
        sharpness_scores.append(sharp)

        # Directional gradients for motion blur signature
        sobel_x = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(gray_frame, cv2.CV_64F, 0, 1, ksize=3)
        grad_x_var = sobel_x.var()
        grad_y_var = sobel_y.var()

        epsilon = 1e-6
        if grad_x_var < 1.0 and grad_y_var < 1.0:
            anisotropy = 1.0  # flat/black frame — no directional signature, treat as neutral
        else:
            anisotropy = max(grad_x_var, grad_y_var) / (min(grad_x_var, grad_y_var) + epsilon)

        anisotropy_scores.append(anisotropy)

    cap.release()

    if not sharpness_scores:
        return None

    blurry_frames = sum(score < blur_threshold for score in sharpness_scores)
    blur_percentage = (blurry_frames / len(sharpness_scores)) * 100

    # Motion-blur-suspect frames: low sharpness AND high directional anisotropy
    motion_blur_frames = sum(
        (s < blur_threshold and a > anisotropy_threshold)
        for s, a in zip(sharpness_scores, anisotropy_scores)
    )
    motion_blur_percentage = (motion_blur_frames / len(sharpness_scores)) * 100

    return {
        "avg_sharpness": np.mean(sharpness_scores),
        "min_sharpness": np.min(sharpness_scores),
        "Blurry_Frames": blurry_frames,
        "Blur_Percentage": blur_percentage,
        "avg_anisotropy": np.mean(anisotropy_scores),
        "Motion_Blur_Frames": motion_blur_frames,
        "Motion_Blur_Percentage": motion_blur_percentage
    }