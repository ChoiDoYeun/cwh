import time
from camera import read_qr_code
from motor.in_out_mode import input_mode

stop_thread = False


# qr코드 정보처리
def process_qr_code(warehouse):
    global stop_thread
    qr_code_image_path = '세단_QR_Code.PNG'
    while not stop_thread:
        #capture_image(qr_code_image_path)
        qr_data = read_qr_code(qr_code_image_path)
        if qr_data:
            cars = qr_data.split('\n')
            for car in cars:
                if car:
                    location = warehouse.store_item(car)
                    if location:
                        print(f"{car}가 {location}에 저장되었습니다.")
                        x, y, z = warehouse.calculate_coordinates(location)
                        input_mode(x,y,z)
                    else:
                        print(f"{car}를 저장할 공간이 없습니다.")
        else:
            print("QR 코드를 읽을 수 없습니다.")
        
        # 15초마다 동작
        time.sleep(5)
