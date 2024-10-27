from moviepy.editor import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('movie')
parser.add_argument('start')
parser.add_argument('finish')
parser.add_argument('new_movie')
args = parser.parse_args()
clip = VideoFileClip(args.movie)
clip = clip.subclip(args.start, args.finish)
clip.write_videofile(args.new_movie)