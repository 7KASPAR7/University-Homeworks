import torch
import torchvision
import torchvision.transforms as transforms
import os
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 29 * 29, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 113)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def get_dataset(data_dir, data_transforms):

    image_datasets = {x: torchvision.datasets.ImageFolder(os.path.join(data_dir, x),
                                                              data_transforms[x])
                        for x in ['train', 'test']}
    dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4,
                                                      shuffle=True, num_workers=4)
                       for x in ['train', 'test']}
    dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'test']}

    classes = image_datasets['train'].classes

    return dataloaders["train"], dataloaders['test'], classes, dataset_sizes

def dir_transforms():

    dir = os.path.abspath(os.curdir)

    data_dir = os.path.join(dir, "quick_draw_subset\\")


    data_transforms = {
        'train': transforms.Compose([
            transforms.RandomResizedCrop(128),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ]),
        'test': transforms.Compose([
            transforms.RandomResizedCrop(128),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ]),
    }
    return data_dir, data_transforms


def imshow(img):
        img = img / 2 + 0.5
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()


def main():
    net = Net()

    data_dir, data_transforms = dir_transforms()

    trainloader, testloader, classes, dataset_sizes = get_dataset(data_dir, data_transforms)
    print(trainloader)
    print('Classes: ', classes)
    print('The datasest have: ', dataset_sizes, " images")

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)



    for epoch in range(80):

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):

            inputs, labels = data

            optimizer.zero_grad()

            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()


            running_loss += loss.item()
            if i % 2000 == 1999:
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    print('Finished Training')

    PATH = './draw_net.pth'
    torch.save(net.state_dict(), PATH)

   # dataiter = iter(testloader)
   # images, labels = dataiter.next()

    # print images
   # imshow(torchvision.utils.make_grid(images))
   # print('GroundTruth: ', ' '.join('%5s' % classes[labels[j]] for j in range(batch_size)))

   # net = Net()
   # net.load_state_dict(torch.load(PATH))

   # outputs = net(images)
   # _, predicted = torch.max(outputs, 1)

   # print('Predicted: ', ' '.join('%5s' % classes[predicted[j]]
     #                             for j in range(batch_size)))

if __name__ == "__main__":
    main()