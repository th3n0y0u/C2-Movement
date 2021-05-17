## Pygame
A set of Python modules designed for writing video games

### Coordinates in Pygame window 
- The top left corner of the screen is (0,0) and bottom right is (width, height)

- Positive x-direction is to the right and negative x-direction is to the left

- Positive y-direction is downwards and negative y-direction is upward

```
# 1. Import the Pygame library
import pygame  

# 2. Initialize the pygame
pygame.init()

# 3. Create a pygame window with size(Width, Height)

gameDisplay = pygame.display.set_mode((W,H))

# 4. Accepting key inputs from the user
pygame.key.get_pressed()

# 5. Setup delay time(## in ms, (1s = 1000s))
pygame.time.delay(##)

# 6. Update frames
pygame.display.update()

#7. Terminate the pygame at the end
pygame.quit()