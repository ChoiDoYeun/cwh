# run.py
import threading
from qr_processor import process_qr_code
from motor.move_position import move_position
import time

def run(warehouse):
    print("Run 시작")
    
    move_position(225,350,50) # 입차대기장소로 이동
    time.sleep(0.5)
    
    # 멀티스레딩 #qr코드 인식 및 저장장소 처리
    qr_thread = threading.Thread(target=process_qr_code, args=(warehouse,))
    qr_thread.daemon = True
    qr_thread.start()