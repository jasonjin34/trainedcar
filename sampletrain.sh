#!/bin/bash

opencv_createsamples -info cars.info -num 8694 -w 48 -h 24 -vec cars.vec

opencv_traincascade -data data -vec cars.vec -bg bg.txt -numPos 6000 -numNeg 514 -numStages 20 -w 48 -h 24 -featureType LBP
