import cv2

# Draw line:
def draw_line(image):
    im_height, im_width = image.shape[:2]
    center = (im_width/2, im_height/2)
    cv2.rectangle(image, (0, int(center[1])), (im_width - 2, int(center[1] + 1)), (0, 0, 0xFF), 4)
    return center
def draw_line_green(image):
    im_height, im_width = image.shape[:2]
    center = (im_width/2, im_height/2)
    cv2.rectangle(image, (0, int(center[1])), (im_width - 2, int(center[1] + 1)), (0, 0xFF, 0), 4)
    return center
def put_number_car(image, count):
    text = "Xe oto : {}".format(count)
    cv2.putText(image, text, (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

def put_objectID_into_object(image, centroid, objectID, score):
    #text = "{}".format(objectID)
    text = '{}: {}'.format('Car',str(score).replace("[","").replace("]","").replace("'",""))
    cv2.putText(image, text, (centroid[0], centroid[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0xFF, 0), 1)

def put_text_into_object(image, startX, startY, score):
    text = '{}: {}'.format('Car',str(score).replace("[","").replace("]","").replace("'",""))
    cv2.putText(image, text, (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0xFF, 0), 1)
