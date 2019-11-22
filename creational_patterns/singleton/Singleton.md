# Singleton Design Pattern

## Intent

Ensure a class only has one unique instance, and provide a global point of access to it.

## Motivation

Sometimes it is necessary to have some classes to have an one unique instance. Singleton design handles this problem by letting the class itself responsible for keeping track of its sole instance and providing a way to access the instance. The class should guarantee that no otehr instance can be created.

## Applicability

Singleton pattern is useful when:

* Enusre that a class has just a single instance
* Provide access point to clients

## Structure



## Consequences

Singleton provides following advantages:

1. Controlled access to sole instance
2. Reduced name space
3. Permits refinement of operations and representation
4. Permits a variable number of instances
5. More flexible than class operations

## Caveats

* It violoates Single Responsibility Principle by solving two problems, which are uniqueness and providing global access points.
* It could increases the complexity of code by exposing too much information from the unique class.
* If your program uses multithread operations, you need to prevent each thread from making their own singleton object.