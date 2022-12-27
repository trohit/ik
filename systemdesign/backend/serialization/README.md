# What is seralization 
- process of translating a (data structure | obj state) into a (storable | transmittable) format and reconstructed later (possibly in a different computer).
- used to create a semantically identical clone of the original object.
- For complex nested objects, such as those that make extensive use of references, this process is not straightforward.
- a.k.a. Marshalling | Swizzling | Loading

# Overview of serializtion protocols and what to use when 
- JSON
- Google ProtoBuf
- MsgPack
- XML
- YAML
- CSV
- TOML

# When to use what ?
- If data is small I like using csv for small dirty hack projects.
  - If I want the design to be extensible, I use JSON. 
- If readability + extensibility is imp., I like using YAML.
- I'd like to try out MsgPack someday.
- If I ever need to squeeze bits for performance|throughput gains, will consider ProtoBufs. It will come at the expense of marshalling|unmarshallng overhead.

# References
- https://en.wikipedia.org/wiki/Serialization
- https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats
