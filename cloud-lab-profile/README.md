# CloudLab Setup

```
Hunter Leary
2022.11.20
```

## 1. Description

The CloudLab profile is a modified version of the ```small-lan``` profile that CloudLab users will have access to.
The profile leverages CloudLabs image-backed datasets for data persistence from experiment to experiment.

***

## 2. Usage

***

### 2.1 First Setup

First, start a CloudLab experiment using the ```small-lan``` experiment. Enter ```3``` for the ```Number of Nodes```. Select ```Ubuntu 20.04``` for ```Select OS Image```. Under ```Temporary Filesystem Size``` enter the size of drive in ```GB```. 

When the experiment is running, go to ```Storage -> Create Datasets```. Select a name that will be memorable with the name of the node appended to the end. For example, ```wss-node0``` is the name of one of our datasets. Under ```Type```, select ```Image backed```. Under ```Instance```, select the running experiment. Under ```Node```, select the node that corresponds to the name of the dataset. For example, ```node0```(name of node in experiment) for ```wss-node0```(name of dataset). Choose permission how you'd prefer and click create. 

After you have create a dataset for each node in the running experiment, you can terminate the running experiment.

***

### 2.2 Core Experiment Setup

Now, we should have ```3``` image backed datasets. Each dataset will have a URN, copy this URN. The URN will be of the form ```urn:publicid:IDN+emulab.net:vtcs-5914+imdataset+wss-node0```. Create a new experiment profile, select ```Edit Code```. Copy the profile, ```profile.py``` in this repo and paste the code into the profile editor on CloudLab.

Modify the ```urn``` line from this code snippet from ```profile.py```,

```
    if params.tempFileSystemSize > 0 or params.tempFileSystemMax:
        bs = node.Blockstore(name + "-bs", params.tempFileSystemMount)
        bs.dataset = 'urn:publicid:IDN+emulab.net:vtcs-5914+imdataset+wss-node' + str(i)
        if params.tempFileSystemMax:
```

Edit this on the CloudLab editor to be,

```
    if params.tempFileSystemSize > 0 or params.tempFileSystemMax:
        bs = node.Blockstore(name + "-bs", params.tempFileSystemMount)
        bs.dataset = 'your_urn_from_your_dataset_for_a_node_without_the_number' + str(i)
        if params.tempFileSystemMax:
```

Choose any name you want and click create.

Now instantiate an experiment with your new profile with the same settings as the 2.1 First Setup.

***

# 3. Node Setup

For each node, copy the corresponding node folder i.e. node0 if the node is node0, into the ```/mydata/``` directory.

After each node has their corresponding folder downloaded, run the ```main_node_setup.sh``` to perform necessary installations/modifications and updates.

After the ```main_node_setup.py``` has finished, follow the ```SETUP.md``` in the ```/docs``` directory.