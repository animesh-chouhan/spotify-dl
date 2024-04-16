def get_user_playlists(sp):
    playlists = []
    results = sp.current_user_playlists(limit=50)
    while results:
        for i, playlist in enumerate(results["items"]):
            playlists.append(
                {
                    "id": playlist["id"],
                    "name": playlist["name"],
                    "url": playlist["external_urls"]["spotify"],
                }
            )
        if results["next"]:
            results = sp.next(results)
    print(f"Playlists found: {len(playlists)}")
    return playlists


def get_playlist_tracks(sp, playlist_id):
    tracks = []
    results = sp.playlist_tracks(
        playlist_id,
        fields="next,items(track(album(images,name),duration_ms,external_urls(spotify),id,name,preview_url,uri,artists))",
        limit=50,
    )
    while results:
        for i, item in enumerate(results["items"]):
            track = item["track"]
            tracks.append(
                {
                    "id": track["id"],
                    "uri": track["uri"],
                    "track_url": track["external_urls"]["spotify"],
                    "duration": track["duration_ms"],
                    "preview_url": track["preview_url"],
                    "name": track["name"],
                    "image_url": track["album"]["images"][0]["url"],
                    "album": track["album"]["name"],
                    "artist": ", ".join([item["name"] for item in track["artists"]]),
                }
            )
        if results["next"]:
            results = sp.next(results)
        else:
            results = None
    print(f"Tracks found: {len(tracks)}")
    return tracks
