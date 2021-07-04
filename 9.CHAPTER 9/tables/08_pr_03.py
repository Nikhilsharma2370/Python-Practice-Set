
for i in range(2,21):
    with open(f"{i}.txt",'w') as f :
      for j in range(1,11):
        print(f"{i}x{j}={i*j}")
        f.write(f"{i}x{j}={i*j}")
        if j!=10:
            f.write("\n")