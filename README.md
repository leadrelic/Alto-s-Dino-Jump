# Alto's Dino Jump

## Overview
**Alto's Dino Jump** is a retro-style, side-scrolling game built with **Pygame**. Inspired by the classic offline Dino game, it introduces new twists with various power-ups, dynamic gameplay, and engaging visual effects. Players control a dinosaur that jumps, collects XP, and avoids obstacles while leveling up to gain new abilities.

## Features
- **Power-Ups & Abilities**: 
  - **Fireball Attack**: Shoot fireballs to destroy obstacles.
  - **Speed Boost**: Increases game speed temporarily for fast-paced action.
  - **Double Jump**: Allows an extra jump while in mid-air.
  - **Shield**: Provides protection against a single obstacle collision.
  - **Glide**: Slows down descent when falling, offering greater control.
  - **Extra Life**: Gives a second chance after a game-over.

- **Leveling System**: Gain XP by collecting items, defeat obstacles using power-ups, and choose from three random upgrades upon leveling up. Each level increases the XP needed for the next level.

- **Dynamic Background**: Enjoy parallax scrolling effects with layers, creating a sense of depth with moving ground, clouds, and distant elements.

- **Visual Feedback**: Particle effects enhance the visual experience during events like leveling up, using a shield, or launching fireballs.

- **Pause Menu**: Pause the game anytime with `P`, view controls, and restart or quit if needed.

## Gameplay
- **Controls**:
  - `SPACE`: Jump (double jump if unlocked).
  - `F`: Fire a fireball (if unlocked).
  - `G`: Glide while falling (if unlocked).
  - `P`: Pause/Resume the game.
  - `R`: Restart the game upon Game Over.
  - `Q`: Quit the game from the pause menu.

- **Power-Up Effects**:
  - **Fireball**: Shoots fireballs to destroy obstacles. Has a limited duration, displayed by a timer.
  - **Shield**: Absorbs one collision with an obstacle, after which it deactivates.
  - **Glide**: Activated by holding `G` during a fall, reducing fall speed for a controlled descent.
  - **Speed Boost**: Temporarily increases the speed of the game, making it more challenging.
  - **Extra Life**: Allows the player to avoid a game-over once and continue playing.

## Setup
### Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **Pygame**: Install Pygame using pip:
  ```bash
  pip install pygame
  ```

### Running the Game
1. Clone this repository or download the `Alto's Dino Jump` code file.
2. Ensure you have the `dinoo.png` image for the dinosaur character in the same directory as the game code.
3. Run the game script:
   ```bash
   python dino_jump.py
   ```

## Code Overview
This game leverages Pygame to create a simple, yet engaging side-scrolling experience with various power-ups and a leveling system to enhance replayability.
