
《《 训练过程 》》

1、准备数据集，放入EyeData/train、EyeData/val中，目录结构：

	EyeData/
		  train/		  
			     0/
			     1/
		  val/
		  	     0/
			     1/
      说明：0、1目录下分别存放着0类、1类的图像
	
2、制作train.txt和val.txt，如：train.txt内容

	  1/1429.jpg 1
   	  1/1430.jpg 1

	  0/1491.jpg 0
	  0/1435.jpg 0
       格式为：  目录/图片名.jpg  目录
       
3、执行create_bin.sh生成均值文件mean.binaryproto

4、执行create_lmdb.sh生成lmdb文件

5、执行train.sh开始训练，生成的caffemodel存放在snapshot下


《《 测试单张图像过程 》》

1、进入“测试”目录

2、新建label.txt

3、执行npy.py生成mean.npy

4、执行test.py测试单张图像

