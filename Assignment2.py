import pygame
import random
import time

# Set up pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BAR_WIDTH = 20
GAP = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load sound effects
swap_sound = pygame.mixer.Sound("swap_sound.wav")  # Replace "swap_sound.wav" with your sound file path

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Merge Sort Simulation")

# Function to draw bars representing numbers
def draw_bars(nums, highlighted=[]):
    screen.fill(WHITE)
    for i, num in enumerate(nums):
        color = GREEN if i in highlighted else BLACK
        pygame.draw.rect(screen, color, (i * (BAR_WIDTH + GAP), SCREEN_HEIGHT - num, BAR_WIDTH, num))

# Function to play sound effect for swaps
def play_swap_sound():
    swap_sound.play()

# Merge Sort algorithm
def merge_sort(nums, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(nums, left, mid)
        merge_sort(nums, mid + 1, right)
        merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    left_part = nums[left:mid + 1]
    right_part = nums[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            nums[k] = left_part[i]
            i += 1
        else:
            nums[k] = right_part[j]
            j += 1
        draw_bars(nums, highlighted=[k])
        pygame.display.update()
        play_swap_sound()
        pygame.time.delay(50)
        k += 1

    while i < len(left_part):
        nums[k] = left_part[i]
        draw_bars(nums, highlighted=[k])
        pygame.display.update()
        pygame.time.delay(50)
        i += 1
        k += 1

    while j < len(right_part):
        nums[k] = right_part[j]
        draw_bars(nums, highlighted=[k])
        pygame.display.update()
        pygame.time.delay(50)
        j += 1
        k += 1

def main():
    nums = [random.randint(50, SCREEN_HEIGHT - 50) for _ in range(SCREEN_WIDTH // (BAR_WIDTH + GAP))]
    draw_bars(nums)
    pygame.display.update()

    # Merge sort the array
    merge_sort(nums, 0, len(nums) - 1)

    # Draw the final sorted array in green
    screen.fill(WHITE)
    draw_bars(nums)
    pygame.display.update()

    # Wait for user to close window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()
