import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(mp4_file, output_dir='output/mp3'):
    os.makedirs(output_dir, exist_ok=True)
    mp3_file = os.path.join(output_dir, os.path.splitext(os.path.basename(mp4_file))[0] + '.mp3')
    
    try:
        video_clip = VideoFileClip(mp4_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()
        video_clip.close()
        print(f"Conversion completed! MP3 saved as {mp3_file}")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

# Example usage
if __name__ == "__main__":
    mp4_file = 'output/mp4/tiktok_video.mp4'
    convert_mp4_to_mp3(mp4_file)
