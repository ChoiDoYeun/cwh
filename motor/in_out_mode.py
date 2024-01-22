# in_out_mode.py
from warehouse_class import Warehouse
from motor.move_position import move_position
from motor.move_item import move_item_high,move_item_low

def input_mode(location): 
    warehouse = Warehouse()
    x,y,z = warehouse.calculate_coordinates(location) # 차량이 저장된 위치의 x,y,z값 계산
    move_item_low() # 입차대기장소로 와있는 상태에서 차량을 함으로 이동 # move_item_low 와 move_item_high의 위치는 바뀔수있음
    move_position(x,y,z) # 입차장소로 이동
    move_item_high()    # 차를 함에서 입차장소로 이동
    # move_position(입차대기장소의 x,y,z) # 입차대기장소로 이동
    
def output_mode(location):
    warehouse = Warehouse()
    x,y,z = warehouse.calculate_coordinates(location)
    move_item_high() # move_item_low 와 move_item_high의 위치는 바뀔수있음
    move_position(x,y,z)
    move_item_low()
    # move_position(출차대기장소의 x,y,z) # 출차대기장소로 이동