import os

def rename_subtitles(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)
    
    # Separate video and subtitle files
    video_files = [f for f in files if f.endswith(('.mp4', '.mkv', '.avi'))]
    subtitle_files = [f for f in files if f.endswith(('.ass','.srt'))]

    # Sort the lists to ensure matching order
    video_files.sort()
    subtitle_files.sort()

    # Check if the number of video files matches the number of subtitle files
    if len(video_files) != len(subtitle_files):
        print("The number of video files does not match the number of subtitle files.")
        return

    # Rename subtitle files to match the corresponding video file names
    for video, subtitle in zip(video_files, subtitle_files):
        video_name, _ = os.path.splitext(video)
        subtitle_ext = os.path.splitext(subtitle)[1]
        new_subtitle_name = video_name + subtitle_ext
        os.rename(os.path.join(directory, subtitle), os.path.join(directory, new_subtitle_name))
        print(f'Renamed "{subtitle}" to "{new_subtitle_name}"')

    print("Renaming completed.")

# Replace 'your_directory_path' with the path to your directory
rename_subtitles(r'C:\your_directory_path')
