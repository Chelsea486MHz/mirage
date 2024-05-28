import cv2
import numpy as np

WINDOW_NAME = 'Mirage'
FACEBOX_MARGIN = 40  # pixels
PIXELATION_GRID_SIZE = 10  # pixels
FACE_SIZE_MIN = 30  # pixels

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a VideoCapture object to capture video from your webcam (0 represents the default camera)
cap = cv2.VideoCapture(0)

# Get webcam resolution
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


# Reads a frame from the default webcam
def getFrame():
    try:
        ret, frame = cap.read()
    except Exception as e:
        print(e)
        return None
    return frame


# Returns a list of detected faces in the frame
def FacesInFrame(frame):
    grayscaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayscaleFrame, scaleFactor=1.3, minNeighbors=5, minSize=(FACE_SIZE_MIN, FACE_SIZE_MIN))
    return faces


# Scrambles the faces in a frame
def scrambleFacesInFrame(frame, faces):
    for (x, y, w, h) in faces:
        # Crop the detected face region with a margin (FACEBOX_MARGIN)
        # face = frame[y: y + h, x: x + w]
        face = frame[y - FACEBOX_MARGIN: y + h + FACEBOX_MARGIN, x - FACEBOX_MARGIN: x + w + FACEBOX_MARGIN]

        # Replace the face in the original frame with random noise
        frame[y - FACEBOX_MARGIN: y + h + FACEBOX_MARGIN, x - FACEBOX_MARGIN: x + w + FACEBOX_MARGIN] = np.random.randint(0, 256, face.shape)

        # Pixelate the face region
        for i in range(0, h + (2 * FACEBOX_MARGIN), PIXELATION_GRID_SIZE):
            for j in range(0, w + (2 * FACEBOX_MARGIN), PIXELATION_GRID_SIZE):
                face[i:i + PIXELATION_GRID_SIZE, j:j + PIXELATION_GRID_SIZE] = np.mean(face[i:i + PIXELATION_GRID_SIZE, j:j + PIXELATION_GRID_SIZE])


# Scrambles the entire frame
def scrambleFrame(frame):
    newframe = cv2.cvtColor(np.random.randint(0, 256, (frame_height, frame_width, 3), dtype=np.uint8), cv2.COLOR_BGR2GRAY)
    for i in range(0, frame_height, PIXELATION_GRID_SIZE):
        for j in range(0, frame_width, PIXELATION_GRID_SIZE):
            newframe[i:i + PIXELATION_GRID_SIZE, j:j + PIXELATION_GRID_SIZE] = np.mean(newframe[i:i + PIXELATION_GRID_SIZE, j:j + PIXELATION_GRID_SIZE])
    return newframe


while True:
    frame = getFrame()
    faces = FacesInFrame(frame)

    # Run face detection. If it failed, we scramble everything.
    if len(faces) != 0:
        scrambleFacesInFrame(frame, faces)
        if len(FacesInFrame(frame)) != 0:
            frame = scrambleFrame(frame)

    else:
        frame = scrambleFrame(frame)

    # Display the frame
    cv2.imshow(WINDOW_NAME, frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
