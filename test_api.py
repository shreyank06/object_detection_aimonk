"""
Test script to validate the microservice architecture
Run this after starting the services with docker-compose
"""

import requests
import json
import cv2
import numpy as np
import os
from pathlib import Path

# Configuration
UI_BACKEND_URL = 'http://localhost:5000'
AI_BACKEND_URL = 'http://localhost:5001'
TEST_IMAGE_PATH = 'test_image.jpg'

def create_test_image():
    """Create a simple test image"""
    # Create a blank image with some shapes
    img = np.zeros((480, 640, 3), dtype=np.uint8)

    # Add some colored rectangles to simulate objects
    cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), -1)
    cv2.rectangle(img, (400, 100), (600, 300), (255, 0, 0), -1)
    cv2.circle(img, (320, 240), 50, (0, 0, 255), -1)

    # Add text
    cv2.putText(img, 'Test Image', (250, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imwrite(TEST_IMAGE_PATH, img)
    print(f"Test image created: {TEST_IMAGE_PATH}")

def test_health_checks():
    """Test health endpoints"""
    print("\n=== Testing Health Checks ===")

    try:
        ui_health = requests.get(f'{UI_BACKEND_URL}/health', timeout=5)
        print(f"UI Backend Health: {ui_health.json()}")
    except Exception as e:
        print(f"UI Backend Health Check Failed: {e}")

    try:
        ai_health = requests.get(f'{AI_BACKEND_URL}/health', timeout=5)
        print(f"AI Backend Health: {ai_health.json()}")
    except Exception as e:
        print(f"AI Backend Health Check Failed: {e}")

def test_detection():
    """Test object detection through UI backend"""
    print("\n=== Testing Object Detection ===")

    if not os.path.exists(TEST_IMAGE_PATH):
        create_test_image()

    with open(TEST_IMAGE_PATH, 'rb') as f:
        files = {'image': f}
        try:
            response = requests.post(
                f'{UI_BACKEND_URL}/api/detect',
                files=files,
                timeout=60
            )

            if response.status_code == 200:
                result = response.json()
                print(f"Detection Successful!")
                print(f"Request ID: {result['request_id']}")
                print(f"Objects Detected: {result['detection_results'].get('objects_detected', 0)}")
                print(f"Response: {json.dumps(result, indent=2)}")

                # Save results
                save_results(result)
                return result['request_id']
            else:
                print(f"Detection Failed: {response.text}")
        except Exception as e:
            print(f"Error during detection: {e}")

def test_status_check(request_id):
    """Test status check endpoint"""
    print(f"\n=== Testing Status Check for Request {request_id} ===")

    try:
        response = requests.get(f'{UI_BACKEND_URL}/api/status/{request_id}', timeout=5)

        if response.status_code == 200:
            result = response.json()
            print(f"Status Check Successful!")
            print(f"Result: {json.dumps(result, indent=2)}")
        else:
            print(f"Status Check Failed: {response.text}")
    except Exception as e:
        print(f"Error during status check: {e}")

def save_results(result):
    """Save results to JSON file"""
    output_dir = 'test_results'
    os.makedirs(output_dir, exist_ok=True)

    result_file = os.path.join(output_dir, f"{result['request_id']}_result.json")
    with open(result_file, 'w') as f:
        json.dump(result, f, indent=2)
    print(f"Results saved to: {result_file}")

def main():
    """Run all tests"""
    print("Starting API Tests...")
    print(f"UI Backend: {UI_BACKEND_URL}")
    print(f"AI Backend: {AI_BACKEND_URL}")

    # Test health
    test_health_checks()

    # Test detection
    request_id = test_detection()

    # Test status
    if request_id:
        test_status_check(request_id)

    print("\n=== Testing Complete ===")

if __name__ == '__main__':
    main()
