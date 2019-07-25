import argparse
import time

import cv2
import numpy as np
from PIL import Image

from yolo_counting import YOLO, detect_video
from centroidtracker import CentroidTracker
from trackableobject import TrackableObject
from model import yolo_eval, yolo_body, tiny_yolo_body
from utils import letterbox_image


def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image, box = yolo.detect_image(image)
            # r_image.show()
            r_image = np.asarray(r_image)
            cv2.imwrite('image_output/image.jpg', r_image)
    yolo.close_session()


FLAGS = None

if __name__ == '__main__':

    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )

    parser.add_argument(
        "--input", nargs='?', type=str, required=False, default='./path2your_video',
        help="Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="",
        help="[Optional] Video output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:

        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)))

    elif "input" in FLAGS:

        start = time.time()

        detect_video(YOLO(**vars(FLAGS)), FLAGS.input)
        duration = time.time() - start
    # print('duration:' + str(duration))
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
