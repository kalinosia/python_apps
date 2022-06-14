## Virtual environment

```shell
python -m venv wirtualne
wirtualne\Scripts\activate.bat
```

At the end of work

```bash
deactivate

```


### Remove background 

1. Create folder to your project
2. Download file "remove_background.py"
3. Bring your picture/s to this folder
4. Rund comand line in this folder


>PixelLib supports tensorflow's version (2.0 - 2.4.1)
>To check your verson `$pip show tensorflow` so no to `$pip install --upgrade tensorflow`
>TensorFlow v2.1 is not compatibile with Python >3.8 (...)



```
python -m venv wirtualne
wirtualne\Scripts\activate.bat
pip install pixellib
pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl

```
go to ...\python_apps\wirtualne\Lib\site-packages\pixellib\semantic
Go to Pixellib folder -> semantic -> deeplab.py and replace this line from tensorflow.python.keras.layers import BatchNormalization with this one from keras.layers.normalization.batch_normalization import BatchNormalization

```
python remove_background.py

```