import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge

import cv2
import torch
import json

from groundingdino.util.inference import load_model, predict


class GreenCrabDetector(Node):

    def __init__(self):
        super().__init__('green_crab_detector')

        self.bridge = CvBridge()

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.get_logger().info(f"Using device: {self.device}")

        config_path = "src/green_crab_detector/model/groundingdino_config.py"
        weights_path = "src/green_crab_detector/model/groundingdino_weights.pth"

        self.model = load_model(config_path, weights_path)
        self.model.to(self.device)
        self.model.eval()

        self.text_prompt = (
            "a european green crab with five spines on each side of its shell"
        )

        self.box_threshold = 0.4
        self.text_threshold = 0.25

        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)

        self.image_pub = self.create_publisher(
            Image,
            '/green_crab/image_annotated',
            10)

        self.detection_pub = self.create_publisher(
            String,
            '/green_crab/detections',
            10)

        self.get_logger().info("Green Crab Detector Ready")

    def image_callback(self, msg):

        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        with torch.no_grad():
            boxes, logits, phrases = predict(
                model=self.model,
                image=image_rgb,
                caption=self.text_prompt,
                box_threshold=self.box_threshold,
                text_threshold=self.text_threshold,
                device=self.device
            )

        h, w, _ = frame.shape
        detections = []

        for box, logit in zip(boxes, logits):

            box = box * torch.tensor([w, h, w, h])
            box = box.int().cpu().numpy()

            x1, y1, x2, y2 = box
            confidence = float(logit)

            detections.append({
                "confidence": confidence,
                "bbox": [int(x1), int(y1), int(x2), int(y2)]
            })

            cv2.rectangle(frame, (x1, y1), (x2, y2),
                          (0, 255, 0), 2)

            cv2.putText(frame,
                        f"Green Crab {confidence:.2f}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2)

        annotated_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.image_pub.publish(annotated_msg)

        detection_msg = String()
        detection_msg.data = json.dumps(detections)
        self.detection_pub.publish(detection_msg)


def main(args=None):
    rclpy.init(args=args)
    node = GreenCrabDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()