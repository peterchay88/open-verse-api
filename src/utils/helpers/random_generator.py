import random
import string


class RandomGenerator:

    @staticmethod
    def random_name(length=8):
        """
        This method generates a random name
        :return:
        """
        return ''.join(random.choices(string.ascii_letters, k=length))
