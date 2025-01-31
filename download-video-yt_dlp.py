import yt_dlp
#from yt_dlp import Pla
import os

def download_best_video(url, id_video, id_audio):       
    # Membuat folder jika belum ada
  #  if not os.path.exists():
   #     os.makedirs()

    ydl_opts = {
#        'format': 'bestvideo+bestaudio/best',  # Mengambil kombinasi video dan audio dengan kualitas terbaik
        'format': id_video+'+'+id_audio+'/best',  # Mengambil kombinasi video dan audio dengan kualitas terbaik
        'outtmpl': f'%(title)s.%(ext)s',  # Format nama file output
        'merge_output_format': 'mp4',  # Gabungkan video dan audio ke dalam format mp4
    }


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"[DONE] %(title)s berhasil didownload.")

if __name__ == "__main__":
    video_url = input("Masukkan URL video YouTube: ")
    id_video = input("Masukkan id kualitas video (default = bestquality) : ") or 'bestvideo'
    id_audio = input("Masukkan id kualitas audio (default = bestquality) : ") or 'bestaudio'
    download_best_video(video_url, id_video, id_audio)
