import os
import eyed3
from datetime import datetime

# Path to the directory containing your MP3 files
directory_path = os.getcwd()

# Recursively traverse all subdirectories
for root, _, files in os.walk(directory_path):
    for filename in files:
        if filename.endswith(".mp3"):
            full_path = os.path.join(root, filename)
            original_modified_time = os.path.getmtime(full_path)  # Read the original "modified" timestamp
            
            audio = eyed3.load(full_path)
            
            # Check if album name is empty and album art might be present
            if not audio.tag.album and audio.tag.images:
                artist = audio.tag.artist if audio.tag.artist else 'Unknown Artist'
                title = audio.tag.title if audio.tag.title else 'Unknown Title'
                artist_str = ", ".join(artist) if isinstance(artist, list) else artist
                title_str = ", ".join(title) if isinstance(title, list) else title
                album_name = f"{artist_str} - {title_str}"
                audio.tag.album = album_name
                audio.tag.save()
                print(f"Updated album name for {filename}: {album_name}")
                
                # Reapply the original "modified" timestamp
                os.utime(full_path, (original_modified_time, original_modified_time))
                original_time_readable = datetime.fromtimestamp(original_modified_time).strftime('%Y-%m-%d %H:%M:%S')
                print(f"Reapplied modified timestamp for {filename}: {original_time_readable}")
