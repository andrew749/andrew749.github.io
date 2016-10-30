---
title: Creating a Distributed Computation System
subtitle: Uses, Pitfalls and Challenges
date: Sunday October 23, 2016
---

If you've been following my GitHub, you would have noticed I've amassed
a healthy number of commits over the last week on a new project aptly named
Distribute. The goal of this project is to provide a proof of concept of
a system which takes advantage of a large number of clients on a particular
website or service, and uses these clients as slave nodes in a giant "cluster"
which can be used to solve computational problems. The idea was taken from
normal map reducing systems, i.e. Hadoop, where normally all the nodes that you
perform operations on owned by you

This idea works particularly well when there isn't too much data to distribute
among the nodes and when the payloads that each node execute is very
computationally intensive (i.e. most of the time is not spend sending the data
to the nodes). In an ideal use case, the server only handles io operations from
the slave nodes, as well as stitching together results from the slave nodes.
Slave nodes can be used for traditional map reduce tasks that don't require too
much communication with the server.

## Challenges

Some of the most notable challenges of this project were managing the locks for
nodes. Node states must be constantly updated, and must never get into a stale
un-synced state. If we send payload data/execution instructions to a node that
does not exist any more, expecting it to return data, we might have an
incomplete result set of data. This problem was tackled by tracking the state
of the browser window, sending events back to the master server in the event of
a disconnection of any sort.

Another challenge which has yet to be solved for this project is that of
monitoring the execution lifecycle and providing status updates for
a particular jobs status. The best solution in my opinion would be to create
some sort of helper method to report status, and leave it up to the person
creating a payload to pepper in these calls with custom status checkpoints.
Since each payload is unique, it doesn't make sense to infer where a program is
in its execution as this would be outright wrong. Certain computations are
inherently more expensive and cannot be accurately estimated. By providing
a status call, the onus is on the user to manage the state reporting of their
program. This solution has the added benefit of allowing a user to provide
custom update messages and to react to certain statuses with possible other
actions (i.e. starting up another pipeline after a certain amount of data has
been processed).

## Potential use cases

Map reduce systems have been traditionally used for tasks that have to operate
on large, easily separable data sets. For example, one might want to access
data from a distributed database and then perform simple aggregation operators
on this. This is a challenge with this system since we first need to determine
a way to send credentials to the child nodes. At the time of this writing,
I don't see a good way of doing this, with the exception of setting up a proxy server which knows about the nodes in the computing cluster and will let each node access data that it has permission to use. This defeats the purpose of the system being able to distribute database queries since there must be a single point through which all data traffic must flow. Separating queries should work as
expected, as long as the specifics of the payload are fully understood (i.e.
the way we send data to a particular variable, as its payload data parameter).

Another use case that I find interesting and much safer and more effective is
to distribute map reduce jobs that are aimed at solving machine learning
problems. Problems such as batch gradient descent can be tackled using a large
number of slave nodes. After the initial transfer of data, models can be trained
to large epochs without any interaction from an external server. Once the model
is trained on a particular set of data, a VERY small result can be sent back to
the master server, thus reducing the amount of io that needs to be done by this
critical keystone.

One last use case that I am hesitant to mention for this distributed computing
system is a botnet. At some point during the development of this project
I realized that this system is pretty much the textbook definition of a botnet:
a master or set of master nodes, sending payloads(potentially malicious) to
a set of client nodes, making these client nodes blindly execute the payload
node. More specifically, this cluster can be used to create DDOS attacks on
certain clients (simply point each client node to make requests to a particular
target). Luckily, cross origin policies help to mitigate this issue by
preventing clients from asking external servers for data.

## Dangers

There are inherent dangers with this project that I should mention. Firstly,
the nodes are trusting of the server. They do not expect the server to be
sending malicious code as they are blindly executing it. This can be extremely
dangerous and can allow for people to setup a MITM attack and pwn these nodes
for their own profit. One solution to this could implementing a key-paid based
system and checking payload hashes with a private key that a client generates.
Similar to handshakes are created in GPG, this system could mitigate attacks by
forcing nodes to authenticate pieces of code that are sent to them.

Another danger of this system is that as of this writing, there is no way to
cancel a job. The system has a semaphore like locking mechanism to prevent
nodes from getting more than one payload. If there is a bug in the payload
(i.e. infinite loop) this will, for all intensive purposes, destroy the node as
it will be blocked indefinitely, or until the user manually kills the node or
refreshes the page. This can be mitigated by doing some analysis of the code
while running and having sane default kill switches which can stop a job after
an exorbitant amount of time.

## Planned improvements

-  Add the ability to analyze a jobs status using custom reporting.
-  Ability to cancel a job.
-  Some sort of higher level language that is more suitable for executing and which prevents dangerous operations.
-  Private-Public key pair generation and code validation.
