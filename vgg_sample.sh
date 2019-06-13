

#bash vgg_sample.sh [work_name] [train_num] [n-th layer] [detector]
echo examples/sample.py -p ~/sample_$1/dataset -n tuned-vgg16-$2 -l $3 -d $4 -f examples/hist/$1_$2_$3_$4
python examples/sample.py -p ~/sample_$1/dataset -n tuned-vgg16-$2 -l $3 -d $4 -f examples/hist/$1_$2_$3_$4
