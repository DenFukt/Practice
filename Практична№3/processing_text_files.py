import threading
import os

total_lines = 0
total_words = 0
total_chars = 0

stats_lock = threading.Lock()

def analyze_file(filename):
    global total_lines, total_words, total_chars
    
    try:
        if not os.path.exists(filename):
            print(f"Файл {filename} не знайдено.")
            return

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

            lines = content.count('\n') + (1 if content else 0)
            words = len(content.split())
            chars = len(content)
            
            print(f"[Потік {threading.current_thread().name}] Оброблено {filename}: "
                  f"{lines} рядків, {words} слів.")

            with stats_lock:
                total_lines += lines
                total_words += words
                total_chars += chars
                
    except Exception as e:
        print(f"Помилка при читанні {filename}: {e}")

def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]

    for name in files:
        with open(name, "w", encoding="utf-8") as f:
            f.write(f"Це тестовий контент для {name}.\nТут кілька рядків.\nКінець файлу.")

    threads = []

    for i, file_name in enumerate(files):
        t = threading.Thread(target=analyze_file, args=(file_name,), name=f"Worker-{i+1}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n" + "="*30)
    print("ЗАГАЛЬНА СТАТИСТИКА:")
    print(f"Всього рядків: {total_lines}")
    print(f"Всього слів:   {total_words}")
    print(f"Всього знаків: {total_chars}")
    print("="*30)

if __name__ == "__main__":
    main()