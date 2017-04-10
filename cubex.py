import os
import string

def slove(cube):
	cubex_str="cubex "
	#result=os.popen(r"cubex 111111111222333222555222555444555444333444333666666666100003")
	result=os.popen(cubex_str+cube)
	out=result.read()
	result_begin='sending solution:\n'
	start_pos=out.index(result_begin)
	gap=len(result_begin)
	result_end="\n211 completed solution.\n201 terminating successfully.\n"
	end_pos=out.index(result_end)
	return out[start_pos+gap:end_pos]

