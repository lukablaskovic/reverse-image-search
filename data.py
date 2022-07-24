import pandas as pd
import cv2
from towhee._types.image import Image

source = 'D:/data/reverse_image_search.csv'

#Read data
df = pd.read_csv(source)
print(df.head())

#Data preparation
id_img = df.set_index('id')['path'].to_dict()
label_ids = {}
for label in set(df['label']):
    label_ids[label] = list(df[df['label']==label].id)
    
#Helper function
def read_images(results):
    imgs = []
    for re in results:
        path = id_img[re.id]
        imgs.append(Image(cv2.imread(path), 'BGR'))
    return imgs