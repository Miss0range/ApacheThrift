# ApacheThrift

This repo contains tutorial files for using Apache Thrift.

## Introduction
### What is Apache Thrift?
Apache Thrift is an interface definition language and binary communication protocol that is used to define and create services for various languages. In other words, it helps describe a software component’s application programming interface (API) that allows it to communicate with other software components, even if they are not written in the same language. Apache Thrift does this by creating remote procedure call (RPC) clients and servers. A RPC is when a computer program causes a procedure to execute in a different address space. Apache Thrift can provide clean abstractions for data transport, data serialization and application level processing.
Currently, Apache Thrift can connect applications written in 26 languages, including C/C++, C#, Haskell, Java, JavaScript, node.js, Perl, PHP, Python and Ruby. It was originally developed at Facebook, but is now an open source project hosted on Apache.

### Why use Apache Thrift?
At Facebook, Thrift was developed for “scalable cross-language services development”. Compared to other alternatives, such as SOAP, Apache Thrift has a lower overhead for cross-language serialization. There is no framework to code or XML configuration files. There are no build dependencies, non-standard software or mix of incompatible software licenses. Additionally, the application-level wire format and the serialization-level wire format are separated so that they can be modified separately. In other words, if you need a lightweight, language-independent way to connect multiple software components, use Apache Thrift.

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
