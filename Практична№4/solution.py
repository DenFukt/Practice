import multiprocessing
import time

def writer_process(queue):
    """Функція для процесу-відправника"""
    messages = [
        "Перше повідомлення через Queue",
        "Друге повідомлення: Windows теж може!",
        "Третє повідомлення: Завдання виконано."
    ]
    
    print(f"[Writer] Процес запущено.")
    for msg in messages:
        print(f"[Writer] Надсилаю: {msg}")
        queue.put(msg)
        time.sleep(1)
    print("[Writer] Всі повідомлення відправлено.")

def reader_process(queue):
    """Функція для процесу-отримувача"""
    print(f"[Reader] Процес запущено, чекаю дані...")
    for i in range(3):
        msg = queue.get()
        print(f"[Reader] Отримано {i+1}: {msg}")
    print("[Reader] Всі повідомлення прочитано.")

if __name__ == "__main__":
    shared_queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=writer_process, args=(shared_queue,))
    p2 = multiprocessing.Process(target=reader_process, args=(shared_queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("[*] Роботу програми завершено успішно.")