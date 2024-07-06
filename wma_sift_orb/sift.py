import cv2

img1 = cv2.imread('gaz1_white.jpg')
img2 = cv2.imread('gaz2_white.jpg')

image1 = cv2.resize(img1, (400, 350))
image2 = cv2.resize(img2, (400, 350))

sift = cv2.SIFT_create()

keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

bf = cv2.BFMatcher()

cap = cv2.VideoCapture('gaz.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    keypoints_frame, descriptors_frame = sift.detectAndCompute(frame, None)

    matches1 = bf.knnMatch(descriptors1, descriptors_frame, k=2)
    matches2 = bf.knnMatch(descriptors2, descriptors_frame, k=2)

    good_matches1 = [m for m, n in matches1 if m.distance < 0.75 * n.distance]
    good_matches2 = [m for m, n in matches2 if m.distance < 0.75 * n.distance]

    best_matches = good_matches1 if len(good_matches1) > len(good_matches2) else good_matches2
    best_image = image1 if len(good_matches1) > len(good_matches2) else image2

    result_image = cv2.drawMatches(best_image, (keypoints1 if best_image is image1 else keypoints2),
                                   frame, keypoints_frame, best_matches, None,
                                   flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


    cv2.imshow('Matches', result_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
