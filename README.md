# Spotify Search
<p>
    <a href="https://choosealicense.com/licenses/mit/" target="_blank">
        <img src="https://img.shields.io/github/license/matcsantos/SpotifySearch" alt="LICENSE">
    </a>
    <a href="https://pypi.org/project/spotifysearch/0.0.1/" target="_blank">
        <img src="https://img.shields.io/pypi/v/spotifysearch?color=33BBFF&label=PIP" alt="LICENSE">
    </a>
</p>

SpotifySearch is a complete wrapper for the Search API provided by Spotify written in Python.

It has built-in classes that helps you access the data returned by Spotify, alongside with useful methods for exporting data.

Check the [documentation](https://github.com/matcsantos/SpotifySearch/wiki) for more information on classes and methods.

## What you can do
- Get Spotify catalog information about albums, artists, tracks or episodes that match a keyword string.
- Easily access the information provided by Spotify using specific class attributes and methods, such as **name**, **id**, **url** and many more.
- Access and export audio and image files, such as album covers for example.

## Installation
SpotifySearch depends on **[requests](https://pypi.org/project/requests/)**. You can easily install it by using **PIP**
```bash
python -m pip install requests
```

With requests installed, you can safelly install Spotify Search with the following command
```bash
python -m pip install spotifysearch
```

## Basic usage
Here's an example of basic usage of Spotify Search
```python
from spotifysearch.client import Client

#Check the documentation to learn how to get your credentials.
myclient = Client('CLIENT_ID', 'CLIENT_SECRET')


search_results = client.search('Never gonna give you up')
track = search_results.get_first_track()

#Show some information about the track
print(track.name, '-', track.artist.name)
print('Duration:', track.formatted_duration)
print(track.url)
```

Result:
```bash
Never Gonna Give You Up - Rick Astley
https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT
Duration: 03:33
```

## Getting your credentials
Check [this section](https://github.com/matcsantos/SpotifySearch/wiki#-getting-started) of the documentation to learn how to get your client ID and secret.

## License
This project is under the terms of the [MIT license](https://opensource.org/licenses/MIT).
