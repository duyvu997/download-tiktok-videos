# TikTok Video Downloader and Converter

This project allows you to download TikTok videos and convert them to MP3 format. It reads TikTok video links from a file, downloads each video, and converts the video files to audio files.

## Purpose

The primary purpose of this project is to download TikTok videos and convert them to MP3 format for offline listening or other uses.

## Setup

### 1. Create a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
```
### 2. Activate the Virtual Environment

- **Linux/MacOS:**
```
source venv/bin/activate
```

- **Windows:**
```
.\venv\Scripts\activate
```

### 3. Install Dependencies  

Install the required Python packages:
```
pip install -r requirements.txt
```

## Input or Modify Input

### 1. Create input.txt
Create a file named input.txt in the root directory of the project. Add the TikTok video links, one per line:

```
https://www.tiktok.com/@speakenglishwithtiffani5/video/7406629157943266603
https://www.tiktok.com/@anotheruser/video/1234567890123456789
# Add more links here
```

### 2. Modify input.txt
To modify the list of TikTok videos, simply update input.txt with the new links. Each link should be on a new line.


## Running the Script

### 1. Process Videos from input.txt
Run the script to download and convert the videos:

```
python src/process_videos.py
```

This will:

- Read TikTok video links from input.txt.
- Download each video to the output/mp4/ directory.
- Convert each downloaded video to an MP3 file in the output/mp3/ directory.

## Project Structure
```
my_python_project/
├── venv/                       # Virtual environment directory
├── src/                        # Source code directory
│   ├── __init__.py             # Empty file to mark the directory as a package
│   ├── download_video.py       # Script to download TikTok videos
│   ├── convert_mp4_to_mp3.py   # Script to convert MP4 to MP3
│   └── process_videos.py       # Script to process videos from input file
├── output/                     # Output folder for media files
│   ├── mp4/                    # Folder for MP4 files
│   └── mp3/                    # Folder for MP3 files
├── requirements.txt            # File listing installed dependencies
├── .gitignore                  # File specifying which files to ignore in version control
├── input.txt                   # File listing TikTok video links
└── README.md                   # Project description and usage instructions
```

## Troubleshooting

- Ensure you have the necessary permissions to write to the output directory.
- Verify that the links in input.txt are valid and correctly formatted.
- If you encounter any issues with the dependencies, ensure they are installed correctly in your virtual environment.