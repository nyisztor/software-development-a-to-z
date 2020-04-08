for index in range(5):
    # print("Called from within a for-in loop")
    if index % 2 == 0: continue
    print(f"{index} - iteration count {index + 1}")


