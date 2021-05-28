# OEE Solution with Near Real Time Availability and Quality

This is a sample OEE solution to demo the design pattern. Kepware EX Demo Server is used as the OPC UA Server. The Edge Gateway Device is a Windows 10 PC. Both Kepware and Edge Gateway are installed on the same device for simplicity.

## Prerequisites
- Windows 10 PC
- Visual Studio Code
- Azure Subscription
- Azure CLI

## Install and Configure OPC UA Server

    This sample uses the Kepware EX Server but you can use any other test server like the [OPC PLC server](https://github.com/Azure-Samples/iot-edge-opc-plc), [node-red-contrib-opcua](https://flows.nodered.org/node/node-red-contrib-opcua), or others.

- Install [Kepware EX Demo Server](https://www.kepware.com/en-us/products/kepserverex/)
    
- Setup [Kepware OPC UA Configuration](https://www.kepware.com/getattachment/de80e240-765e-451a-afce-640d413891c3/opc-ua-configuration-manager-manual.pdf)

    - Open `OPC UA Configration Manager` in KepWare Administration
    - Make sure `opc.tcp://127.0.0.1:49320` endpoint in Enabled

- Open the Kepware Configuration Manager, and open the [files/FullSimulationDriverDemo.json](files/FullSimulationDriverDemo.json)
    - This file contains a new Channel configuration named `OEESample` with 3 tags


## Create and Configure Azure IoT Hub

    IoT Hub is used as the cloud gateway to ingest data from multiple OPC Server

- Create IoT Hub (S1 with 400,000 4K messages a day)

- Create a new IoT Edge device and copy the connection string


## Install and Configure IoT Edge

    IoT Edge enables store & forward functionality as well as secure connection between the OPC Server and the cloud gateway

- Install [Docker Desktop](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

- Create new docker network `docker network create azure-iot-edge`

- Install IoT Edge via [IoT Edge Installer](https://github.com/Azure/Industrial-IoT-Gateway-Installer/tree/master/Releases)

- Copy [edge/publishednodes.json](edge/publishednodes.json) file to `C:\IoTEdgeMapping` and update the EndPointUrl if your OPC Server is on a different box.

- Install [OPC Publisher Module](https://github.com/azure/iot-edge-opc-publisher#getting-started) using Azure Portal
  
    - Use [edge/opcpublisher-container-create-options.txt](edge/publisher-container-create-options.txt) file for container create options


- Or you can use the [edge/edgeManifest.json](edge/edgeManifest.json) to create a new edge deployment.

- Open `OPC UA Configration Manager` in KepWare Administration and the IoT Edge certificate to Trusted Client


## Create and Configure Azure Data Explorer

    Data explorer is the near real time big data store to analyze telemetry coming out of the cloud gateway.

- Create Data Explorer Cluster with `Workload` as `Dev/Test` and `Streaming Ingestion` set to `On`

- Add database named `opcdb`

- Add data connection in the database with connection type as `IoT Hub` and select the IoT Hub that we created in the previous step.
    - Shared Access Policy=iothubowner
    - Table name= [Blank]
    - Data format=MULTILINE JSON
    - Mapping name=opcua_mapping

- Open [http://dataexplorer.azure.com/](http://dataexplorer.azure.com/), add you cluster and the [kusto/setup.sql](kusto/setup.kql) script on the opcdb database.

## Create and Configure Azure SQL DB

    SQL DB is used to store the aggregate data for OEE calculation to enable basic reporting

- Create SQL DB and run the [sql/AssetOEE.sql](sql/AssetOEE.sql) script to create the tables


## Create and Configure Azure Function

    Python function app (serverless compute) is used as the on demand compute to run the OEE calculation. The actual calculation code is inside a python package which can be executed in multiple other computes like databricks, synapse spark or even at the edge.

- Open the [function](function) folder and  update the `local.settings.json` file

- Use Visual Studio Code to deploy to Azure

- <TODO...>

## Create and Configure Azure Data Factory

- <TODO...>


## Setup OEE Dashboard

- <TODO...>


## Additional Resources

- [OPC Publisher command line options](https://github.com/Azure/iot-edge-opc-publisher/blob/main/docs/CommandLineArguments.md#opc-publisher-command-line-arguments-for-version-26-and-above)  

- [OPC Publisher nodes template file](https://raw.githubusercontent.com/Azure/iot-edge-opc-publisher/main/opcpublisher/publishednodes.json)