# -*- coding: utf-8 -*-

from Game import *




def main(game=None):
    """game = Game()
    ip = input("Direccion ip del servidor: ")
    nick = input("nickname: ")
    choosed_pokemon = input("pokemon a usar: ")"""
    
    
    while not game.stopped:
        # Main pokemon battle loop
        # First ask for the commands
        game.process()
        game.render()


if __name__ == "__main__":
    main()
