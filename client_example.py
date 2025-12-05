"""
Python Client Example for Object Detection Microservice
Demonstrates how to use the detection API
"""

import requests
import json
import os
from pathlib import Path
import argparse

class ObjectDetectionClient:
    """Client for interacting with Object Detection Microservice"""

    def __init__(self, base_url='http://localhost:5000'):
        self.base_url = base_url
        self.session = requests.Session()

    def detect_objects(self, image_path):
        """
        Send image for object detection

        Args:
            image_path (str): Path to image file

        Returns:
            dict: Detection results
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")

        with open(image_path, 'rb') as f:
            files = {'image': f}
            response = self.session.post(
                f'{self.base_url}/api/detect',
                files=files,
                timeout=60
            )

        response.raise_for_status()
        return response.json()

    def get_results(self, request_id):
        """
        Retrieve detection results by request ID

        Args:
            request_id (str): Request ID from detection response

        Returns:
            dict: Detection results
        """
        response = self.session.get(
            f'{self.base_url}/api/status/{request_id}',
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    def health_check(self):
        """
        Check if service is healthy

        Returns:
            dict: Health status
        """
        response = self.session.get(f'{self.base_url}/health', timeout=5)
        response.raise_for_status()
        return response.json()

    def process_batch(self, image_dir, output_dir=None):
        """
        Process multiple images in a directory

        Args:
            image_dir (str): Directory containing images
            output_dir (str): Directory to save results (optional)

        Returns:
            list: Results for each image
        """
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        results = []
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}

        for image_path in Path(image_dir).glob('*'):
            if image_path.suffix.lower() not in image_extensions:
                continue

            try:
                print(f"Processing: {image_path.name}")
                result = self.detect_objects(str(image_path))
                results.append(result)

                # Save results if output directory specified
                if output_dir:
                    request_id = result['request_id']
                    result_file = os.path.join(
                        output_dir,
                        f"{request_id}_result.json"
                    )
                    with open(result_file, 'w') as f:
                        json.dump(result, f, indent=2)
                    print(f"  ✓ Detected {result['detection_results']['objects_detected']} objects")

            except Exception as e:
                print(f"  ✗ Error: {e}")

        return results

def main():
    parser = argparse.ArgumentParser(
        description='Object Detection Client'
    )
    parser.add_argument(
        'image',
        help='Image file or directory path'
    )
    parser.add_argument(
        '--url',
        default='http://localhost:5000',
        help='Base URL of detection service'
    )
    parser.add_argument(
        '--output',
        help='Output directory for results'
    )
    parser.add_argument(
        '--health',
        action='store_true',
        help='Check service health'
    )

    args = parser.parse_args()

    client = ObjectDetectionClient(args.url)

    try:
        # Health check
        if args.health:
            print("Checking service health...")
            health = client.health_check()
            print(f"Status: {health}")
            return

        # Process image or directory
        image_path = args.image

        if os.path.isdir(image_path):
            print(f"Processing directory: {image_path}")
            results = client.process_batch(image_path, args.output)
            print(f"\nProcessed {len(results)} images")

        else:
            print(f"Processing image: {image_path}")
            result = client.detect_objects(image_path)

            print("\nDetection Results:")
            print(json.dumps(result, indent=2))

            # Save results if output specified
            if args.output:
                os.makedirs(args.output, exist_ok=True)
                result_file = os.path.join(
                    args.output,
                    f"{result['request_id']}_result.json"
                )
                with open(result_file, 'w') as f:
                    json.dump(result, f, indent=2)
                print(f"\nResults saved to: {result_file}")

    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to service. Is it running?")
        print(f"URL: {args.url}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == '__main__':
    main()
