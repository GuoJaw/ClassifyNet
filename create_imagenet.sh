EXAMPLE=lmdb     #这里修改为自己的路径
DATA=EyeData          #  修改为自己的路径
TOOLS=../build/tools
 
TRAIN_DATA_ROOT=/home/gjw/caffe-ssd-mobile/guojawNet/EyeData/train/     # 修改为自己的路径
VAL_DATA_ROOT=/home/gjw/caffe-ssd-mobile/guojawNet/EyeData/val/         #修改为自己的路径
 

RESIZE=true             
if $RESIZE; then
  RESIZE_HEIGHT=39
  RESIZE_WIDTH=39
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

echo "Creating train lmdb..."
 
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $TRAIN_DATA_ROOT \
    $DATA/train.txt \
    $EXAMPLE/train_lmdb      #把这里改成自己命名的数据库
 
echo "Creating val lmdb..."
 
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $VAL_DATA_ROOT \
    $DATA/val.txt \
    $EXAMPLE/val_lmdb    #这里也改一下
