import towhee
from data import source
from db import create_milvus_collection
collection = create_milvus_collection('reverse_image_search', 2048)

dc = (
    towhee.read_csv(source)
      .runas_op['id', 'id'](func=lambda x: int(x))
      .image_decode['path', 'img']()
      .image_embedding.timm['img', 'vec'](model_name='resnet50')
      .to_milvus['id', 'vec'](collection=collection, batch=100)
)
print('Total number of inserted data is {}.'.format(collection.num_entities))
