# ApacheThrift

This repo contains tutorial files for using Apache Thrift.

## Introduction
Coming Soon

## Tutorial
1. Download a copy of Thrift, found [here](https://thrift.apache.org)

2. Follow the install guides found [here](https://thrift.apache.org/docs/install/)

3. Write a thrift file defining an interface for your service.  See `bank.thrift` for an example.
  * The Thrift interface description language can be found [here](http://thrift.apache.org/docs/idl)
  * The Thrift type desction can be found [here](http://thrift.apache.org/docs/types)

4. Write a server file and handler to perform the functions defined in your `.thrift` file.  See `JavaServer.java` and `BankHandler.java` for examples of a server and handler respectively.

5. Write a client to interface with your server.  See `PythonClient.py` for an example.

6. The Thrift compiler is used to generate your Thrift file into source code which is used by the different client libraries and the server you write. To generate the source from a Thrift file run
`thrift --gen <language> <Thrift filename>`

7. Start server application and test with client.

8. DONE!
---
Made for OSU CSE 5914 tech teams.
