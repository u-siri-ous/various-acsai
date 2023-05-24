from torchvision.datasets import ImageFolder

# this works like a dataloader
'''
suppose:
root/dog/1.png
root/dog/2.png
....
root/cat/1.png
root/cat/2.png
...

ImageFolder needs a root, and it gets all the folders as labels and associates it to the files (che figata)
'''