import threading
from qr_processor import process_qr_code
from gui import create_gui
from warehouse_class import Warehouse
from location_selected_callback import location_selected_callback

def main():
    warehouse = Warehouse()
    # 미리 저장된 차량 정보
    existing_items = {'A12': '차량1', 'A21': '차량2', 'A31': '차량3'}

    # # 미리 저장된 차량 정보 로딩
    warehouse.load_existing_items(existing_items)
    
    qr_thread = threading.Thread(target=process_qr_code, args=(warehouse,))
    qr_thread.daemon = True
    qr_thread.start()
    
    create_gui(warehouse, callback=location_selected_callback)
    
if __name__ == "__main__":
    main()