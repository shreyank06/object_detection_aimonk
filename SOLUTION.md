# Solution Documentation

## Approach

Built a microservice architecture with three components:
1. **Frontend** (React) - User interface for image upload
2. **UI Backend** (Flask) - REST API handling requests
3. **AI Backend** (Flask + OpenCV) - YOLOv3 object detection

## Steps

1. Set up Docker containers for each service
2. Implemented image upload endpoint in UI backend
3. Integrated YOLOv3 model in AI backend for object detection
4. Connected services via Docker network
5. Returned detection results as JSON with bounding box coordinates
6. Saved output images with drawn bounding boxes

## References

- YOLOv3: https://pjreddie.com/darknet/yolo/
- OpenCV DNN module: https://docs.opencv.org/master/d6/d0f/group__dnn.html
- Flask documentation: https://flask.palletsprojects.com/
- Docker Compose: https://docs.docker.com/compose/

## Output Format

Detection results saved in `outputs/` folder:
- `*_detected.jpg` - Images with bounding boxes
- `*_detection.json` - JSON with detection data (class, confidence, coordinates)
