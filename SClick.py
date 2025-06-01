import pydirectinput
import time
from pynput.mouse import Listener

# Флаг для управления состоянием кликера
clicker_active = False

def toggle_clicker():
    """Переключает состояние кликера."""
    global clicker_active
    clicker_active = not clicker_active
    if clicker_active:
        print("Кликер включен")
    else:
        print("Кликер выключен")

def auto_clicker():
    """Автоматический кликер левой кнопкой мыши."""
    while True:
        if clicker_active:
            pydirectinput.click()  # Выполняем клик левой кнопкой
            time.sleep(0.1)  # Задержка между кликами
        else:
            time.sleep(0.01)  # Небольшая пауза для снижения нагрузки

def main():
    from pynput.mouse import Button

    # Обработчик событий нажатия кнопок мыши
    def on_click(x, y, button, pressed):
        if button.name == 'right' and pressed:  # Проверяем нажатие правой кнопки
            toggle_clicker()

    # Создаем поток для автоматического кликера
    import threading
    clicker_thread = threading.Thread(target=auto_clicker, daemon=True)
    clicker_thread.start()

    # Отслеживаем события мыши
    with Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == '__main__':
    print("Программа запущена. Нажмите правую кнопку мыши для включения/выключения кликера.")
    main()