import cv2 as cv
import numpy as np

root=np.zeros((1000,1000,3),np.uint8)

class Button():
    def  __init__(self, pos, text, size=[70,70]):
        self.pos = pos
        self.size = size
        self.text = text
    
    def draw(self, root):
        x,y= self.pos
        w,h= self.size 
        cv.rectangle(root, self.pos, (x+w, y+h), (0,0,255), cv.FILLED)
        cv.putText(root, self.text, (x+20, y+50), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)
        
        return root
        
    def ifClicked(self, xcor, ycor):
        if((xcor>=self.pos.x and xcor<=self.pos.x+self.size.w) and (ycor>=self.pos.y and ycor<=self.pos.y+self.size.h)):
            return True
        return False
        

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(root, "SUDOKU AIR", (400,50), font, 1, (255,255,255), 2, cv.LINE_AA)
cv.rectangle(root, (400,55), (600,55), (255,255,255))

startScreen=Button([400,200], "PLAY!", [170,80])


cv.putText(root, "CREDITS:", (0, 480), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
cv.rectangle(root, (0,485), (75,485), (255,255,255))
cv.putText(root, "Prajwal V Shenoy", (0, 500), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
cv.putText(root, "Pranav Ajay Desai", (0, 520), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
cv.putText(root, "Prerana M", (0, 540), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)

run = True

while run:
    cv.imshow("SudokuAir", root)

    root=startScreen.draw(root)

    if(startScreen.ifClicked(xcor, ycor)):
        run = False
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

