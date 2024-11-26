import cv2
from simple_facerec import SimpleFacerec


def parodyFunction():
    sfr = SimpleFacerec()
    #sfr.load_encoding_images("images/")
    sfr.load_encoding_images("C:\\Users\\neelanjan\\Documents\\Code\\Fest\\face_rec\\images")

    cap = cv2.VideoCapture(0)

    #global t_output
    t_output = []
    #while True:
    ret, frame = cap.read()
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        #t=name.split()
        t=name
        t_output.append(t)
        cv2.putText(frame, t[0],(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    
    #if key == 27:
    #    break
    
    cap.release()
    cv2.destroyAllWindows()

    print(t_output[0])
    return t_output[0]


#parodyFunction()
#print(parodyFunction())