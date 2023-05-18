import cv2

cap = cv2.VideoCapture(0)
# Define the codec for the video file
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create a VideoWriter object to save the video
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    _, frame = cap.read()

    cv2.imshow("frame", frame)

    # Write the frame to the video file
    out.write(frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

