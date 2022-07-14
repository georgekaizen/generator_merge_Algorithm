import logging
from Utility.LogsUtil import Logger

log = Logger(__name__, logging.INFO)


class Algo:
    # Function to iterate through the items and append them to list called merged.
    def merge1(*iterables):
        merged = []

        # looping through the items and append to the list.
        for i in iterables:
            merged.extend(i)
        # sorting the list.
        merged.sort()
        # Iterating through the sorted list and returning the results.
        for el in merged:
            yield el

    log.logger.info("Iterables added to list and sorted" + str(merge1()))

    def merge(*iterables):
        # list here help to store multiple items in a single variable.
        iterables = list(iterables)
        # verification condition to ensure supplied iterables can be iterated on.
        while True:
            if not iterables:
                return StopIteration

            results = []
            # enumerate helps to iterate through the sequence as we keep track of the index and the item.
            for i, iterable in enumerate(iterables):
                try:
                    results.append(next(iterable))
                except StopIteration:
                    del iterables[i]

            results.sort()

            for el in results:
                yield el

    log.logger.info("Merged the lists provided and sorted them all" + str(merge()))

    if __name__ == "__main__":

        # Below are the functions iterating through all the list
        @staticmethod
        def Iterable_1():
            for el in [1, 5, 9]:
                yield el

        @staticmethod
        def Iterable_2():
            for el in [2, 5]:
                yield el

        @staticmethod
        def Iterable_3():
            for el in [1, 6, 10, 11]:
                yield el

        # calling the above functions and storing them in a variable.
        i1 = Iterable_1()
        i2 = Iterable_2()
        i3 = Iterable_3()
        # here we are merging the list items from the functions above .
        for el in merge1(i2, i3, i1):
            print(el, end=" ")
