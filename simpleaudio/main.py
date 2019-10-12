import simpleaudio as sa



filename = 'ciara.mp3'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()


if __name__ == '__main__':
	main()