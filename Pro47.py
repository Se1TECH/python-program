# Function to rotate string left and right by d length

def rotate(input1,d):

    Lfirst = input1[0:d]
    Lsecond = input1[d:]
    Rfirst = input1[0: len(input1)-d]
    Rsecond = input1[len(input1)-d : ]

    print("Left Rotation: ", (Lsecond + Lfirst))
    print("Right Rotation: ", (Rsecond + Rfirst))

if __name__ == "__main__":
    input1 = "HelloWorld"
    d=1
    rotate(input1, d)