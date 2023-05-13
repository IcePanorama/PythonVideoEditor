from moviepy.editor import VideoFileClip, concatenate_videoclips
from os import listdir, path, makedirs
import sys


def get_input_vids(dir : str) -> list:
    return listdir(input_dir)


if __name__ == "__main__":
    input_dir = "input/"
    video_files = []
    clips = []

    try:
        video_files = get_input_vids(input_dir)
    except:
        print("No videos to combine.\nPlease create a directory called " +
                input_dir + " and add your videos there.")
        sys.exit(-1)

    for video in video_files:
        clips.append(VideoFileClip(input_dir + video))

    # adding method='compose' should fix glitching when clips have varying
    # resolutions
    output = concatenate_videoclips(clips, method='compose')

    output.write_videofile("test.mp4"); # need file name

