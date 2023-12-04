# mp3 Album Auto-Tagger
A simple python script which changes mp3 metadata so that the album tag is in the format "Artist - Title". This can be run on android using Termux and will solve improper album art in Samsung Music (and other players)

# How to use
1. Install Termux:  
If you don't have Termux installed already, you can download it from the Google Play Store.

2. Install Python and Required Libraries:
Open Termux and install Python by running the following command:  
```pkg install python```  
Then, install the mutagen library, which is used to work with audio file metadata:  
```pip install mutagen```  
Install the eyed3 library using pip in your Termux environment:  
```pip install eyed3```

3. Download the `script.py` to the folder which contains your mp3 library.
   
4. Navigate to the Storage Directory  
Example:  
```cd storage/shared/Music```

5. Run the Script:  
```python script.py```
