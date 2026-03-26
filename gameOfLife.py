import sys


#################################################################################
######   Function to read in the file
######   
######   Each line in the file contains W characters and L lines. This defines
######   the starting generation of a W wide by L long work.
######   An X represents a living cell and a . is not.    
#################################################################################
def read_initial_file_and_extract_gen1(filename:str):
    pass

#################################################################################
######   Function to print the current world
######   
#################################################################################
def print_generation(world):
    pass

#################################################################################
######   Function to calculate the next generation based on the rules:
######   https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for the rules
#################################################################################
def calculate_next_generation(world):
    pass

#################################################################################
######   Function to calculate the number of living cells
######   
#################################################################################
def calculate_living_cells(world):
    return 0

#################################################################################
###### Main function that runs
#################################################################################
def main(filename:str,maxGenerations: int):
    world = read_initial_file_and_extract_gen1( filename)

    #print the starting point
    print_generation(world)
    for i in range(maxGenerations):
        world=calculate_next_generation(world)
        numCells =  calculate_living_cells(world) 
        print(f"Generation {i} num cells {numCells}")
        print_generation(world)
        if numCells == 0:
            print(f"Game exited after {i} Generation")
            break




# Main, this is the entry point
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gameOfLife.py <filename> <max generations>")
        sys.exit(1)
    main(sys.argv[1],int(sys.argv[2]))