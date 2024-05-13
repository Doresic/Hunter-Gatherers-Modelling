import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.axes as axes


# Test the animation manually

fig, ax = plt.subplots()

def get_some_artists(ax: axes) -> list:
    """Get some random artists for the current state of the game."""
    artists_for_current_state = []

    # Random points
    for _ in range(10):
        artists_for_current_state.append(ax.scatter(random.random(), random.random(), color='red', marker='x'))
    
    return artists_for_current_state

all_state_artists = []
for _ in range(10):
    all_state_artists.append(get_some_artists(ax))

ani = animation.ArtistAnimation(fig, all_state_artists, interval=200, blit=True, repeat_delay=1000)
plt.show()
