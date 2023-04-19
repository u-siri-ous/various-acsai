import cv2
import numpy as np

#ex2 - book recognition and object classification (no dl/ml)
#database in Exercise_2/data

#load images in a list
image = []
img = cv2.imread('Exercise_2/data/think.jpg')
image.append(img)

img = cv2.imread('Exercise_2/data/kafka_sulla_spiaggia.jpg')
image.append(img)

img = cv2.imread('Exercise_2/data/postverita.jpg')
image.append(img)

#define classes for loaded objects
classes = ['think', 'kafka sulla spiaggia', 'postverita']

'''#create a descriptors database
def descriptorDB(images):
	descriptor_list = []
	orb = cv2.ORB_create(nfeatures=1000)

	# extract the features from each loaded image
	for image in images:
		#two variables for two arrays: keypoint array (x,y), descriptor array of the feature
		kpt, des = orb.detectAndCompute(image,None)
		descriptor_list.append(des)

	return descriptor_list

# do the match!
def objClassification(frame, descriptor_list):
	orb = cv2.ORB_create(nfeatures=1000)
	ktp, des = orb.detectAndCompute(frame,None)

	#create the instance of the matcher
	matcher = cv2.BFMatcher()
	best_matches = []

	#perform the mactehs with the database
	for descriptor in descriptor_list:
		matches = matcher.knnMatch(des, descriptor, k=2)
		good = []

		for m,n in matches:
			if m.distance < n.distance * 0.8:
				good.append([m])

		best_matches.append(len(good))

	# classId
	classId = -1

	if len(best_matches) > 0:
		max_val = max(best_matches)
		if max_val > 10:
			classId = best_matches.index(max_val)
	return classId

#let's see if it works
descriptor_list = descriptorDB(image)
webcam = cv2.VideoCapture(0)

while True:

	#read the frame from the webcam
	success, frame = webcam.read()

	#get the class id
	obj_id = objClassification(frame, descriptor_list)

	if obj_id != -1:
		cv2.putText(frame,classes[obj_id],(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)

	cv2.imshow("Frame", frame)
	k = cv2.waitKey(30)
	if k == ord("q"):
		break'''

#create the descriptor database via a function that takes the images as list and creates the descriptor list
def descriptorDB(images):
    descriptor_list = []
    orb = cv2.ORB_create(nfeatures=1000)    #using orb as it's faster than akaze and sift

    #extract features from each loaded image
    for image in images:
        kpt, des = orb.detectAndCompute(image, None)    
        #None means no mask (TL;DR: The mask parameter is a 1-channel numpy array with the same shape as the grayscale image in which you are trying to find features (if image shape is (480, 720), so is mask).
        #The values in the array are of type np.uint8, 255 means "use this pixel" and 0 means "don't")

        descriptor_list.append(des)
    
    return descriptor_list

#create a function to do matches
def objClass(frame, desc_list):
    orb = cv2.ORB_create(nfeatures=1000)    #using orb as it's faster than akaze and sift
    kpt_currentframe, des_currentframe = orb.detectAndCompute(frame, None)    

    #create matcher instance
    matcher = cv2.BFMatcher()
    best_matches = []

    #compare and compute matches with data
    for desc in desc_list:
        matches = matcher.knnMatch(des_currentframe, desc, k=2)
        good_match = []     #save good matches and perform ratio test (see panorama)

        for m,n in matches:
            if m.distance < n.distance * 0.8:
                good_match.append([m])

        #creating a list that contains the number of matches, as i need the highest number of matches to classify the object
        best_matches.append(len(good_match)) 

    #classId - index to use to pick the class from aforementioned array
    #we will locate it in the list via indexing the maximum valui in the matches
    classId = -1    

    if len(best_matches):
        max_val = max(best_matches)

        if max_val > 10: #if i have enought points to classify
            classId = best_matches.index(max_val)

    return classId

#try mamma mia
descriptor_list = descriptorDB(image)
webcam = cv2.VideoCapture(0)

while True:
    #read frame 
    success, frame = webcam.read()

    #get classId
    objId = objClass(frame, descriptor_list)

    #print name of class of found object
    if objId != -1:
        cv2.putText(frame, classes[objId], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 3)

    cv2.imshow("matches??", frame)

    k = cv2.waitKey(30)
    if k == ord("q"):  
        break