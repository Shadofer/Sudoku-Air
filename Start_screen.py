import cv2 as cv
import numpy as np

root=np.zeros((1000,1000,3),np.uint8)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(root, "SUDOKU AIR", (400,50), font, 1, (255,255,255), 2, cv.LINE_AA)
cv.rectangle(root, (400,55), (600,55), (255,255,255))

cv.rectangle(root, (400,200), (590,260), (0, 0, 255), cv.FILLED)
cv.putText(root, "PLAY!", (410,250), font, 2, (255,255,255), 3)

cv.putText(root, "CREDITS:", (0, 480), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
cv.rectangle(root, (0,485), (75,485), (255,255,255))
cv.putText(root, "Prajwal V Shenoy", (0, 500), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
cv.putText(root, "Pranav Ajay Desai", (0, 520), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
cv.putText(root, "Prerana M", (0, 540), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)

cv.imshow("SudokuAir", root)
cv.waitKey(0)
