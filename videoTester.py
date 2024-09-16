import cv2
import os
import numpy as np 
import faceRecognition as fr 


class VideoCamera(object):

	def __init__(self):
		#self.faces,self.faceID=fr.labels_for_training_data('D:/final_project/TrainImages')
		#self.face_recognizer=fr.train_classifier(self.faces,self.faceID)
		#self.face_recognizer.save('trainingData.yml')
		self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
		self.face_recognizer.read('D:/final_project/testData.yml')
		self.name={0:"Not match",1:"Verified"}
		self.cap=cv2.VideoCapture(0)

		
	def getFrame(self):
		verifiedFrame = 0
		while True:
			ret,test_img=self.cap.read()
			faces_detected,gray_img=fr.faceDetection(test_img)

			for(x,y,w,h) in faces_detected:
			   cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=3)

			resized_img=cv2.resize(test_img,(1000,700))
			cv2.imshow("face detection",resized_img)
			cv2.waitKey(10)

			for face in faces_detected:
				(x,y,w,h)=face
				roi_gray=gray_img[y:y+h,x:x+h]
				label,confidence=self.face_recognizer.predict(roi_gray)
				print("confidence:",confidence)
				print("label:",label)
				fr.draw_rect(test_img,face)
				predicted_name=self.name[label]
				if confidence>50:
					if label == 0:
						verifiedFrame = 0
						fr.put_text(test_img,predicted_name,x,y)
					if label == 1:
						verifiedFrame +=1
						fr.put_text(test_img,predicted_name,x,y)

			resized_img=cv2.resize(test_img,(1000,700))
			cv2.imshow("face detection",resized_img)
			if verifiedFrame == 28:
				self.releaseCamera()
				return True
			if cv2.waitKey(2) == 27:
				self.releaseCamera()
				return False

	def releaseCamera(self):
		self.cap.release()
		cv2.destroyAllWindows()

