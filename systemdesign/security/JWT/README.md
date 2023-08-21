# JWT
- JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.
- JSON Web Tokens are an open, industry standard RFC 7519 method for representing claims securely between two parties.
  - This information can be verified and trusted because it is digitally signed.
  -  JWTs can be signed using a secret (with HMAC algorithm) or a public/private key pair using RSA.
 
  ## When should you use JSON Web Tokens?
  - Authentication
  - Info Exchg
 
  ## Why not use cookies instead of JWT ?
  - JWT is simply a token format.
  - A cookie is an HTTP state management mechanism really.
  - A web cookie can contain JWT and can be stored within your browser’s Cookies storage.
  - More in https://jerrynsh.com/all-to-know-about-auth-and-cookies/



 
  # Which is the JSON Web Token structure?
  - Hdr
  - Payload
    - contains Claims
    - Claims are statements about an entity (typically, the user) and additional metadata.
    - There are three types of claims: reserved, public, and private claims.  
  - Signature
 
  # References
  - https://datatracker.ietf.org/doc/html/rfc7519
  - https://auth0.com/learn/json-web-tokens
  - https://auth0.com/blog/build-and-secure-fastapi-server-with-auth0/
  - https://jwt.io/
