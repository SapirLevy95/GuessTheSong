
Commands:

Activate Virtual Env : venv\Scripts\activate


The Game:
* The Developer enter 10 bands / singers that we like.
* The system needs to fetch related song's name from the Internet
    1. Search in YouTube
    2. Check Spotify API
* The system plays a song and the player should guess the name of the song.
    * max score=100, min_score = 50. max time 1 min. . for each second delay he gets less score. it should not be linear.
    * he need to enter the song name, do fuzzy matching (1 char different)
    * normalize the song name (= remove weird characters)