# move_item.py
from motor.move_motor import move_motor
from motor.config import initialize

def move_item_high():
    A_STEP, A_DIR = initialize()
    steps = 500 # 예시
    direction = "HIGH" # 예시
    move_motor(A_STEP, A_DIR, steps, direction)
    
def move_item_low():
    A_STEP, A_DIR = initialize()
    steps = 500 # 예시
    direction = "LOW" # 예시
    move_motor(A_STEP, A_DIR, steps, direction)