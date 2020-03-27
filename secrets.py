import spotify_token as st


spotify_user_id = 'gzangerme'
data = st.start_session("gzangerme","Saymyname799$")
spotify_token = data[0]
expiration_date = data[1]
