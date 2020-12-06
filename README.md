# SpotifyRoll

Listening to a long playlist on spotify?
Want to play a new song without losing your position on the playlist?

Look no further, this script will roll over your songs so you can continue later on where you left off.

Example:

Given a playlist with songs entitled 1,2,3,4,5,6,7
By rolling over to song 7, the playlist will now have the order of 5,6,7,1,2,3,4 as shown here:

<img src="https://raw.githubusercontent.com/Joseph-33/SpotifyRoll/master/Boxes.png" width="400">




# Getting Started
- Edit the config.yaml file with a text editor and fill in the required values
- Run Main.py using python3
- Once Main.py is run, a browser should open, follow the instructions in the console

# Prequisites
- An internet connection
- Spotify Premium
- Python 3.x
  - [Spotipy](https://pypi.org/project/spotipy/)
  - [html2text](https://pypi.org/project/html2text/)
  - [Yaml](https://pypi.org/project/PyYAML/)

# How to obtain a client and secret id
1. [Create a new app in spotify dashboard](https://developer.spotify.com/dashboard/applications)
2. Locate your apps client id and secret
3. Set your app redirect uri to `http://127.0.0.1`

More help [here](https://developer.spotify.com/documentation/general/guides/authorization-guide/) and [here](https://spotipy.readthedocs.io/en/2.12.0/#authorization-code-flow)

# Installing
Use git clone to download repository
`
git clone
`

# Running
Open a command prompt in the repository folder and run
`
python Main.py
`
Now input the name of the song and artist you would like to move to the top.



# Authors
- Joseph Andrews


