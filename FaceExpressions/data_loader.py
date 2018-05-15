from torch.utils.data import Dataset, DataLoader
from os import listdir
from os.path import join
from PIL import Image
import numpy as np
from os.path import exists

# folders
CK_plus = './data/CKplus/'
# X
IMAGES = 'cohn-kanade-images/'  # (11, 490, 640)
# Y
EMOTION = 'Emotion/'        # 1 to 9  -> (categorical)
FACS = 'FACS/'              # 1 to 43 -> (categorical)
LANDMARKS = 'Landmarks/'    # (11, 68, 2)


# Load images sequence
def load_images_sequence(folder):
    return np.array([np.array(Image.open(join(CK_plus, IMAGES, folder, img))) for img in listdir(join(CK_plus, IMAGES, folder))], dtype=np.float64)


# Load landsmark sequence
def load_landmarks_sequence(folder):
    return np.array([read_points_txt(join(CK_plus, LANDMARKS, folder, landmark)) for landmark in listdir(join(CK_plus, LANDMARKS, folder))])


# Load Facs
def load_facs(folder):
    return np.array([read_points_txt(join(CK_plus, FACS, folder, facs)) for facs in listdir(join(CK_plus, FACS, folder))])


# Load Emotion
def load_emotion(folder):
    if listdir(join(CK_plus, EMOTION, folder)):
        return np.array([read_emotion_txt(join(CK_plus, EMOTION, folder, emotion)) for emotion in listdir(join(CK_plus, EMOTION, folder))])
    else:
        return np.zeros((1,), dtype=np.float64)


# read points from txt
def read_points_txt(file):
    with open(file, 'r') as f:
        points = [np.array(point.split(), dtype=np.float64) for point in f.read().split('\n')]
        return np.concatenate(points).reshape(len(points) - 1, 2)


# read emotion from txt
def read_emotion_txt(file):
    with open(file, 'r') as f:
        return np.array(f.read(), dtype=np.float64)


class EmotionsData(Dataset):
    def __init__(self):
        super(EmotionsData, self).__init__()
        # create indexes dictionary
        self.index = dict()
        idx = 0
        for person in listdir(join(CK_plus, IMAGES)):
            for expression in listdir(join(CK_plus, IMAGES, person)):
                if expression is ".DS_Store":
                    continue
                self.index[idx] = join(person, expression)
                idx += 1

    def __getitem__(self, index):
        folder = self.index[index]
        images = load_images_sequence(folder)
        landmarks = load_landmarks_sequence(folder)
        facs = load_facs(folder)
        emotion = load_emotion(folder)
        return (images, landmarks, facs, emotion)

    def __len__(self):
        return len(self.index)
