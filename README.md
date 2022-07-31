# "reverse-image-search"

Reverse image search using Milvus.io and Towhee.io. Undergraduate thesis, Faculty of informatics in Pula.

### Author

-   Luka Blašković (lblaskovi@unipu.hr)

### Short description
Vector databases are used to store unstructured data such as images, videos, music, sensor data, and so on. Before importing the data into the Milvus database, it first has to be encoded into vector embeddings using the towhee.io. 

### Tools used
- [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
- [Milvus.io](https://milvus.io/)
- [Towhee.io](https://towhee.io/)
- [Jupyter notebook](https://jupyter.org/)

### Organization

[Sveučilište Jurja Dobrile u Puli](http://www.unipu.hr/)  
[Fakultet informatike u Puli](https://fipu.unipu.hr/)  
Undergraduate thesis - Vector databases for unstructured data processing, 2021./2022.  
Course: **Databases 2**  
Mentor: **Goran Oreški** (https://fipu.unipu.hr/fipu/goran.oreski, goran.oreski@unipu.hr)

### Dependencies

```python
! python -m pip install -q pymilvus towhee gradio opencv-python pillow pyarrow
```
### Dataset

```
curl -L https://github.com/towhee-io/examples/releases/download/data/reverse_image_search.zip -O
```
