def permute(output, input):
    if len(input) == 0:
        print(output)
    else:
        memory = set()
        for i in range(len(input)):
            if input[i] in memory:
                continue
            memory.add(input[i])
            permute(output + input[i], input[:i] + input[i+1:])

#This recurive function to permute has time complexity O(n x n!)

input = input("Type anything to permute it: ")
permute("", input)