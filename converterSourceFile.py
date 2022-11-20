import sys
import time
import youtube_dl
import ctypes; kernel32 = ctypes.WinDLL('kernel32'); hStdOut = kernel32.GetStdHandle(-11); mode = ctypes.c_ulong(); kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode)); mode.value |= 4; kernel32.SetConsoleMode(hStdOut, mode)

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

#startvalues
userInput = "Y"

#startup-screen
print()
print(bcolors.FAIL + "Youtube to MP3 Converter" + bcolors.RESET)
print()
print(bcolors.WARNING + "Info:" + bcolors.RESET)
print()
print("MP3-Output is always set to high Quality")
print("MP3-File will be saved to the same directory")
print()


# Main-Cycle
while userInput.upper() == "Y":

    #URL Input
    video_url = input("Please enter YouTube-Video URL: ")

    #checks if URL is empty
    if video_url == "":
        break
    
    #checks for protocol
    #if missing, adds https
    completeness_checker = video_url.find("https://")

    if completeness_checker == -1:

        listed_url = list(video_url)

        listed_url.insert(0, "https://")

        video_url = "".join(listed_url)


    try:

        #Fetching Youtube Information
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = video_url,download=False
        )

        #Setting Configuration
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }
        #Download through YT-API
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        

    #Error Handler
    except:

        print()
        print(bcolors.FAIL + "Something went wrong :(" + bcolors.RESET)
        print(bcolors.FAIL + "Try again!" + bcolors.RESET)
        print()
        continue
    
    #Download Conformation
    print(bcolors.OK + "Download complete... {}".format(filename) + bcolors.RESET)
    print()
    print("Do you want to download another file?")
    print("(If yes, type: y | else, press Enter)")
    userInput = input()

#goodbye screen & program exit
print()
print("Goodbye :(")
time.sleep(2)
sys.exit()