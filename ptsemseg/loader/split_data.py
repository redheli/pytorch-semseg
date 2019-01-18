import sys
from shutil import copyfile

print(sys.argv)

file = sys.argv[1]

input_data = '/media/max/DATA/camvid/701_StillsRaw_full/'
annotation_data = '/media/max/DATA/camvid/LabeledApproved_full/'

dst_path_train = '/media/max/DATA/camvid/train/'

with open(file, "r") as ins:
    for line in ins:
        print('line:', line)
        input_anno = line.split()
        print('input: ',input_anno[0])
        # copy input to train folder
        src = input_data +'/'+ input_anno[0]
        dst =
        copyfile(src, dst)
