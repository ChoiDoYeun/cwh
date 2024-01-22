# calculate_steps_and_direction.py
from motor.config import STEPS_PER_MM

def calculate_steps_and_direction(current_pos, target_pos):
    print(f"현재 위치: {current_pos}, 목표 위치: {target_pos}")
    if target_pos > current_pos:
        direction = "HIGH"
        steps = (target_pos - current_pos) * STEPS_PER_MM
        print("Direction:", direction)
        print("Steps:", steps)
    else:
        direction = "LOW"
        steps = (current_pos - target_pos) * STEPS_PER_MM
        print("Direction:", direction)
        print("Steps:", steps)
    return steps, direction