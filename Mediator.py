class Playlist(object):

 
    def displaySinger(self, singer, music):
        print("[{}'s music]: {}".format(singer, music))
 
 
class Singer(object):
   
 
    def __init__(self, name):
        self.name = name
        self.playlist = Playlist()
 
    def sendCourse(self, music):
        self.playlist.displaySinger(self, music)
 
    def __str__(self):
        return self.name
 

if __name__ == "__main__":
 
    mayank = Singer('Ed Sheeran')   # user object
    lakshya = Singer('Tyler the creator') # user object
    krishna = Singer('Scriptonite') # user object
 
    mayank.sendCourse("Bad Habits")
    lakshya.sendCourse("Are we still friends")
    krishna.sendCourse("2004")