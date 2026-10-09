import cv2
import os

# Путь к видео и папке для кадров
video_path = "output.mp4"  # Можно поменять на "input.mp4", если нужны исходные кадры
frames_dir = "frames"

# Создаем папку, если её нет
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

cap = cv2.VideoCapture(video_path)
frame_count = 0
saved_count = 0

print(f"Начинаем извлечение кадров из {video_path}...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Сохраняем каждый 10-й кадр, чтобы не засорять папку (можно изменить число)
    if frame_count % 10 == 0:
        frame_name = os.path.join(frames_dir, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(frame_name, frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f"Готово! Сохранено {saved_count} кадров в папку {frames_dir}.")