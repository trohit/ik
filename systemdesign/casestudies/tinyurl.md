# DAS to implement TinyURL
- Principles to use FTMLDS
- (F)unc req
  - a user can provide a url and get a shortened id
  - user can customize it while creating it 
  - user can set expiry date
  - user can force delete it
  - many shortids can map to the same URL
  - nice to be able to view stats on the shortid
  - Qs to ask
    - for generic B2C or should we design it so that many orgs can incorporate it 
- (T)ech Reqs
  - API to get a short id
    - input: URL + desired_shortcode + [optional_expiry_time]
- (M)icroservices
  - URL shortner uservice
  - URL decoder uservice
  - stats uservice    
  - For force del shortid req, system needs to be able to identify the user, so need a identification uservice | SSO
- Logical diagram


# Prob
URL shortener

# FR
- given a url, return shortcode
- 1:1 url:shortcode
- stretch goals: stats, 
- 10M urls shortening a day
- 1:10x 100M reads a day

# NFR
- Scale
- Uniqueness
- Availability
- Low Latency

# API
- POST /create_tinyurl
  - params:longurl 
  - response: shortcode
- GET /shortcode
  - response: url
  - HTTP 301 perm redirect cached by browser
  - HTTP 302: temp redirect not cached <<<<< good for stats

# Design
![image](https://github.com/trohit/ik/assets/466385/e3b5048e-ff5d-4bb2-9a41-5aeeee129823)


# Scalability

# References
