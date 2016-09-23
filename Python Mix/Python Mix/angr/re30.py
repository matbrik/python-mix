import angr
import claripy
 
proj = angr.Project('./re30',
        load_options={"auto_load_libs": False})
 
length = 0x15
flag = claripy.BVS("flag", length * 8)
 
# create a initial state
# initial_state = proj.factory.blank_state()
initial_state = proj.factory.entry_state(args=["./wurscht", flag])
# initial_state = proj.factory.call_state()
initial_state.libc.buf_symbolic_bytes = length + 1
 
for byte in flag.chop(8):
    # ' ' <= b <= '~'
    initial_state.add_constraints(byte >= ' ')
    initial_state.add_constraints(byte <= '~')
 
# create a path group based on the initial state
path_group = proj.factory.path_group(initial_state)
 
# explore until a path is found that we like :)
path_group.explore(find=0x0804881f, avoid=0x08048769)
 
for found in path_group.found:
    print flag
    print found.state.se.any_str(flag)