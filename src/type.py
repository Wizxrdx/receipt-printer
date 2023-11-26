class _Paper:
    def __init__(self, print_width, height_ratio, width_ratio):
        self._print_width: int = print_width
        self._height_ratio: int = height_ratio
        self._width_ratio: int = width_ratio

    def get_print_width(self):
        return self._print_width

    def get_height_ratio(self):
        return self._height_ratio

    def get_width_ratio(self):
        return self._height_ratio


class Paper58MM(_Paper):
    def __init__(self):
        '''

        X:Y
        20:1.5
        
        '''
        super.__init__(print_width, height_ratio, width_ratio)
        

class Paper80MM(Paper):
    def __init__(self):
        # TODO: still need to test
        pass
