
import caffe
import sys
import numpy as np
 
caffe_root='/home/gjw/caffe-ssd-mobile/'
sys.path.insert(0,caffe_root+'python')
 
caffe.set_mode_gpu()

import caffe
import numpy as np
 
proto_path='../mean.binaryproto'
npy_path='mean.npy'
 
blob=caffe.proto.caffe_pb2.BlobProto()
data=open(proto_path,'rb').read()
blob.ParseFromString(data)
 
array=np.array(caffe.io.blobproto_to_array(blob))
mean_npy=array[0]
np.save(npy_path,mean_npy)
