# Installation 
## Install Erlang
```
sudo apt install erlang
```

## Install RabbitMQ Server Ubuntu
```
sudo apt install rabbitmq-server
```

# Rabbitmq
RabbitMQ is a message-queueing software also known as a message broker or queue manager. Simply said; it is software where queues are defined, to which applications connect in order to transfer a message or messages.

![0](images/0.png)

A message can include any kind of information. It could, for example, have information about a process or task that should start on another application (which could even be on another server), or it could be just a simple text message. The queue-manager software stores the messages until a receiving application connects and takes a message off the queue. The receiving application then processes the message. 

## RabbitMQ Example

A message broker acts as a middleman for various services (e.g. a web application, as in this example). They can be used to reduce loads and delivery times of web application servers by delegating tasks that would normally take up a lot of time or resources to a third party that has no other job.

In this guide, we follow a scenario where a web application allows users to upload information to a website. The site will handle this information, generate a PDF, and email it back to the user. Handling the information, generating the PDF, and sending the email will, in this example case, take several seconds. That is one of the reasons why a message queue will be used to perform the task.

When the user has entered user information into the web interface, the web application will create a "PDF processing" message that includes all of the important information the user needs into a message and place it onto a queue defined in RabbitMQ. 

![1](images/1.png)
![2](images/2.png)

The basic architecture of a message queue is simple - there are client applications called producers that create messages and deliver them to the broker (the message queue). Other applications, called consumers, connect to the queue and subscribe to the messages to be processed. Software may act as a producer, or consumer, or both a consumer and a producer of messages. Messages placed onto the queue are stored until the consumer retrieves them. 

## When and why should you use RabbitMQ?

Message queueing allows web servers to respond to requests quickly instead of being forced to perform resource-heavy procedures on the spot that may delay response time. Message queueing is also good when you want to distribute a message to multiple consumers or to balance loads between workers.

The consumer takes a message off the queue and starts processing the PDF. At the same time, the producer is queueing up new messages. The consumer can be on a totally different server than the producer or they can be located on the same server. The request can be created in one programming language and handled in another programming language. The point is, the two applications will only communicate through the messages they are sending to each other, which means the sender and receiver have low coupling. 

![3](images/3_new.png)

1. The user sends a PDF creation request to the web application.
2. The web application (the producer) sends a message to RabbitMQ that includes data from the request such as name and email.
3. An exchange accepts the messages from the producer and routes them to correct message queues for PDF creation.
4. The PDF processing worker (the consumer) receives the task message and starts processing the PDF.

## Exchanges

Messages are not published directly to a queue; instead, the producer sends messages to an exchange. An exchange is responsible for routing the messages to different queues with the help of bindings and routing keys. A binding is a link between a queue and an exchange. 

![4](images/4.png)


## Message flow in RabbitMQ

1. The producer publishes a message to an exchange. When creating an exchange, the type must be specified. This topic will be covered later on.
2. The exchange receives the message and is now responsible for routing the message. The exchange takes different message attributes into account, such as the routing key, depending on the exchange type.
3. Bindings must be created from the exchange to queues. 
4. In this case, there are two bindings to two different queues from the exchange. The exchange routes the message into the queues depending on message attributes.
The messages stay in the queue until they are handled by a consumer
5. The consumer handles the message.

## Types of exchanges 

![5](images/5.png)


Direct: The message is routed to the queues whose binding key exactly matches the routing key of the message. For example, if the queue is bound to the exchange with the binding key pdfprocess, a message published to the exchange with a routing key pdfprocess is routed to that queue.

![6](images/6.png)

Fanout: A fanout exchange routes messages to all of the queues bound to it.

![7](images/7.png)

Topic: The topic exchange does a wildcard match between the routing key and the routing pattern specified in the binding.

![8](images/8.png)

Headers: Headers exchanges use the message header attributes for routing.

![9](images/9.png)


## RabbitMQ and server concepts

Some important concepts need to be described before we dig deeper into RabbitMQ. The default virtual host, the default user, and the default permissions are used in the examples, so let’s go over the elements and concepts:

* Producer: Application that sends the messages.

* Consumer: Application that receives the messages.

* Queue: Buffer that stores messages.

* Message: Information that is sent from the producer to a consumer through RabbitMQ.

* Connection: A TCP connection between your application and the RabbitMQ broker.

* Channel: A virtual connection inside a connection. When publishing or consuming messages from a queue - it's all done over a channel.

![10](images/10.png)

![11](images/11.png)

* Exchange: Receives messages from producers and pushes them to queues depending on rules defined by the exchange type. To receive messages, a queue needs to be bound to at least one exchange.

* Binding: A binding is a link between a queue and an exchange.

* Routing key: A key that the exchange looks at to decide how to route the message to queues. Think of the routing key like an address for the message.

* AMQP: Advanced Message Queuing Protocol is the protocol used by RabbitMQ for messaging. 

* Users: It is possible to connect to RabbitMQ with a given username and password. Every user can be assigned permissions such as rights to read, write and configure privileges within the instance. Users can also be assigned permissions for specific virtual hosts.

* Vhost, virtual host: Provides a way to segregate applications using the same RabbitMQ instance. Different users can have different permissions to different vhost and queues and exchanges can be created, so they only exist in one vhost. 
