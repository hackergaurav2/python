import requests
import bs4

SEARCH_URL = "https://search.azlyrics.com/search.php?q="


def searchSong(songName):
    res = requests.get(SEARCH_URL+songName)
    html = bs4.BeautifulSoup(res.text, "html.parser")
    songs = html.select('.text-left a')
    songList = []

    for song in songs:
        songDict = {}
        songDict['name'] = song.text
        songDict['link'] = song.get('href')
        songList.append(songDict)
    
    return songList


def getLyrics(link):
    res = requests.get(link)
    html = bs4.BeautifulSoup(res.text, "html.parser")
    lyrics = html.select('.col-xs-12.col-lg-8.text-center div')

    for lyric in lyrics:
        if len(lyric.text) > 50:
            return (lyric.text)


if __name__ == "__main__":
    songName = input("Enter song name: ")
    songList = searchSong(songName)
    
    print("Select a song: ")
    listNo = 0
    for song in songList:
        listNo += 1
        print(str(listNo) +  ". " + song["name"])
    
    option = int(input("Select a song: "))

    link = songList[option-1]['link']

    lyrics = getLyrics(link)

    print(lyrics)

