import cv2,time
import datetime 

#for i in range(0,10):

for j in range(0,4):

  cap=cv2.VideoCapture(0)

  print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


  check , frame =cap.read() 
        # date and time on it 

  font= cv2.FONT_HERSHEY_SIMPLEX
  text = 'width:'+ str(cap.get(3)) + 'height:' + str(cap.get(4)) 
  datet=str(datetime.datetime.now())
  frame =cv2.putText(frame , datet ,(10,50), font ,1,(0,255,255), 2 ,cv2.LINE_AA)
  print(check)
  print(frame)

        #representing image 
  cv2.imshow("capturing",frame)

        # for press any key to out (millis )

  cv2.waitKey(0)
 
        # saving image 
  cv2.imwrite(str(j)+'.jpg',frame)

         # shutdown the camera 
  cap.release()
 
