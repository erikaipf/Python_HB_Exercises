import winsound
import random

# Function to play the sound
def play_sound(p_sound_number, p_time):
	# The frequency of the sound is 37 thru 32767
	# Print the sound number (comma prints the sound in the same line)
	print p_sound_number,

	# Verify the number of the sound to play
	if p_sound_number == 1:
		# Play the sound
		winsound.Beep(390, p_time)
	elif p_sound_number == 2:
		# Play the sound
		winsound.Beep(440, p_time)
	elif p_sound_number == 3:
		# Play the sound
		winsound.Beep(500, p_time)
	elif p_sound_number == 4:
		# Play the sound
		winsound.Beep(600, p_time)

def main():
	
	# Loop to test the random sounds
	# for i in range(10):
	# 	sound_number = random.randint(1, 4)
	# 	play_sound(sound_number, 1000)

	# Print a new line
	# print ""
	# play_sound(3, 1300)
	# play_sound(1, 1300)
	# play_sound(4, 1300)
	# print ""
	# play_sound(3, 1000)
	# play_sound(1, 1000)
	# play_sound(4, 1000)
	# print ""
	# play_sound(3, 700)
	# play_sound(1, 700)
	# play_sound(4, 700)

	print ""
	play_sound(3, 300)
	play_sound(1, 300)
	play_sound(4, 300)
	play_sound(3, 300)
	play_sound(1, 300)
	play_sound(4, 300)

if __name__ == '__main__':
	main()