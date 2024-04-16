# spotify-dl

Download your Spotify playlists and songs

## Usage(Linux)

You need Spotify Premium with client application installed for this to work. You would also need a Spotify Developer account and client credentials.

Edit `playlist_id` and `output_dir` in main.py. Also, rename the output template folder to match. Also select the output stream to record using `pavucontrol`.

```sh
pip3 install requests pyaudio spotipy pydub xdotool
python3 spotify-dl/main.py
```
