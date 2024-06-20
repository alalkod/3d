import Engine

SCREEN_SIZE = (1400, 800)
CAPTION = "3D"
BACKGROUND_COLOR = "black"
FPS = 30
FOV = 90

if __name__ == "__main__":
    engine = Engine.Engine(SCREEN_SIZE, CAPTION, BACKGROUND_COLOR, FPS, FOV)
    engine.start()