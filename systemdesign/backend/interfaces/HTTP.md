![image](https://github.com/trohit/ik/assets/466385/6fce45e6-51b2-495b-b01f-60474940e73a)


[HTTP Methods Gif](https://www.linkedin.com/posts/alexxubyte_systemdesign-coding-interviewtips-activity-7129153243707789312-OvjW)

![image](https://user-images.githubusercontent.com/466385/218242962-8d4479ee-7432-4790-933a-7219ce843bf7.png)

- Note that [GET|HEAD|PUT|DELETE should be idempodent](https://restfulapi.net/idempotent-rest-apis/)
- POST should not be idempodent

# Return Codes
- Informational 1xx
- Successful 2xx
- Redirection 3xx
- Client err 4xx
- Server err 5xx

## Significant return Codes
- Rate limiting
  - HTTP 429 too many requests : used in rate limiting /  throttling / QoS / DoS / too many logins
  - response code from server that indicates that client is sending too many requests 
- Tinyurl
  - 301 Permanent Redirect
    - Useful when we dont want too much load on the tinyurl server 
  - 302 Temporary Redirection aka Moved Temporarily (see RFC 1945)
    - Useful when we want to record stats 
    
