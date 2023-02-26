#Tower of Hanoi

class Rod:
    def __init__(self, name):
        self.name = name
        self.disks = []

    def push(self, disk):
        self.disks.append(disk)

    def pop(self):
        return self.disks.pop()

    def if_empty(self):
        return len(self.disks) == 0

class Hanoi:
    def __init__(self, n_disks):
        self.n_disks = n_disks
        self.initial = Rod("A")
        self.helper = Rod("B")
        self.destination = Rod("C")

        for i in range(n_disks, 0, -1):
            self.initial.push(i)

    def a_c_move(self, initial, destination):
        disk = initial.pop()
        destination.push(disk)
        print(f"Move disk {disk} from rod {initial.name} to rod {destination.name}")

    def moving_disks(self):
        self.a_b_c_move(self.n_disks, self.initial, self.destination, self.helper)

    def a_b_c_move(self, n, initial, destination, helper):
        if n == 1:
            self.a_c_move(initial, destination)
        else:
            self.a_b_c_move(n-1, initial, helper, destination)
            self.a_c_move(initial, destination)
            self.a_b_c_move(n-1, helper, destination, initial)

Tower_of_Hanoi = Hanoi(3)
Tower_of_Hanoi.moving_disks()