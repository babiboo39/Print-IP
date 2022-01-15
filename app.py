from flask import Flask, request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return "User Address: {0} \nHits: {1}".format(request.remote_addr, count)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
