# Experiment Setup

```
Hunter Leary
2022.11.30
```

***

## 1. Prerequisites

See the ```README.md``` in the ```/cloud-lab-profile``` directory, if following the CloudLab approach before starting this document.

If you are not following the CloudLab approach, continue.

***

## 2. Dependencies

Java: OpenJDK 8

Ubuntu: 20.04

Hadoop: 3.3.4

Spark: 3.3.0

Python: 3.8.10

## 3. Node Setup

<b> Step 1: </b>

***

On your nodes create a ```/mydata``` directory.

<b> Step 2: </b>

***

On your nodes create a directory with a name of your choice.

Use ```cd``` to go into the newly created directory.

Clone our repo with,

```git clone https://github.com/manticorevenom/cs-5914-wsc```

<b> Step 3: </b>

***

For each node in your 3 node cluster, copy the ```node().tar.gz``` ,where the ```()``` corresponds to the node number, to the correct node in the ```/mydata``` directory.

For instance, the ```node0.tar.gz``` would be copied to ```node0``` on the cluster in the ```/mydata``` directory.

```Note:``` It is recommended that you choose a single node to have the cloned repo and use ```scp``` to copy the files to the correct location on the other nodes.

<b> Step 4: </b>

***

Now unpack the ```.tar.gz``` that you copied to your nodes with,

```tar -zxvf <name_of_file>```

<b> Step 5: </b>

***

Move the contents to your directory and delete the other directory with these commands.

```cp -R ./mydata/ ./```

```rm -drf ./mydata```

```Note:``` You are NOT removing the ```/mydata``` directory that you created. You are removing the ```/mydata``` directory that came from the ```.tar.gz```

<b> Step 6: </b>

***

On each node

Edit the ```main_node_setup.sh```, edit the ```Count52``` to be the name of your CloudLab user. Then edit the ```VTCS-5914``` group to be the name of your CloudLab group/project.

<b> Step 7: </b>

***

On each node

Run the ```main_node_setup.sh``` with,

```bash main_node_setup.sh```

<b> Step 8: </b>

***

On each node

After the ```main_node_setup.sh``` has finished.

Remove the ```namenode/``` and the ```datanode/``` directories in the ```/mydata``` directory.

```rm -drf namenode/```

```rm -drf datanode/```

<b> Step 9: </b>

***

On each node

Re-create the ```namenode/``` and the ```datanode/``` directories in the ```/mydata``` directory.

```mkdir namenode```

```mkdir datanode```

<b> Step 10: </b>

***

On your ```node0```

Install remaining dependencies.

```pip install jupyter==1.0.0 pyspark==3.3.0 numpy notebook pyarrow findspark```

<b> Step 11: </b>

***

On your ```node0```

Add dependencies to ```~/.bashrc```

Edit the ```~/.bashrc``` and add the following lines.

```export xx```
```export xx```

Now do the following command,

```source ~/.bashrc```

<b> Step 12: </b>

***

Start HDFS,

First format the namenode directory with,

```/mydata/hadoop/bin/hdfs namenode -format```

Now start HDFS and YARN with the following commands,

```/mydata/hadoop/sbin/start-dfs.sh```

```/mydata/hadoop/sbin/start-yarn.sh```

<b> Step 13: </b>

***

Start Spark with the follwing command,

```/mydata/spark/sbin/start-all.sh```

***

## 4. Starting the Experiment

To train the models do,

```some command here```

***

## 5. Conclusion

We tried to thoroughly and comprehensively document the steps we took to setup the environment and train the models. Issues may arise when following our setup or when training the models. We suggest that for Spark or Hadoop related issues that you follow official guidelines.
