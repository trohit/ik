# Microservices Patterns


# Types of Microservices Patterns
## Event Sourcing
- what is event sourcing ?
  - ensuring every change to the state of an application is captured in an event object
  - event objects are themselves stored in the sequence they were applied for the same lifetime as the application state itself.
  - key to Event Sourcing is that we guarantee that all changes to the domain objects are initiated by the event objects.
  - Event sourcing implements the [Audit logging pattern](https://microservices.io/patterns/observability/audit-logging).
  - leads to some advantages
    - Rebuild App state from scratch  by running / replaying the events from the persistent event store
    - Run Temporal queries: see how the system was at any point in time
    - Event Replay for things like backtesting or recompute state after event correction
  - Why use event sourcing ?
    - Great to model 'what-if' scenarios : like what if the pilot did action a2 instead of a1 when event e1 happened.
    - Solves prob in [saga patterns](https://microservices.io/patterns/data/saga.html) like : [How to atomically update the database and send messages to a message broker?](https://microservices.io/patterns/data/event-sourcing.html)
  - [Event sourcing vs Event Driven arch](https://stackoverflow.com/questions/71083541/event-sourcing-vs-event-driven-architecture-difference)
    - Event-sourcing  all about constructing the state of a record from events store where events are persisted sequentially. Event sourcing usually relies on a [persistent event store](https://www.reddit.com/r/softwarearchitecture/comments/u2r1rf/what_is_the_best_database_for_a_eventstore/).
    - Event-driven is a communication style in which a service does not expect a response to message it published.   
  - Adv
    - 
  - Disadv

 
### References
- https://martinfowler.com/eaaDev/EventSourcing.html
- 
