import os
from tinytag import TinyTag
url = os.path.join(os.getcwd(), 'songs/Ai Uta.mp4')
path = os.path.join(os.getcwd(), 'song')

import pygame
import sys
from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import Qt

def main():
    app = QApplication(sys.argv)

    song = os.path.join(os.getcwd(),"Ai Uta.mp4")
    print(song)
    # Initialize Pygame
    pygame.init()

    # Load the audio file
    pygame.mixer.music.load(song)

    # Get the total duration of the audio file
    total_duration = pygame.mixer.Sound(song).get_length()

    # Start playing the audio file
    pygame.mixer.music.play()

    # Create a horizontal slider
    slider = QSlider(Qt.Horizontal)
    slider.setRange(0, 100)  # Assuming the slider range is from 0 to 100

    # Monitor playback and update slider
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        # Calculate the elapsed time
        elapsed_time = pygame.mixer.music.get_pos() / 1000  # Convert milliseconds to seconds

        # Calculate the progress as a percentage
        progress_percent = (elapsed_time / total_duration) * 100

        # Update the slider's value
        slider.setValue(progress_percent)

        # Allow Pygame to process events
        pygame.event.pump()

        # Cap the frame rate to avoid excessive CPU usage
        clock.tick(30)  # Limit to 30 frames per second

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
