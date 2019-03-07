import caffe
import sys
import numpy as np
 
caffe_root='/home/gjw/caffe-ssd-mobile/'
sys.path.insert(0,caffe_root+'python')
 
caffe.set_mode_gpu()
 
deploy='../deploy.prototxt'
caffe_model='../snapshot/caffe_GuojawNet__iter_1000.caffemodel'

labels_name='labels.txt'
mean_file='mean.npy'

imagefile = '/home/gjw/data/EyeData/train/1/'
img=imagefile+'1393.jpg'

net=caffe.Net(deploy,caffe_model,caffe.TEST)
 
transformer=caffe.io.Transformer({'data':net.blobs['data'].data.shape})
transformer.set_transpose('data',(2,0,1))
transformer.set_mean('data',np.load(mean_file).mean(1).mean(1))
transformer.set_raw_scale('data',255)
transformer.set_channel_swap('data',(2,1,0))
 
image=caffe.io.load_image(img)
net.blobs['data'].data[...]=transformer.preprocess('data',image)
 
out=net.forward()
labels=np.loadtxt(labels_name,str,delimiter='\t')
 
prob=net.blobs['prob'].data[0].flatten()
top_k=net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
for i in np.arange(top_k.size):
    print top_k[i],labels[top_k[i]],prob[top_k[i]]
