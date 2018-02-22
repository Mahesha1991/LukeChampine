#Program

generatorA = 16807
generatorB = 48271
divisor = 2147483647

startA = 65
startB = 8921

maskValue = 0xFFFF # it represent 16 one's

loopCount = 0
count = 0
while loopCount < 40000000:
    startA = (startA * generatorA) % divisor
    startB = (startB * generatorB) % divisor
    maskA = maskValue & startA
    maskB = maskValue & startB
    if (maskA == maskB):
        count += 1
    loopCount = loopCount + 1

print(count)