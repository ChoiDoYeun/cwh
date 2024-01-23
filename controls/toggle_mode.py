# toggle_mode.py
from motor.in_out_mode import input_mode, output_mode
import threading
from qr_processor import process_qr_code
from warehouse_class import Warehouse

def toggle_mode(button, mode, mode_name,location):
    warehouse = Warehouse()
    mode['state'] = not mode['state']
    new_state = "ON" if mode['state'] else "OFF"
    button.config(bg='green' if mode['state'] else 'SystemButtonFace')
    print(f"{mode_name} mode is now {new_state}")
    
    # # 모드와 상태에 따라 동작 수행
    # if mode_name == "INPUT" and new_state == "ON":
    #     # 멀티스레딩 #qr코드 인식 및 저장장소 처리
    #     qr_thread = threading.Thread(target=process_qr_code, args=(warehouse,))
    #     qr_thread.daemon = True
    #     qr_thread.start()
        
    #     x,y,z = warehouse.calculate_coordinates(location)
    #     output_mode(x,y,z)
        
    # # INPUT 모드 ON 상태일 때 수행할 작업
    #     input_mode()
    # elif mode_name == "INPUT" and new_state == "OFF":
    # # INPUT 모드 OFF 상태일 때 수행할 작업
    #     pass  # 필요한 작업 추가
    # elif mode_name == "OUTPUT" and new_state == "ON":
    # # OUTPUT 모드 ON 상태일 때 수행할 작업
    #     output_mode()
    # elif mode_name == "OUTPUT" and new_state == "OFF":
    # # OUTPUT 모드 OFF 상태일 때 수행할 작업
    #     pass  # 필요한 작업 추가