import cv2
import numpy as np


def nothing(x):
    pass


# Utwórz okno
cv2.namedWindow('image')

# Stwórz suwaki dla parametrów dolnego i górnego zakresu koloru
cv2.createTrackbar('Hue Lower', 'image', 0, 179, nothing)
cv2.createTrackbar('Saturation Lower', 'image', 0, 255, nothing)
cv2.createTrackbar('Value Lower', 'image', 0, 255, nothing)
cv2.createTrackbar('Hue Upper', 'image', 179, 179, nothing)
cv2.createTrackbar('Saturation Upper', 'image', 255, 255, nothing)
cv2.createTrackbar('Value Upper', 'image', 255, 255, nothing)

# Wczytaj obraz
image = cv2.imread('ball.png')

while True:
    # Skonwertuj obraz na przestrzeń kolorów HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Pobierz aktualne wartości suwaków
    hue_lower = cv2.getTrackbarPos('Hue Lower', 'image')
    saturation_lower = cv2.getTrackbarPos('Saturation Lower', 'image')
    value_lower = cv2.getTrackbarPos('Value Lower', 'image')
    hue_upper = cv2.getTrackbarPos('Hue Upper', 'image')
    saturation_upper = cv2.getTrackbarPos('Saturation Upper', 'image')
    value_upper = cv2.getTrackbarPos('Value Upper', 'image')

    # Zdefiniuj zakres dolnego i górnego koloru
    lower_color = np.array([hue_lower, saturation_lower, value_lower])
    upper_color = np.array([hue_upper, saturation_upper, value_upper])

    # Utwórz maskę za pomocą zdefiniowanego zakresu kolorów
    mask = cv2.inRange(hsv, lower_color, upper_color)
    kernel = np.ones((5, 5), np.uint8)

    # Zastosowanie operacji zamknięcia do maski
    closing_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Zmniejsz rozmiar obrazu i maski proporcjonalnie
    resized_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    resized_mask = cv2.resize(closing_mask, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)

    # Wyświetl oryginalny obraz oraz maskę
    cv2.imshow('image', cv2.hconcat([resized_image, cv2.cvtColor(resized_mask, cv2.COLOR_GRAY2BGR)]))

    # Zatrzymaj pętlę, jeśli naciśnięto klawisz 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zamknij wszystkie okna
cv2.destroyAllWindows()
