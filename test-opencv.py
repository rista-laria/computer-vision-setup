import cv2

img = cv2.imread("gambar.jpg")

if img is None:
    print("Gambar tidak ditemukan")
else:
    print("Gambar berhasil dibaca")

cv2.imshow("Gambar Asli", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()