""" train - 60%, val - 10%, test - 30%"""
import  os

classes = ['fish', 'salamander', 'spider', 'frog', 'snake', 'scorpion', 'coala', 'dog', 'snail', 'fly']

os.chdir('../sample')

path_to_train = '/home/data-scientist/PycharmProjects/finetune_alexnet_with_tensorflow/tables/train.txt'
path_to_val =  '/home/data-scientist/PycharmProjects/finetune_alexnet_with_tensorflow/tables/val.txt'
path_to_test = '/home/data-scientist/PycharmProjects/finetune_alexnet_with_tensorflow/tables/test.txt'

for dir in os.listdir():
    paths_to_img_files = list(map(lambda x:  os.path.join('sample',os.path.join(dir,x)), os.listdir(dir)))

    dir_size = len(paths_to_img_files)
    train_size = int(dir_size * 0.6)
    val_size = int(train_size * 0.5)
    test_size = dir_size - train_size - val_size

    with open(path_to_train, 'a') as f:
        for i in range(train_size):
            f.write(paths_to_img_files[i] + ' ' + str(classes.index(dir)) + '\n')

    with open(path_to_val, 'a') as f:
        for i in range(train_size, dir_size - val_size):
            f.write(paths_to_img_files[i] + ' ' + str(classes.index(dir)) + '\n')

    with open(path_to_test, 'a') as f:
        for i in range(dir_size - val_size, dir_size):
            f.write(paths_to_img_files[i] + ' ' + str(classes.index(dir)) + '\n')
