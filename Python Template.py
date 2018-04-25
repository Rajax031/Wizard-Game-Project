# Pygame template (Skeleton for New Game)


# initialize pygame and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

#Game loop
running = True
while running:
    # keep loop running at right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
    # Update
    
    # Draw / render
    screen.fill(BLACK)
    # after drawing everything, Flip the display
    pg.display.flip()

pg.quit()
        
