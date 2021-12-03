with open("./input.txt", "r", encoding='UTF-8') as file:
    binaries = [str(line.strip()) for line in file]

oxygens = binaries
nBinaryDigits = len(binaries[0])
for index in range(nBinaryDigits): 
    cnt = sum(1 if oxy[index]=='1' else -1 for oxy in oxygens)
    oxygens = list(filter(lambda binary: binary[index]=='1' if cnt>=0 else binary[index]=='0', oxygens))
    if len(oxygens)==1:
        break  

co2s = binaries
for index in range(nBinaryDigits):
    cnt = sum(1 if co2[index]=='1' else -1 for co2 in co2s)
    co2s = list(filter(lambda binary: binary[index]=='0' if cnt>=0 else binary[index]=='1', co2s))
    if len(co2s)==1:
        break

oxygen = int(oxygens[0], 2)
co2 = int(co2s[0], 2)

print(oxygen * co2)