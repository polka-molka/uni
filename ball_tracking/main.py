import cv2
import numpy as np


def track_image(image, color_range):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, color_range[0], color_range[1])
    kernel = np.ones((8, 8), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if center:
            cv2.circle(image, center, 5, (0, 0, 0), -1)

    return image, mask


def track_video(input_path, output_path, color_range):
    cap = cv2.VideoCapture(input_path)

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    max_width = 800
    max_height = 600
    ratio = min(max_width / frame_width, max_height / frame_height)  # Obliczenie proporcji zmniejszenia

    cv2.namedWindow('Mask Video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Mask Video', int(frame_width * ratio), int(frame_height * ratio))
    cv2.namedWindow('Tracked Video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Tracked Video', int(frame_width * ratio), int(frame_height * ratio))

    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        tracked_frame, mask = track_image(frame, color_range)

        cv2.imshow('Mask Video', mask)
        cv2.imshow('Tracked Video', frame)
        out.write(tracked_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


image_ball = cv2.imread('ball.png')
b_h_min = 0
b_h_max = 179
b_s_min = 98
b_s_max = 189
b_v_min = 0
b_v_max = 255
color_range_ball = (np.array([b_h_min, b_s_min, b_v_min]), np.array([b_h_max, b_s_max, b_v_max]))
tracked_image_ball, mask_ball = track_image(image_ball, color_range_ball)
cv2.imshow('Tracked Image', tracked_image_ball)
cv2.imshow('Mask Image', mask_ball)
cv2.waitKey(0)
cv2.destroyAllWindows()
track_video('movingball.mp4', 'tracked_movingball.avi', color_range_ball)

image_object = cv2.imread('bullet.png')
o_h_min = 7
o_h_max = 130
o_s_min = 147
o_s_max = 179
o_v_min = 0
o_v_max = 253
color_range_other_object = (np.array([o_h_min, o_s_min, o_v_min]), np.array([o_h_max, o_s_max, o_v_max]))
tracked_image_object, mask_object = track_image(image_object, color_range_other_object)
# cv2.imshow('Tracked Image', tracked_image_coins)
# cv2.imshow('Mask Image', mask_coins)
cv2.waitKey(0)
cv2.destroyAllWindows()
track_video('movingbullet.mp4', 'tracked_movingbullet.mp4', color_range_other_object)
