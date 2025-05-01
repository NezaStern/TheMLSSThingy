# The MLSSS thingy 
## aka Music Lyrics Sheet Stuff thingy 
###### (for podpadc zaklucni projekt)

#### Project description
Nek program ki ima več različnih funkcij za predvajanje glasbe, prenašanje glasbe (mp3), prenašanje besedil komadov...
Fokus je na piano sheet music primarly

### Features (probablly maybe perhaps mayhaps)
- Music player (pygame.mixer)
- Music mp3 scraper (w spotDL)
- Lyrics scraper (GENIUS api ?)
- Sheet music scraper (musescore ?)
- Sheet music player? (decode musescore web thingy)
- Sheet music notating (adding note names/letters below notes...)
- Seperate tracks player (for music scores with more tracks/voices/instruments)? (maybe)
- 
- Ce hocs predvajat songs from spotify ti connecta spotify in kaze lyrics for song na spotifyu?
- .
- .
- Iz shazema api? da dobis dorekt lyrics


## GUI
Tabs:
1. Listed music (basicly list /Music dir)
2. Player (displayed lyrics and playing bar with commands at the bottom)
3. Downloading music tab (input prompt for title/artist/link)
4. Shhetmusic display....

## TODOs:
- [x] setup lyrics api aka lyricsgenius lib for py lol
- [ ] importable mp3 files (pop up dialog files/folders)
- [ ] make music player play music
	- [ ] pop up window for importing songs
- [x] basic pygame window setup
- [x] adding lyrics to songs metadata?
- [x] downloading music (spotDL) setupp
	- [x] check if its a link or song title or playlist to donwload?
- [x] Reorginize "modules" 
	- [ ] song module bi mev vse o mski
		- [ ] downloading mp3
		- [ ] downlaoidng lyrics ce se ni lyricsa v METADATA
- [ ] hande mutagen ID3 when no ID3 header exists...
	- [ ] manualy adds tags for song title, artist, lyris....
- [x] read mp3 files and names from \Music za imena za komade
- [ ] addd reading spotDL replys (if download fails or is skipped... (read the prints from stdin from spotdl??))
................................................................................................................................................................................................................................................................................................................................................................................................................................................................
- [ ] ffmpeg za mixer ker mp3 je shit??
- [ ] dl-librescore for mscz tehn mscx
- [ ] cuz i cant get mscz files directly for now user will have to import them .. 

### TO DO LATER CUZ IM LOSING MY MIND:
- [ ] add importable files (drag drop too maybe?)
- [ ] TA FUCKING MUSESCORE THINGGG AČLSDFJKAČLSKDFJLČK

## DOINT RN
- GUI
 


## DONE
- adding lyrics to a custom metadata tagggggggg on mp3 files [lyrics] #### NEVER MIND IG SE SAM DODA KER spotDL ze downloada to????
- check if song already exists-dont download spotdl...
- get song path (find the song in dict somehow)
- - trying to make the "check if song already exists" thingy grr


#### APP tabs?
- audio player
- audio files list folder thingy (importable new songs/folders)

## ==Links==

- GENIUS api : https://docs.genius.com/#/getting-started-h1
- Mutagen py lib: https://mutagen.readthedocs.io/en/latest/user/index.html
- Pygame MIXER : https://www.pygame.org/docs/ref/music.html

Za Podpadca Zaključna naloga
