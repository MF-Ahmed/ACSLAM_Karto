// Auto-generated. Do not edit!

// (in-package graph_d_exploration.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class InfoMatrix {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.rows = null;
      this.data = null;
    }
    else {
      if (initObj.hasOwnProperty('rows')) {
        this.rows = initObj.rows
      }
      else {
        this.rows = 0;
      }
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type InfoMatrix
    // Serialize message field [rows]
    bufferOffset = _serializer.uint32(obj.rows, buffer, bufferOffset);
    // Serialize message field [data]
    bufferOffset = _arraySerializer.float32(obj.data, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type InfoMatrix
    let len;
    let data = new InfoMatrix(null);
    // Deserialize message field [rows]
    data.rows = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [data]
    data.data = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.data.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'graph_d_exploration/InfoMatrix';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c56ec7891acf134bf7f478b29ade73c5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Matrix of type [Reward, X, Y] with dimensions [nx3]
    uint32 rows
    float32[] data
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new InfoMatrix(null);
    if (msg.rows !== undefined) {
      resolved.rows = msg.rows;
    }
    else {
      resolved.rows = 0
    }

    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = []
    }

    return resolved;
    }
};

module.exports = InfoMatrix;
