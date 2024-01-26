# toggle_mode.py
import threading
from qr_processor import process_qr_code

global stop_thread
stop_thread = False
qr_thread = None  # 스레드를 전역 변수로 선언

def input_on(warehouse):
    global stop_thread, qr_thread
    stop_thread = False
    print("Input Mode ON")

    qr_thread = threading.Thread(target=process_qr_code, args=(warehouse,))
    qr_thread.start()
    
def input_off():
    global stop_thread, qr_thread
    stop_thread = True
    if qr_thread:
        qr_thread.join()  # 스레드가 종료될 때까지 기다립니다
    print("Input Mode OFF")