from pytube import YouTube
import os

def download_video(url, output_path='./'):
    try:
        yt = YouTube(url)
        # Select the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading video: {yt.title}")
        stream.download(output_path)
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check the URL or your connection.")

# Example usage:
video_url = input("Enter the YouTube video URL: ")
# The video will be saved to the same directory as the script by default
download_video(video_url)