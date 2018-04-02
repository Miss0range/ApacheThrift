# ApacheThrift

This repo contains tutorial files for using Apache Thrift.

## Introduction
Coming Soon

## Tutorial
1. Download a copy of Thrift, found [here](https://thift.apache.org)

2. Follow the install guides found [here](https://thrift.apache.org/docs/install/)

3. Write a thrift file, defining an interface for your service.  See `bank.thrift` for an example.

4. Write a server file and handler to perform the functions defined in your `.thrift` file.  See `JavaServer.java` and `BankHandler.java` for examples of a server and handler respectively.

5. Write a client to interface with your server.  See `PythonClient.py` for an example.

6. The Thrift compiler is used to generate your Thrift file into source code which is used by the different client libraries and the server you write. To generate the source from a Thrift file run
`thrift --gen <language> <Thrift filename>`

Made for OSU CSE 5914 tech teams.
