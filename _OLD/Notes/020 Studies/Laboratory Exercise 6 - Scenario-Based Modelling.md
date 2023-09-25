# # Control Alt Elite

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

![[Pasted image 20221115145124.png]]

<div style="page-break-after: always;"></div>


## 1. Character Customization

Formal Use Case
---
**Use Case**: Character Customization

**Actor**: Players

**Goal**: To customize a character preferred by players.

**Precondition**: To be able to customize the character, players should create a new character.

**Trigger**: New character has been created.

**Scenarios**:
-   Player creates a new character
-   Player gets sent to customization screen
-   Player customizes character

**Exception**: Unable to customize an existing character.  

User Story
---
**User Story**:
> As a player, I should be able to **view, select, and modify available designs** so that I can **freely customize my character accordingly** for **greater experience**.

**Acceptance Criteria:**    
- Interactable and functioning user interface for character customization
- Organize available options for character customization

<div style="page-break-after: always;"></div>

Use Case Diagram
---

![[image17.png]]

<div style="page-break-after: always;"></div>

Swimlane Diagram
---
![[Pasted image 20221115133122.png]]

<div style="page-break-after: always;"></div>

Flowchart Diagram
---
![[image3 1.png]]


---

## 2. Pause the game
Formal Use Case
---
**Use Case**: Pause the game

**Actor**: Players

**Goal**: To pause the game 

**Precondition**: To be able to pause the game, player should press the pause button

**Trigger**: Pause button is pressed

**Scenarios**:
-   Player plays the game
-   Player pauses the game
-   Pause menu screen pops up
-   Player can choose to do 3 things: unpause and continue playing, save the current progress, quit the game

**Exception**: Unable to pause the game if the player is currently not in game e.g. player is in the main menu

User Story
---
**User Story**:
>  As a player, I should be able to **pause the game** so that I can **temporarily stop playing, save my current progress, or quit the game**.

**Acceptance Criteria:**    
- Pause the game through a button or pause icon, or by using a shortcut key
- Display the pause menu user interface

<div style="page-break-after: always;"></div>

Use Case Diagram
---
![[image11.png]]

Swimlane Diagram
---
![[Pasted image 20221115120828.png]]

Flowchart Diagram
---
![[image5.png]]

---


## 3. Save current progress
Formal Use Case
---
**Use Case**: Save current progress

**Actor**: Players

**Goal**: To save current progress 

**Precondition**: To be able to save current progress, game must be paused

**Trigger**: Save button is pressed

**Scenarios**:
-   Player jumps from platform to platform
-   Player pauses the game
-   Player saves the current progress by pressing the save button
  
**Exception**: The player has not landed on an environment platform (e.g. falling or jumping)

User Story
---
**User Story**:
> As a player, I should be able to **save my progress** so that I can **play the game anytime I want without having to play from the beginning again** for **me to avoid repetition**.

**Acceptance Criteria:**    
- Save the progress through a button or save icon

<div style="page-break-after: always;"></div>

Use Case Diagram
---

![[image5 1.png]]

<div style="page-break-after: always;"></div>

Swimlane Diagram
---
![[Pasted image 20221115120609.png]]

Flowchart Diagram
---
![[image8 1.png]]

<div style="page-break-after: always;"></div>

---

## 4.  Load Saved Progress
Formal Use Case
---
**Use Case**: Load a saved progress

**Actor**: Players

**Goal**: To go back to a previous saved point in the game 

**Precondition**: To be able to load a saved point, the player should have a saved instance

**Trigger**: Press the load button in the main menu

**Scenarios**:
-   Player selects load to a saved checkpoint in main menu
-   Player is sent to that saved point in the game
-   Player plays the game with the same position from the saved point

**Exception**: Unable to load an instance if none has been created before..

User Story
---
**User Story:**
> As a player, I should be able to **load my previous progress** so that **I can continue playing the game from where I left off**.

**Acceptance Criteria:**    
- Continue playing the selected saved progress

<div style="page-break-after: always;"></div>

Use Case Diagram
---
![[image9.png]]


Swimlane Diagram
---
![[image2.png]]

<div style="page-break-after: always;"></div>

Flowchart Diagram
---
![[image12.png]]

---

## 5. Power-ups
Formal Use Case
---
**Use Case**: Use power-ups to gain an advantage e.g. speed boost, increased jump height, +1 jump, etc.

**Actor**: Players

**Goal**: To gain an advantage over certain situations.

**Precondition**: To be able to activate power-ups, players must first pick up these power-ups scattered throughout the map.

**Trigger**: Picked up power-ups

**Scenarios**:
Through power-ups, players receive a:
-   Speed boost
-   Jump boost
-   Double jump

**Exception**: Players can’t activate power-ups without picking them up.

User Story
---
**User Story:**
> As a player, I should be able to **use power-ups** so that **to overcome certain situations in the game which would otherwise be difficult to pass**.

**Acceptance Criteria:**    
- Allow the player to pick up and use these power-ups
- Speed boost increases player movement speed
- Jump boost increases player jump height
- Double jump allows the player to jump a second time whilst still in mid air 

<div style="page-break-after: always;"></div>

Use Case Diagram
---
![[3.png]]

Swimlane Diagram
---
![[image6.png]]

Flowchart Diagram
---
![[image11 1.png]]

---


## 6. Game Controls
Formal Use Case
---
**Use Case**: Use movement keys like WASD to move the player, Spacebar for jump, and the F key for interacting with NPCs.

**Actor**: Players

**Goal**: To be able to control the player’s movement and interaction.

**Precondition**: Players should use the designated keybinds for the respective movement and interaction.

**Trigger**: WASD, Spacebar, and F for movement, jumping, and interaction.

**Scenarios**:
- Players can press the WASD keys to move up, left, down, and right respectively.
- Players can press the Spacebar to jump.
+ When near an NPC, players can press the F key to interact with them.

**Exception**: Players can’t do anything else aside from the respective keybinds.

User Story
---
**User Story:**
> As a player, I should be able to **interact my character in the game environment** so that **I can perform certain actions like player movement, interactions, and commands**.

**Acceptance Criteria:**    
- Press certain keyboard keys to move or interact

<div style="page-break-after: always;"></div>

Use Case Diagram
---
![[image4.png]]

Swimlane Diagram
---
![[image10.png]]

<div style="page-break-after: always;"></div>

Flowchart Diagram
---
![[Pasted image 20221115125401.png]]