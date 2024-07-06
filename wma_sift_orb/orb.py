import cv2

img1 = cv2.imread('gaz1_white.jpg')
img2 = cv2.imread('gaz2_white.jpg')

image1 = cv2.resize(img1, (400, 350))
image2 = cv2.resize(img2, (400, 350))

orb = cv2.ORB_create()

keypoints1, descriptors1 = orb.detectAndCompute(image1, None)
keypoints2, descriptors2 = orb.detectAndCompute(image2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

cap = cv2.VideoCapture('gaz.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    keypoints_frame, descriptors_frame = orb.detectAndCompute(frame, None)

    matches1 = bf.match(descriptors1, descriptors_frame)
    matches2 = bf.match(descriptors2, descriptors_frame)

    matches1 = sorted(matches1, key=lambda x: x.distance)
    matches2 = sorted(matches2, key=lambda x: x.distance)

    best_matches = matches1 if len(matches1) > len(matches2) else matches2
    best_image = image1 if len(matches1) > len(matches2) else image2

    result_image = cv2.drawMatches(best_image, (keypoints1 if best_image is image1 else keypoints2),
                                   frame, keypoints_frame, best_matches[:30], None,
                                   flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv2.imshow('Matches', result_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
