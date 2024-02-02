# Design how we can use ContentID in the content upload workflow to prevent uploads of this protected content.
## Given an API that detects is_dup_music(content_id) and returns whether or not its a dup, use it to detect dup music during upload itself.
- QPS : 10
- latency of the is_dup_music APi : few secs

## Workflow
1. user uploads music track M to music.com
2. server generates a contentID (fingerprint to the track)
3. server queries is_dup_API and returns err if contentID is a dup
4. if not server, publishes the track

# Qs
1. What if 2 ppl upload the same track around the same time ?
2. How will you invoke this API even before the upload is finished and return dup to the client
3. How will you scale it ?
   
