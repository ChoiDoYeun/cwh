# run.py
import threading
from qr_processor import process_qr_code

def run(warehouse):
    print("Run 시작")
    qr_thread = threading.Thread(target=process_qr_code, args=(warehouse,))
    qr_thread.daemon = True
    qr_thread.start()