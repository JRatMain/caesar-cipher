class RandomString:

    def __init__(self, rand_string, shift_dir, shift_num):
        self.rand_string = rand_string
        self.shift_dir = shift_dir
        self.shift_num = shift_num

    def getString(self):
        return self.rand_string

    def getShift_dir(self):
        return self.shift_dir

    def getShift_num(self):
        return self.shift_num


def getShift_num(self):
    return self.shift_num


def __getattribute__(self):
    name = str()
    if type == str:
        return self.rand_string
    elif type == int:
        if name == 'shift_num':
            return self.shift_num
        elif name == 'direct_num':
            return self.shift_dir

    else:
        return None
