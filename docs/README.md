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

***

## 3. Node Setup

<b> Step 1: </b>

On your nodes create a ```/mydata``` directory.

***

<b> Step 2: </b>

On your nodes create a directory with a name of your choice.

Use ```cd``` to go into the newly created directory.

Clone our repo with,

```git clone https://github.com/manticorevenom/cs-5914-wsc```

***

<b> Step 3: </b>

For each node in your 3 node cluster, copy the ```node().tar.gz``` ,where the ```()``` corresponds to the node number, to the correct node in the ```/mydata``` directory.

For instance, the ```node0.tar.gz``` would be copied to ```node0``` on the cluster in the ```/mydata``` directory.

```Note:``` It is recommended that you choose a single node to have the cloned repo and use ```scp``` to copy the files to the correct location on the other nodes.

***

<b> Step 4: </b>

Now unpack the ```.tar.gz``` that you copied to your nodes with,

```tar -zxvf <name_of_file>```

***

<b> Step 5: </b>

Move the contents to your directory and delete the other directory with these commands.

```cp -R ./mydata/ ./```

```rm -drf ./mydata```

```Note:``` You are NOT removing the ```/mydata``` directory that you created. You are removing the ```/mydata``` directory that came from the ```.tar.gz```

***

<b> Step 6: </b>

On each node

Edit the ```main_node_setup.sh```, edit the ```Count52``` to be the name of your CloudLab user. Then edit the ```VTCS-5914``` group to be the name of your CloudLab group/project.

***

<b> Step 7: </b>

On each node

Run the ```main_node_setup.sh``` with,

```bash main_node_setup.sh```

***

<b> Step 8: </b>

On each node

After the ```main_node_setup.sh``` has finished.

Remove the ```namenode/``` and the ```datanode/``` directories in the ```/mydata``` directory.

```rm -drf namenode/```

```rm -drf datanode/```

***

<b> Step 9: </b>

On each node

Re-create the ```namenode/``` and the ```datanode/``` directories in the ```/mydata``` directory.

```mkdir namenode```

```mkdir datanode```

***

<b> Step 10: </b>

On your ```node0```

Install remaining dependencies.

```pip install -r requirements.txt```

***

<b> Step 11: </b>

On your ```node0```

Add dependencies to ```~/.bashrc```

Edit the ```~/.bashrc``` and add the following lines.

```export xx```
```export xx```

Now do the following command,

```source ~/.bashrc```

***

<b> Step 12: </b>

Start HDFS,

First format the namenode directory with,

```/mydata/hadoop/bin/hdfs namenode -format```

Now start HDFS and YARN with the following commands,

```/mydata/hadoop/sbin/start-dfs.sh```

```/mydata/hadoop/sbin/start-yarn.sh```

***

<b> Step 13: </b>

Start Spark with the follwing command,

```/mydata/spark/sbin/start-all.sh```

***

## 4. Starting the Experiment

# 4a. Preparing the Data
The first step starting the experiment is cleaning all of the data. To clean the airline data, execute all the cells of clean.ipynb located in the cs-5914-wsc/flight-delay-model/data/ directory. You will have to do repeat this for each of the files in the dirty data folder so each month. The only thing you should have to change is the variable filename. The purpose of clean.ipynb is to remove any extraneous data so the combined file of each of the months is not very large. 

Once you have cleaned the airline data, each of the months new csv files will be in a folder called "less dirty". Now, using combining_csv.ipynb located in the same spot of as the clean.ipynb file, execute all the cells. This will combine all of the cleaned csv files into one big csv file called full.csv.

Now, you need to clean the weather data to prepare to merge with the airline data. For this step, simply run clean_weather.ipynb andit should create a csv in /data/clean.

Next, you must perform the feature engineering using the file preprocessing.ipynb located in the same directory as the others. Follow the instructions in this file for running this file. You will have to run it two times. The first time it will create a file in the clean directory called clean_merge_full.csv which ccontains all the airline data with new features joined with the weather data by date. The second time you run this, you want to change the file name to clean_full.csv and make sure it is the airline data not joined with the weather data.

Finally, you are ready to train the models. 

# 4b. Training the Models
The hard part was cleaning the data. All you have to do is run all the cells in models.ipynb located in cs-5914-wsc/flight-delay-model/. Depending on the specs of your machine, you may have to adjust the memory given to the spark app. On the cluster we used, it took approximately 3-4 hours.

***

## 5. Conclusion

We tried to thoroughly and comprehensively document the steps we took to setup the environment and train the models. Issues may arise when following our setup or when training the models. We suggest that for Spark or Hadoop related issues that you follow official guidelines.
