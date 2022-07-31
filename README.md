# "reverse-image-search"

Reverse image search using Milvus.io and Towhee.io. Undergraduate thesis, Faculty of informatics in Pula.

### Author

-   Luka Blašković (lblaskovi@unipu.hr)

### Short description
Vector databases are used to store unstructured data such as images, videos, music, sensor data, and so on. Before importing the data into the Milvus database, it first has to be encoded into vector embeddings using towhee.io. An “embedding” vector is a numeric representation of unstructured data, images in this case. Embedding vectors are then loaded into Milvus database. Milvus supports different types of similarity metrics and indexes for different use cases. Here, we will use L2 euclidian distance metric and IVF_FLAT index. Application can be tested using Gradio web interface which runs from build.ipynb file.

### Tools used
- [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
- [Milvus.io](https://milvus.io/)
- [Towhee.io](https://towhee.io/)
- [Jupyter notebook](https://jupyter.org/)

### Organization

[Sveučilište Jurja Dobrile u Puli](http://www.unipu.hr/)  
[Fakultet informatike u Puli](https://fipu.unipu.hr/)  
Undergraduate thesis - Vector databases for unstructured data processing, 2021./2022.  
Course: **Databases II**  
Mentor: **doc. dr. sc. Goran Oreški** (https://fipu.unipu.hr/fipu/goran.oreski, goran.oreski@unipu.hr)

### Dependencies

```python
! python -m pip install -q pymilvus towhee gradio opencv-python pillow pyarrow
```
### Dataset

```
curl -L https://github.com/towhee-io/examples/releases/download/data/reverse_image_search.zip -O
```
