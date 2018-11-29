class my_list(list):
    def __init__():
        super().__init__()

    def my_remove(self, value):
        try:
            idx = self.index(value)
            self.pop(idx)
            return None
        except ValueError:
            return 'list.my_remove({}): {} is not in list'.format(value, value)
