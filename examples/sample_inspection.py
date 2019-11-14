import os
from datetime import datetime
from shutil import move, copy2
import imageio
from module.novelty_detector import NoveltyDetector
import argparse

class TrimmingData():
    def __init__(self, position: tuple, size: tuple, needs_trimming: bool):
        self.position = position
        self.size = size
        self.needs_trimming = needs_trimming

original_image_path = 'testimages/campbelle/test/NG/Campbell-Soup-Shop-456x456.jpg'
_, ext = os.path.splitext(original_image_path)
timestamp = str(datetime.now().isoformat()).replace(':', '-')
file_name = f'camera_0_{timestamp}{ext}'
copied_image_path = os.path.join(os.path.dirname(__file__), 'tmp', file_name)
copy2(original_image_path, copied_image_path)

image_paths = [copied_image_path]
image_path = image_paths[0]

# 仮の値
position = (0, 0)
size = (250, 300)
needs_trimming = True

trimming_data = TrimmingData(position, size, needs_trimming)
# truncated_image_path = Dataset.trim_image(image_path, os.path.dirname(image_path), trimming_data)

path = image_path
save_path = os.path.dirname(image_path)
data = trimming_data

try:
    img = imageio.imread(path)
except:
    truncated_image_path = path
file_name = os.path.basename(path)
position = data.position
size = data.size
rect = img[int(position[1]):int(position[1]) + size[1], int(position[0]):int(position[0]) + size[0]]
imageio.imwrite(os.path.join(save_path, file_name), rect)

__model = NoveltyDetector()
def predict(image_paths):
    return __model.predict_paths(image_paths)

__model.load("sample.joblib")

scores = predict(image_paths)

# 仮
threshold = -0.5

if scores >= threshold:
    print('良品です')
    print(scores)
else:
    print('不良品です')
    print(scores)








# truncated_image_path = Dataset.trim_image(image_path, os.path.dirname(image_path), trimming_data)
# # if truncated_image_path:
# #     return truncated_image_path
# # self.predicting_start.emit()
# # predict_thread = threading.Thread(target=self.predict, args=([image_paths]))
# # predict_thread.start()
# # return

# path = self.learning_model.start_predict([copied_image_path])
# if path:
#     self.alert_for_truncated_image(original_image_path)
#     return

