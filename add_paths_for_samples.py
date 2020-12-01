import  os

classes = ['bee', 'wasp']

path_to_train = './tables/train.txt'
path_to_val = './tables/val.txt'
path_to_test = './tables/test.txt'

if __name__ == '__main__':
    for dir in os.listdir('sample'):
        paths_to_img_files = list(map(lambda x:  os.path.join('sample',os.path.join(dir,x)), os.listdir(os.path.join('sample',dir))))

        dir_size = len(paths_to_img_files)
        train_size = int(dir_size * 0.6)
        val_size = int(train_size * 0.5)
        test_size = dir_size - train_size - val_size

        with open(path_to_train, 'w') as f:
            for i in range(train_size):
                f.write(paths_to_img_files[i] + ' ' + str(classes.index(dir)) + '\n')

        with open(path_to_val, 'w') as f:
            for i in range(train_size, dir_size - val_size):
                f.write(paths_to_img_files[i] + ' ' + str(classes.index(dir)) + '\n')

        with open(path_to_test, 'w') as f:
            for i in range(dir_size - val_size, dir_size):
                f.write(paths_to_img_files[i] + ' ' + str(classes.index(dir)) + '\n')
