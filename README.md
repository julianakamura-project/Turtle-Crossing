# 🐢 Turtle Road Crossing — Python OOP Project

A simple **road-crossing game** developed in Python using the `turtle` module as part of my studies in **Object-Oriented Programming (OOP)**.

The project is designed as a practical exercise to apply OOP concepts while building a small interactive game.

---

## 🎯 About the Project

The goal of this project is to create a game in which the player controls a turtle and attempts to cross a road while avoiding moving vehicles.

The project is being developed as part of my Python and OOP studies, with an emphasis on organizing the game into separate classes and objects with clearly defined responsibilities.

As the project develops, additional features and improvements may be added.

---

## 🎮 Gameplay

The player controls a turtle positioned at the bottom of the screen.

The objective is to:

1. Move the turtle forward.
2. Avoid the vehicles traveling across the road.
3. Reach the other side of the screen.
4. Progress to the next level.
5. Survive as long as possible.

As the level increases, the traffic becomes faster, making the game progressively more difficult.

---

## 🧠 OOP Concepts Practiced

This project provides an opportunity to practice:

- Classes and Objects
- Constructors (`__init__`)
- Instance Attributes
- Instance Methods
- Encapsulation
- Object Interaction
- Inheritance
- Code Organization
- Modular Programming
- Managing Object State
- Collision Detection

The project will also help me understand how multiple independent objects can interact within the same game.

---

## 🏗️ Planned Classes

The game will be divided into several classes, each responsible for a specific part of the application.

### 🐢 Player

Responsible for:

- Creating the turtle
- Controlling player movement
- Moving the turtle forward
- Detecting when the player reaches the finish line
- Resetting the player's position

### 🚗 Car

Responsible for:

- Creating vehicles
- Moving vehicles across the screen
- Generating vehicles at different positions
- Increasing vehicle speed as the level increases

### 🧮 Scoreboard

Responsible for:

- Displaying the current level
- Updating the level after successfully crossing the road
- Displaying game-over information

### 🎮 Game

The main game logic will coordinate the different objects and handle:

- Game state
- Collision detection
- Level progression
- Game-over conditions

The final class structure may change as the project develops.

---

## 🗂️ Project Structure

The project is expected to follow a structure similar to:

```text
Turtle-Road-Crossing/
│
├── main.py
├── player.py
├── car_manager.py
├── scoreboard.py
│
└── README.md