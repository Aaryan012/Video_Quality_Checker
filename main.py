from utils.file_path import folder_path
from analyzer.brightness import brightness
from analyzer.contrast import contrast
from analyzer.video_info import video_infos
from analyzer.sharpness_motionblur import sharpness_and_motion_blur
import pandas as pd
import numpy as np
import os

def analyze_video(vid):
    result={}
    result.update(
      video_infos(vid)  
    )
    result.update(
        sharpness_and_motion_blur(vid)
    )
    result.update(
        brightness(vid)
    )
    result.update(
        contrast(vid)
    )
    return result

def main ():
    input_folder=r"C:\Users\rnkha\OneDrive\Desktop\Egocentric_pilot\pilot_videos\large_gray_tshirt"
    videos = folder_path(input_folder)
    results=[]
    for vid in videos:
        result=analyze_video(vid)
        results.append(result)
    results = pd.DataFrame(results)
    output_file = "Analysis.xlsx"
    if os.path.exists(output_file):
        # Append to existing Excel file
        with pd.ExcelWriter(
            output_file,
            mode="a",
            engine="openpyxl",
            if_sheet_exists="overlay"
        ) as writer:

            # Find existing rows
            start_row = writer.book.active.max_row

            results.to_excel(
                writer,
                index=False,
                header=False,
                startrow=start_row
            )

    else:
        # Create a new Excel file
        results.to_excel(output_file, index=False)
if __name__=="__main__":
    main()

