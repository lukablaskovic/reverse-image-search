import towhee
from data import source
from db import create_milvus_collection

collection = create_milvus_collection('reverse_image_search', 2048)

dc = (
    towhee.read_csv(source)
      #for each row from the data, convert the data type of the column id from str to int
      .runas_op['id', 'id'](func=lambda x: int(x))
      #for each row from the data, read and decode the image at path and put the pixel data into column img
      .image_decode['path', 'img']()
      #extract embedding feature with image_embedding.timm, an operator from the Towhee hub
      .image_embedding.timm['img', 'vec'](model_name='resnet50')
      #insert image embedding features in to Milvus
      .to_milvus['id', 'vec'](collection=collection, batch=100)
)

print('Total number of inserted data is {}.'.format(collection.num_entities))
