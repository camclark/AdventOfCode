with open("./input.txt", "r", encoding='UTF-8') as file:
    binaries = [str(line.strip()) for line in file]

n = len(binaries)
nBinaries = len(binaries[0])
gamma = "".join(map(str, map(lambda index: 1 if sum(1 for binary in binaries if binary[index]=='1')>=n//2 else 0, range(nBinaries))))
epsilon = "".join(map(str, map(lambda index: 1 if sum(1 for binary in binaries if binary[index]=='1')<=n//2 else 0, range(nBinaries))))
print(int(gamma,2)*int(epsilon,2))