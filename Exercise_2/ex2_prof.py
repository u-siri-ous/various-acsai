import cv2
import numpy as np

#ex2 - book recognition and object classification (no dl/ml)
#database in Exercise_2/data

#load images in a list
images = []
img1 = cv2.imread('Exercise_2/data/think.jpg')
images.append(img1)

img2 = cv2.imread('Exercise_2/data/kafka_sulla_spiaggia.jpg')
images.append(img2)

img3 = cv2.imread('Exercise_2/data/postverita.jpg')
images.append(img3)

#define classes for loaded objects
classes = ['think', 'kafka sulla spiaggia', 'postverita']

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
        matches = matcher.knnMatch(des_currentframe, k=2)
        good_match = []     #save good matches and perform ratio test (see panorama)

        for m,n in matches:
            if m.distance < n.distance * 0.4:
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
descriptor_list = descriptorDB(images)
webcam = cv2.VideoCapture(0)

while True:
    #read frame 
    success, frame = webcam.read()

    #get classId
    objId = objClass(frame, descriptor_list)

    #print name of class of found object
    if objId != -1:
        cv2.putText(frame, classes[objId], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)

    cv2.imshow("matches??", frame)

    k = cv2.waitKey(30)
    if k == ord("q"):  
        break