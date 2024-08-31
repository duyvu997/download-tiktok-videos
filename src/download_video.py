import os
import yt_dlp

def download_tiktok_video(url, output_dir='output/mp4'):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'tiktok_video.mp4')
    
    ydl_opts = {
        'outtmpl': output_file,  # Output file name with directory
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed successfully! Video saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    tiktok_url = 'https://www.tiktok.com/@speakenglishwithtiffani5/video/7406629157943266603'
    download_tiktok_video(tiktok_url)
