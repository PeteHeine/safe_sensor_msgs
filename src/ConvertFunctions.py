#!/usr/bin/env python

#from msg_boundingbox.msg import Boundingbox, Boundingboxes
from visualization_msgs.msg import Marker, MarkerArray
#from visualization_msgs.msg import MarkerArray
from msg_safe.msg import Obj,SafeObject,SafeObjectArray 
import copy 
def msgSafe2marker(msg_safe_in):
    
    # Remember to delete below line
    #msg_safe_in = SafeObject() 
    
    marker_out = Marker()
    
    marker_out.header = msg_safe_in.header
    marker_out.id = msg_safe_in.id
    
    # The alpha channels is used for setting the confidence
    marker_out.color.a = msg_safe_in.det_confidence_level

    marker_out.pose.position.x = msg_safe_in.obj_position.x
    marker_out.pose.position.y = msg_safe_in.obj_position.y
    marker_out.pose.position.z = msg_safe_in.obj_position.z
    marker_out.pose.orientation.x = 0
    marker_out.pose.orientation.y = 0
    marker_out.pose.orientation.z = 0
    marker_out.pose.orientation.w = 1
    
    marker_out.scale.x = msg_safe_in.obj_size.x
    marker_out.scale.y = msg_safe_in.obj_size.y
    marker_out.scale.z = msg_safe_in.obj_size.z
    
    return copy.deepcopy(marker_out)


def marker2msgSafe(marker_in):
    safe_object = SafeObject()
    
    safe_object.header = marker_in.header
    safe_object.id = marker_in.id
    
    safe_object.det_confidence_level = marker_in.color.a
#    safe_object.orientation.x = marker_in.pose.orientation.x
#    safe_object.orientation.y = marker_in.pose.orientation.y
#    safe_object.orientation.z = marker_in.pose.orientation.z
#    safe_object.orientation.w = marker_in.pose.orientation.w

    safe_object.obj_position.x = marker_in.pose.position.x
    safe_object.obj_position.y = marker_in.pose.position.y
    safe_object.obj_position.z = marker_in.pose.position.z
    safe_object.obj_position.quality = 0
    
    safe_object.obj_lin_vel.x = 0
    safe_object.obj_lin_vel.y = 0
    safe_object.obj_lin_vel.z = 0
    safe_object.obj_lin_vel.quality = 0
    
    safe_object.obj_size.x = marker_in.scale.x
    safe_object.obj_size.y = marker_in.scale.y
    safe_object.obj_size.z = marker_in.scale.z
    safe_object.obj_size.quality = 0
    
    return copy.deepcopy(safe_object)
