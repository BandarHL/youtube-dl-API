# youtube-dl-API
- API that build with Python and Flask to get video information like (title, thumbnails, download URLs) based in youtube-dl.

# How to use it
- it's simple, just send GET request to /get_video with two URL parameter (youtube video id, search type), for example:
```
http://localhost/get_video?id=5aJ2QAO9PZo&stype=ALL
```
# note
- video id is required and search type it can be empty or MP4, ALL.
- also, you can edit the code to working with any web site that youtube-dl support, like twitter.
