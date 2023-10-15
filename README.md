# YOLOv5环境配置
## 安装anaconda
首先需要安装anaconda的python环境，它可以在做不同项目的时候，可以使用不同的python环境，灵活性很高，必须得配置，以下是安装anaconda的方法，点击[这里](https://blog.csdn.net/HowieXue/article/details/118442904)
进入anaconda环境后，你的终端前面有base的字样，那么证明你以及成功安装anaconda了
## 配置yolov5环境
### 创建python环境
首先先确终端左边是否有base，在有的情况下，执行以下指令来创建一个python环境,python版本一定要注意，这个是3.8的版本，这个决定了你安装有cuda的pytorch的版本
```
conda create -n yolov5 python=3.8
```
然后激活该环境
```
conda activate yolov5
```
你会看到终端右边的base切换为了yolov5的字样，说明你激活环境成功，下面的操作，必须在该环境下进行
### 安装pytorch
#### cpu
如果你没有显卡，那么请安装cpu版本的pytorch
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
#### gpu
如果你有NVIDIA显卡，那么请安装gpu版本的pytorch，gpu版本的torch有加速的效果，当然安装cpu版本的也能用，不过训练模型的时候，切记，一定要用gpu训练，cpu没法玩，训练的速度很慢很慢，不过推理模型的时候，他们之间的速度差距没那么离谱

首先需要安装cuda和cudnn，具体安装方法请点击 [这里](https://blog.csdn.net/qq_41664447/article/details/126914446)

如果用pip下载的话，可能会很慢，建议去[这里](https://download.pytorch.org/whl/torch_stable.html)下载包,注意看清楚版本，比如torch与torchvision之间版本的关系，cuda与pytorch之间版本的关系，python版本，linux与windows的版本

### 安装其他环境
首先是到myyolov5路径里面
```
cd myyolov5
```
然后用pip安装
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
要是报错的话，把清华源删除
## 修改报错
这里有一些anaconda与pytorch兼容问题的报错，因此要修改pytorch环境里面的东西
具体修改方法请参照[这里](https://blog.csdn.net/Thebest_jack/article/details/124723687)

# YOLOv5使用教程
## 训练模型方法
首先是标注图像，这里我建议新手直接用网站标注了，这个标注网站在[这里](https://www.makesense.ai/)
使用方法在[这里](https://blog.csdn.net/weixin_45192980/article/details/119338209)
记得这里一定得导出yolo格式的数据集,现在你的数据集有两个，一个是图像，另外一个是通过标注生成的.txt文件
然后把图像放入以下路径
```
cd myyolov5/mydata/images/train
```
再把.txt的所有文件放入到以下路径
```
cd myyolov5/mydata/labels/train
```
再到以下路径，修改一个.yaml文件
```
cd myyolov5/data
```

这个路径下有我写的mydata.yaml文件，打开它，修改里面的参数，只需要修改nc以及names,nc是你标注图像有多少个类别,names是你标注图像类的名字,把这些弄完，就可以开始训练了，到myyolov5的路径下，执行以下指令
```
python train.py
```
我设置的训练次数是500次，大概要花几个小时的样子
训练好的模型路径在myyolov5/runs/train里面
## 使用模型方法
首先使用官方模型推理，看看能不能用
```
python detect.py --weights yolov5s.pt --source 0
```
weights后面的参数是模型的相对路径,source后面可以填摄像头的地址，图片，视频的相对路径,因此在把yolov5s.pt换成你训练好的模型的相对路径能使用了，推理好的图片或者视频都保留在了myyolov5/runs/detect里面
