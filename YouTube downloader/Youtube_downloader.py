from pytube import YouTube
import shutil as S

link = input("Enter YouTube link: ")
yt = YouTube(link)
pat=input("Enter the path you want to save:") 
print("Title:", yt.title)
print("Views:", yt.views)

# Choose the desired resolution for video download
resolution_choice = int(input("Select resolution for video download:\n1. Highest Resolution\n2. 720p\n3. 480p\n4. 360p\n5.Audio only\nEnter choice: "))

if resolution_choice == 1:
    video_stream = yt.streams.get_highest_resolution()
elif resolution_choice == 2:
    video_stream = yt.streams.get_by_resolution("720p")
elif resolution_choice == 3:
    video_stream = yt.streams.get_by_resolution("480p")
elif resolution_choice == 4:
    video_stream = yt.streams.get_by_resolution("360p")
elif resolution_choice == 5:
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download("/storage/emulated/0/Download")
    S.move(os.path.join(pat,yt.title+".mp4"),os.path.join(pat,yt.title+".mp3"))
    print("Audio Download Completed!")
    exit()
else:
    print("Invalid choice")
    exit()

video_stream.download(path)
	
print("Video Download Completed!")
