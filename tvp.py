#!/usr/bin/python3
#---------------------tvp.py  v0.09   -------------------------- 
# Tesla Dashcam Video Player
# This code reads reads MP4 files from a Tesla thumb drive
# and plays the collection of front views of the 60 second clips continuously
# Press 'n' to jump to the next 60 second clip
# Press 'b' to jump back to the previous 60 second clip
# Press 'j' to jump forward 10 seconds in the current clip
# Press 'k' to jump back 10 seconds in the current clip
# Press 'p' to pause the video and 'p' to resume'
# Press 'q' to exit the script.
# 
# Created Tue 09 Jul 2024 02:54:22 PM  Teslacam Video Player initial upload   ver 0.08
# Updated Tue 09 Jul 2024 05:38:22 PM  added P to pause and K to jump back 10 sec v 0.09
#                                      changed directory path as a str var 'path'
# ----------------------------------------------------------------



import cv2
import os
import time

path  = '/media/juren/TeslaCam/TeslaCam/RecentClips/'

# Directory containing the video files
directory_path = path

# Get a list of all files in the directory
files = os.listdir(directory_path)

# Filter files to include only those that are MP4 and contain 'front' in the name
video_files = [file for file in files if file.endswith('.mp4') and 'front' in file]

# Sort the video files to ensure correct order
video_files.sort()

# Function to display video with properties
def play_video(video_path, video_file):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video {video_file}.")
        return False

    print(f"Playing video {video_file}...")

    start_time = time.time()
    paused = False

    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                break

        # Calculate elapsed time
        current_pos_msec = cap.get(cv2.CAP_PROP_POS_MSEC)
        elapsed_time = current_pos_msec / 1000.0
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        # Display properties on the video
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f'Playing: {video_file}'
        time_text = f'Time: {minutes:02d}:{seconds:02d}'
        cv2.putText(frame, text, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, time_text, (10, 70), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        cv2.imshow('Video', frame)

        key = cv2.waitKey(25)
        if key & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()
        elif key & 0xFF == ord('n'):
            cap.release()
            cv2.destroyAllWindows()
            return 'next'
        elif key & 0xFF == ord('p'):
            paused = not paused
        elif key & 0xFF == ord('k'):
            # Jump back 10 seconds
            new_time = current_pos_msec - 10000  # 10 seconds in milliseconds
            cap.set(cv2.CAP_PROP_POS_MSEC, max(new_time, 0))
        elif key & 0xFF == ord('j'):
            # Jump forward 10 seconds
            new_time = current_pos_msec + 10000  # 10 seconds in milliseconds
            cap.set(cv2.CAP_PROP_POS_MSEC, new_time)
        elif key & 0xFF == ord('b'):
            cap.release()
            cv2.destroyAllWindows()
            return 'previous'

    cap.release()
    cv2.destroyAllWindows()
    return 'next'

current_index = 0
while 0 <= current_index < len(video_files):
    video_file = video_files[current_index]
    video_path = os.path.join(directory_path, video_file)
    action = play_video(video_path, video_file)
    
    if action == 'next':
        current_index += 1
    elif action == 'previous':
        current_index -= 1

