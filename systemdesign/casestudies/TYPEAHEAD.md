# PhdsW

# Prob
- Design the typeahead feature for a search engine (the ability to show a completed query while someone is typing a query in a box, commonly known as ‘autocomplete’).

# FR
- How many responses to provide in autocomplete ? Upto 5
- How many min chars ? say 3 chars, google provides from 1st char itself
- Do we also remember and provide suggestions on what the user searched for before ?

# NFR - non functional reqs
- available
- low latency responsive (say maybe 5 nines) : [Google search doesnt have an SLA](https://sre.google/sre-book/service-level-objectives/) but meets [SLO](https://www.atlassian.com/incident-management/kpis/sla-vs-slo-vs-sli) of 4 nines - 99.99% or 50 mins dt/yr
- relevant, context sensitive
- scalable
- not imp as much here : consistency (mention CAP / PACELC) 

# HLD
## apis
- GET /api/search?q=<prefix_str>
  - response:[list: resp1, resp2....]
    - 200 successful op
    - 301 redirect http to https
    - 404 not found
    - 405 method not allowed
    - 414 uri too long
    - 429 too many reqs
    - 500 internal server err   
- mention using swagger and why other alternatives like SOAP, GraphQL, gRPC not relevant here
   


# data model
