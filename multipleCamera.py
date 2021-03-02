import pyrealsense2 as rs

ctx = rs.context()

if len(ctx.devices) > 0:
	for cam in ctx.devices:
		print ('Found device: ', \
		cam.get_info(rs.camera_info.name), ' ', \
		cam.get_info(rs.camera_info.serial_number))
else:
	print("No Intel Device connected")