import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ----------------------------------------------------------------------------------------------------------------------

year = input('From which year would ypu like to get the top 100? write in this format "YYYY" \n')
month = input('From which month? write in this format "MM" \n')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{year}-{month}-01/')
soup = BeautifulSoup(response.text, 'html.parser')
first_title = soup.find(name='h3',
                        id='title-of-a-story',
                        class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet'
                               ' lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max '
                               'a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only '
                               'u-letter-spacing-0028@tablet').getText().replace('\n', '')
titles = soup.find_all(name='h3',
                       id='title-of-a-story',
                       class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 '
                              'lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 '
                              'u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 '
                              'u-max-width-230@tablet-only')

top_100 = [names.getText().replace('\n', '') for names in titles]

top_100.insert(0, first_title)

# ----------------------------------------------------------------------------------------------------------------------

sp_id = '7ea5bc4609d74943b6be69c3261e26a2'
sp_secret_id = '98f4e9dcbde24e2cbf8945e720c90353'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri='http://example.com',
        client_id=sp_id,
        client_secret=sp_secret_id,
        show_dialog=True,
        cache_path='token.txt'
    )
)

user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user=user_id, name=f"the {year}'s hits", public=False)

song_uri = []
for song in top_100:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uri.append(uri)
    except IndexError:
        print(f"{song} not available")

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uri)
