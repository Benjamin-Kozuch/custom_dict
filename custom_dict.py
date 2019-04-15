class Dict:

    INITIAL_STORAGE_LENGTH = 10
    
    def __init__(self, *args):
        self.storage = self._generate_storage(self.INITIAL_STORAGE_LENGTH)
        for arg in args:
            self.__setitem__(arg[0], arg[1])

    def __getitem__(self, key):
        position_in_storage = self._get_key_position_in_storage(key)
        if position_in_storage is None:
            raise KeyError
        return self.storage[position_in_storage][1]

    def __setitem__(self, key, value):
        if self._storage_is_full():
            self._increase_storage_size()
        self.storage[self._position_to_insert(key)] = (key, value)

    def items(self):
        '''Similar to dict.items()'''
        return [element for element in self.storage if element]

    def keys(self):
        '''Similar to dict.keys()'''
        return [element[0] for element in self.storage if element]
    
    def values(self):
        '''Similar to dict.values()'''
        return [element[1] for element in self.storage if element]

    def get(self, key, default=None):
        '''Similar to dict.get()'''
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __repr__(self):
        return str(self.items())

    def __len__(self):
        return len(self.items())

    def _generate_storage(self, storage_length):
        '''Produce a list of None's the size of storage_length'''
        return [None] * storage_length

    @property
    def _storage_length(self):
        '''Return the length of our storage list'''
        return len(self.storage)

    def _storage_is_full(self):
        '''Determine if there is any room for any other element'''
        return None not in self.storage
        
    def _increase_storage_size(self):
        '''Double storage size and re-hash all previous elements'''
        self.old_storage, self.storage = self.storage, [None] * (2 * self._storage_length)
        for key, value in self.old_storage:
            self.__setitem__(key, value)

    def _position_to_insert(self, key):
        '''Return position where we will insert the current element'''
        position_to_insert = hash(key) % self._storage_length
        while self.storage[position_to_insert % self._storage_length] and self.storage[position_to_insert % self._storage_length][0] != key:
            position_to_insert += 1
        return position_to_insert % self._storage_length

    def _get_key_position_in_storage(self, key):
        '''Return where we can find the current element we are looking for'''
        starting_point = current_position = hash(key) % self._storage_length
        while not self.storage[current_position % self._storage_length] or self.storage[current_position % self._storage_length][0] != key:
            current_position += 1
            if current_position % self._storage_length == starting_point:
                return None
        return current_position % self._storage_length




