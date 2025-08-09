import webbrowser
import sys

def open_spotify_playlist(playlist_url):
    """
    Opens a Spotify playlist in the default web browser.

    Args:
        playlist_url (str): The URL of the Spotify playlist.
    """
    if not playlist_url:
        print("Error: No playlist URL provided.")
        return

    try:
        # Opens the URL in a new browser tab.
        # This will either open the Spotify web player or the desktop app,
        # depending on your browser's settings.
        webbrowser.open(playlist_url)
        print(f"Opening playlist: {playlist_url}")
    except webbrowser.Error as e:
        print(f"An error occurred: {e}")
        print("Please ensure you have a web browser installed.")
    
# --- Main part of the program ---
if __name__ == "__main__":
    # To get a playlist URL:
    # 1. Open Spotify and go to your playlist.
    # 2. Click the three dots (...) and choose "Share" -> "Copy Playlist Link".
    # 3. Paste the link below.
    
    # Replace this with the actual URL of your playlist.
    playlist_url = "https://open.spotify.com/playlist/08o3xVOgpzHhQ0UpwhUtIx?si=ec9124568ed342a3" # Example: My playlist
    
    open_spotify_playlist(playlist_url)

