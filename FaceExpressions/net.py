import torch
import torch.nn as nn
from torch.nn import Conv2d, LSTM, Sequential
from torchvision import transforms

'''
X] -> (#SEQ, 490, 640, 1)
Y] ->
        Landmarks (#SEQ, 68, 2)
        facs      (1, 5, 2)
        emo       (1, )

'''


class EmotionsNet(nn.modules):
    def __init__(self):
        super(EmotionsNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=5, padding=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2))

        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=5, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2))

        self.fc = nn.Linear(7 * 7 * 32, 10)

# class EncoderCNN(nn.Module):
#     def __init__(self, embed_size):
#         """Load the pretrained ResNet-50"""
#         super(EncoderCNN, self).__init__()
#         resnet = models.resnet50(pretrained=True)
#         modules = list(resnet.children())[:-1]      # delete the last fc layer.
#         self.resnet = nn.Sequential(*modules)
#
#     def forward(self, sequence_images):
#         features = self.resnet(sequence_images)
#         return features
