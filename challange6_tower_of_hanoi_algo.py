def tower_of_hanoi(n, source, helper, destination):
    #Base Case
    if n == 1:
        print(f"Disk 1 moved from {source} to {destination}")
        return
    
    #Step 1: Move n-1 disks from source to helper
    tower_of_hanoi(n-1, source, destination, helper)

    #step 2: Move the nth disk from source to destination
    print(f"Disk {n} moved from {source} to {destination}")

    #Step 3: Move the n-1 disks from helper to destination
    tower_of_hanoi(n-1, helper, source, destination)


n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, "A", "B", "C")