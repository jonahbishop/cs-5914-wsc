# Flight Delay Predicition with TensorFlowOnSpark

```
Virginia Tech Computer Science
CS 5914
Special Topics - Warehouse Scale Computing
Group WSS
Jonah Bishop, Hunter Leary, Nicholas Raines
```

***

## 1. Introduction

We decided to do research on flight delay prediction using machine learning. From our brief literature review on this topic, we found that some existing papers use a compromising feature set. For example, in one of the papers we examined they used a feature set that included whether the flight was delayed or not. Also, we found that some papers did not use weather data while training their models. Our discoveries made us want to dig deeper on this topic.

***

## 2. Project Outline

The project was to train two models. One model with use the flight data exclusively, the other model will use the flight data and weather data.

To train our models we decided to use TensorFlowOnSpark.

We wanted to use a cluster of devices running Hadoop and Spark and our models to be deep learning models. TensorFlowOnSpark allowed us to meet these requirements.

After the models we trained, we evaluated the models with ...

***

## 3. Project Setup

We used CloudLab.us for the cluster of devices. The cluster consisted of 3 Ubuntu 20.04 nodes connected in a small lan topology. We used our own profile to instantiate the experiment so that we could have data persistence across our experiments. The profile is under the ```/cloud-lab-profile``` directory. For the specific versions and dependencies, see ```SETUP.md``` under the ```/docs``` directory. Hadoop 3.3.4 was used. Spark 3.3.0 was used. TensorFlowOnSpark 2.2.5 was used. Python 3.8.1 was used.

***

## Instructions

All of the source code files have been added to this repo. If you would like to replicate this project, we suggest that you use CloudLab.us as it will be closest to the original project and this approach will be the easiest. We have provided instructions for the CloudLab.us approach, see ```SETUP.md``` under the ```/docs``` directory.

However, if you decide not to use CloudLab.us you should still be able to replicate this project though this approach will be more difficult. We have not provided instructions for this approach.

***

## Conclusion

We evaluated the two models and found that ...
