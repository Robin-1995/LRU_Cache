import collections

class LRUCache(object):

    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            print(f"Cache capacity of {capacity} is invalid: Capacity must be an integer greater than 0, no Cache created. Function aborting")
            return
        self.capacity = capacity
        self.storage = collections.OrderedDict()
        self.num_items = 0

    def get(self, key):
        '''
        :param key: key to retrieve from the cache
        :return: value of the input key from the cache, if the key is not in the cache -1 will be returned
        '''

        if key in self.storage:

            self.storage.move_to_end(key)   # <-- this key has been used most recently so move to end of the ordereddict
            return self.storage[key]

        return -1

    def at_capacity(self):
        '''
        :return: True if number of items in dict is equal to the max capacity of the cache, else False
        '''
        return self.num_items == self.capacity

    def delete_cache_entry(self, key):
        '''
        :param key: key to be removed from the cache
        :return: no value returned
        '''
        if key not in self.storage:
            print("Key not found")
        else:
            del self.storage[key]
            self.num_items -= 1
        return

    def least_recently_used(self):
        '''
        :return: the key of the least recently used item in the cache
        '''
        return next(iter(self.storage))

    def set(self, key, value):

        if key in self.storage:
            self.storage[key] = value   # <-- update existing key to the new value
            self.storage.move_to_end(key)    # <-- move to end of ordereddict since it was used most recently

        else:

            if self.at_capacity():  # <-- key not in the cache so we add it, first check if the cache is at capacity

                to_delete = self.least_recently_used()
                self.delete_cache_entry(to_delete)
                self.storage[key] = value

            else:
                self.storage[key] = value
            self.num_items += 1

        return

# # Test Case 1:
# our_cache = LRU_Cache(5)
#
# our_cache.set(1, 1);
# our_cache.set(2, 2);
# our_cache.set(3, 3);
# our_cache.set(4, 4);
#
#
# print(our_cache.get(1))      # returns 1
# print(our_cache.get(2))       # returns 2
# print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
#
# our_cache.set(5, 5)
# our_cache.set(6, 6)
#
# print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
#
# # Test Case 2:
# cache_2 = LRU_Cache(0)       # returns None
#
# # Test Case 3:
# cache_2 = LRU_Cache("Hello")    # returns None
#
#
# # Test Case 4:
# cache_4 = LRU_Cache(1000)
#
# for i in range(0,1001):
#     cache_4.set(i,i)
#
# print(cache_4.get(1001)) # returns -1 since 1001 is not in the cache
# print(cache_4.get(0)) # <-- returns -1 because 0 was the first cache entry would have been the least recently used for the 1001th entry
# print(cache_4.get(100)) #<-- return 100
# print(cache_4.get(1000)) #<-- return 1000


