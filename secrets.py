import spotify_token as st

#Make Sure to input the right information for it to generate the Spotify Token

spotify_user_id = 'YOUR_USERNAME_ON_SPOTIFY'
data = st.start_session('YOUR_USERNAME_ON_SPOTIFY','YOUR_PASSWORD_ON_SPOTIFY')
spotify_token = data[0]
expiration_date = data[1]
