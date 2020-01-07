## HOW TO USE
* OBS: for run this application you need install `Docker` before;
### To build and run 
* docker build -t `container` .
* docker run --rm -v "`${PATH}`":/app -it `container` python3 /app/`file.py`
### To run [Jupyter Notebook](https://jupyter.org/)
With one file in the root folder called `Notebook.ipynb`, with a few lines for image analysis, and if you want to work on other things just create a new file or edit it.
* docker run -p 8888:8888 `container`