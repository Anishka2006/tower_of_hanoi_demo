''' This program demonstrates the Tower of Hanoi problem using recursion. 
The function recursively moves n-1 disks between rods until it reaches the base case of a single disk. 
Each recursive call reduces the problem size, illustrating how recursion can simplify complex problems. 
A step counter is included to track the number of moves, and the output is formatted for clarity 
'''

import os
import time

#ANSI Colors
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]
RESET = "\033[0m"

step_count = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Display towers visually
def display_towers(towers, n, move_msg=""):
    clear()

    #Header
    print("=" * 50)
    print(f" Step {step_count}".center(50))
    print("=" * 50)

    #Move description
    if move_msg:
        print(f"\n {move_msg}\n")

    #Print towers
    for level in range(n - 1, -1, -1):
        for rod in ['A', 'B', 'C']:
            if len(towers[rod]) > level:
                disk = towers[rod][level]
                color = COLORS[(disk - 1) % len(COLORS)]
                disk_str = color + "*" * (disk * 2 - 1) + RESET
                print(" " * (n - disk) + disk_str + " " * (n - disk), end="   ")
            else:
                print(" " * (n - 1) + "|" + " " * (n - 1), end="   ")
        print()

    print("-" * (n * 6))
    print("  A".center(n * 2), "  B".center(n * 2), "  C".center(n * 2))
    print("\n")
    time.sleep(0.9)

def move_disk(towers, source, target):
    global step_count

    disk = towers[source].pop()
    towers[target].append(disk)
    step_count += 1

    move_msg = f"Move disk {disk} from {source} ➝ {target}"
    display_towers(towers, total_disks, move_msg)

#Recursive function
def tower_of_hanoi(n, source, target, auxiliary, towers):
    #BASE CASE
    if n == 1:
        move_disk(towers, source, target)
        return

    #RECURSION STEP 1
    tower_of_hanoi(n - 1, source, auxiliary, target, towers)

    #Move nth disk
    move_disk(towers, source, target)

    #RECURSION STEP 2
    tower_of_hanoi(n - 1, auxiliary, target, source, towers)

def main():
    global total_disks

    print("=== Tower of Hanoi (Final Visual Demo) === \n")
    total_disks = int(input("Enter number of disks (recommended 3-5): "))

    towers = {
        'A': list(range(total_disks, 0, -1)),
        'B': [],
        'C': []
    }

    #Initial state
    display_towers(towers, total_disks, "Initial Setup")

    #Run solution
    tower_of_hanoi(total_disks, 'A', 'C', 'B', towers)

    print("=" * 50)
    print("SOLVED!".center(50))
    print(f"Total steps taken: {step_count}".center(50))
    print("=" * 50)

if __name__ == "__main__":
    main()
