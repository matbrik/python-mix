
#!/usr/bin/python

filename = "myfile.txt"
with open( filename ) as f:
    # file read can happen here
    # print "file exists"
    print f.readlines()

with open( filename, "w") as f:
    # print "file write happening here"
    f.write("write something here ")
       

#!/usr/bin/python
def next_move(posr, posc, board):
    
    print ""


if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
 