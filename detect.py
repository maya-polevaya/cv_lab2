from ultralytics import YOLO
import cv2

# Загружаем модель YOLOv8 для сегментации
model = YOLO("yolov8n-seg.pt")  # n = nano (самая быстрая для CPU)

# Открываем видео
video_path = "input.mp4"
cap = cv2.VideoCapture(video_path)

# Получаем параметры видео
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Создаём видео для записи результатов
output_path = "output.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

frame_count = 0
print(f"Начинаем обработку видео: {video_path}")

# Обрабатываем каждый кадр
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Запускаем сегментацию на кадре
    results = model(frame, verbose=False)

    # Рисуем результаты на кадре
    annotated_frame = results[0].plot()

    # Записываем кадр в выходное видео
    out.write(annotated_frame)

    frame_count += 1
    if frame_count % 10 == 0:  # Выводим прогресс каждые 10 кадров
        print(f"Обработано кадров: {frame_count}")

# Закрываем всё
cap.release()
out.release()

print(f"Готово! Обработано {frame_count} кадров.")
print(f"Результат сохранён в: {output_path}")
