import imageio.v3 as iio

filenames = ['SG1 (1).png', 'SG1 (2).png', 'SG1 (3).png', 'SG1 (4).png']

images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('SG3.gif', images, duration = 150, loop = 0)