import os
from moviepy.editor import VideoFileClip
import yt_dlp

def download_tiktok_video(url, output_dir='output/mp4'):
    os.makedirs(output_dir, exist_ok=True)
    video_id = url.split('/')[-1]
    output_file = os.path.join(output_dir, f'{video_id}.mp4')
    
    ydl_opts = {
        'outtmpl': output_file,  # Output file name with directory
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded: {url} -> {output_file}")
        return output_file
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

def convert_mp4_to_mp3(mp4_file, output_dir='output/mp3'):
    os.makedirs(output_dir, exist_ok=True)
    mp3_file = os.path.join(output_dir, os.path.splitext(os.path.basename(mp4_file))[0] + '.mp3')
    
    try:
        video_clip = VideoFileClip(mp4_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()
        video_clip.close()
        print(f"Converted: {mp4_file} -> {mp3_file}")
    except Exception as e:
        print(f"Failed to convert {mp4_file}: {e}")

def read_links_from_file(file_path):
    with open(file_path, 'r') as file:
        links = [line.strip() for line in file if line.strip()]
    return links

def process_videos_from_file(input_file):
    links = read_links_from_file(input_file)
    for link in links:
        mp4_file = download_tiktok_video(link)
        if mp4_file:
            convert_mp4_to_mp3(mp4_file)

# Example usage
if __name__ == "__main__":
    input_file = 'src/input.txt'
    process_videos_from_file(input_file)
