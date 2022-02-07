
# 2048

A clone based on the classic [2048](https://en.wikipedia.org/wiki/2048_(video_game)). I tried to keep the color scheme as close as possible to the original masterpiece.
## Objective
The objective is simple:- try to make a tile of '2048' by merging smaller tiles.
The game will start with two tiles each numbered '2'. You can move UP, RIGHT, DOWN, or LEFT. On each move all the tiles will move to 
the direction of the key pressed as much as free space allows it to. Alse two tiles of same value will merge during this process if the comes in each other's path.

Also after this shifting is done if there is some free space avaibale on board, one of these free spaces will be filled with a block of value '2' or '4' randomly to allow the game to continue.

![Layout](https://github.com/adityaray115/2048-clone/blob/main/Layout.png?raw=true)
## Deployment

To deploy this project run

```bash
  $ python3 2048.py
```
