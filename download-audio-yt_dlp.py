import yt_dlp
import os

def download_best_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',  # Mengambil audio dengan kualitas terbaik
        'outtmpl': f'%(title)s.%(ext)s',  # Format nama file output
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',  # Ekstrak audio menggunakan FFmpeg
                'preferredcodec': 'mp3',  # Format output MP3
                'preferredquality': '320',  # Bitrate audio 320 kbps
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Masukkan URL video YouTube: ")
    download_best_audio(video_url)
