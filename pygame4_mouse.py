import pygame

# You must do this initialization before most pygame things will work
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Make an all black surface (black is default color: 0,0,0)
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

################################################################################

# Initialize mouse variables
mouse_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

################################################################################

# Create a surface from an image
logo_surface = pygame.image.load('logo.jpg')
logo_rect = logo_surface.get_rect()
logo_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Run the game loop
running = True
while running:

    # Cycle through all of the current events
    for event in pygame.event.get():

        # User clicked the X to close program
        if event.type == pygame.QUIT:
            running = False

        # Special one-time keys: SPACE -> 'Boom' and ESC -> Quit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Boom")
            if event.key == pygame.K_ESCAPE:
                running = False            

################################################################################

        # One of the most common mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                print(f"Left button clicked at {mouse_pos}")
            elif event.button == 3:
                print(f"Right button clicked")

################################################################################

    # Place surfaces on the screen but don't display them (order matters)
    # Internally this will use depth calculations to create the final image
    screen.blit(background, (0, 0))
    screen.blit(logo_surface, logo_rect)

    # Draw the current frame on the screen
    pygame.display.update()

# Close down everything
pygame.quit()