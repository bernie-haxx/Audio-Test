from pydub import AudioSegment
from pydub.playback import play


sound = AudioSegment.from_mp3('ciara.mp3')
play(sound)


if __name__ == '__main__':
	main()