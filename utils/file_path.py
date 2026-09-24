import os
# video file path 
def folder_path(file_path):
    videos=os.listdir(file_path)
    video_path=[]
    for i in videos:
        video_path.append(os.path.join(file_path,i))
    return video_path