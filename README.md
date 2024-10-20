
# Alto's Dino Jump

## Overview
**Alto's Dino Jump** is a retro-style, side-scrolling game built with **Pygame**. The game draws inspiration from the classic offline Dino game with a twist, offering various power-ups, dynamic gameplay, and multiple visual effects. Players control a dinosaur that jumps, collects XP, and avoids obstacles while leveling up and gaining new abilities.

## Features
- **Power-Ups & Abilities**: 
  - Fireball attack
  - Speed boost
  - Double Jump
  - Shield for protection
  - Glide to slow descent
  - Extra XP boost
  - Double XP collection
  - Extra Life
- **Leveling System**: Gain XP by collecting items, defeat obstacles using power-ups, and choose from three random upgrades upon leveling up.
- **Dynamic Background**: Parallax scrolling effects with layers, including ground pebbles, mountains, and clouds.
- **Visual Feedback**: Particle effects for various events like leveling up, using a shield, or launching fireballs.
- **Pause Menu**: Pause the game anytime with `P`, view controls, and restart if needed.

## Gameplay
- **Controls**:
  - `SPACE`: Jump (double jump if unlocked)
  - `F`: Fire a fireball (if unlocked)
  - `P`: Pause/Resume the game
  - `R`: Restart the game upon Game Over
  - `Q`: Quit the game from the pause menu

- **Power-Up Effects**:
  - **Fireball**: Shoot fireballs to destroy obstacles. A timer indicates the remaining duration of the ability.
  - **Shield**: Protects the dinosaur from one collision with an obstacle.
  - **Glide**: Slows down the descent speed, allowing more control when falling.
  - **Speed Boost**: Temporarily increases game speed for a short burst.
  - **Double XP**: Temporarily doubles the XP gained from collecting items.
  - **Extra Life**: Allows the player to continue after one game-over.

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
