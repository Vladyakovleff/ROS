#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from flask import Flask, request, jsonify

app = Flask(__name__)

publisher = None

@app.route("/api/log", methods=["POST"])
def log_data():
    global publisher

    if request.is_json:
        data = request.json.get("data", "")
        rospy.loginfo("Received data: %s" % data)

        msg = String()
        msg.data = data
        publisher.publish(msg)

        return jsonify({"success": True}), 200
    else:
        return jsonify({"error": "Invalid JSON"}), 400

def main():
    global publisher
    rospy.init_node("webserver_node", anonymous=True)

    publisher = rospy.Publisher("/received_data", String, queue_size=10)

    rospy.loginfo("Starting web server...")
    app.run(host="0.0.0.0", port=5000, threaded=True)

if __name__ == "__main__":
    main()
