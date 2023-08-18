import threading
import time

def delayed_thread():
    print("Geciken thread başladı.")
    time.sleep(3)  # 3 saniye gecikme
    print("Geciken thread bitti.")

def regular_thread():
    for i in range(5):
        print("Düzgün çalışan thread çalışıyor:", i)
        time.sleep(1)
    print("Düzgün çalışan thread bitti.")

if __name__ == "__main__":
    print("Program başladı.")


    delayed_thread = threading.Thread(target=delayed_thread)
    regular_thread = threading.Thread(target=regular_thread)

    
    delayed_thread.start()
    regular_thread.start()

    # Threadlerin bitmesini bekle
    delayed_thread.join()
    regular_thread.join()

    print("Program bitti.")
