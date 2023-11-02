import requests


class NumberRandomizer:

    r'''
        Create a random number given parameters

        :param length: number of digits in the random number.
        :param minimum: smallest value allowed for each digit.
        :param maximum: largest value allowed for each digit.
        :param column_count: number of columns in which the digits will be arranged.
        :param base: base that will be used to print the numbers i.e 2, 8, 10 or 16. 10 for decimal.
        :param format: determines the return type of the server response i.e. html or plain.
        :param rand_type: determines the randomization used e.g new
    '''
    # TODO: Ensure that every possible construction parameter has been thoroughly tested.

    def __init__(self,
                 length: int = 4,
                 minimum: int = 0,
                 maximum: int = 7,
                 column_count: int = 1,
                 base: int = 10,
                 output_format: str = "plain",
                 rand_type: str = "new"):
        self.url = "https://www.random.org/integers"
        self.length = length
        self.minimum = minimum
        self.maximum = maximum
        self.column_count = column_count
        self.base = base
        self.output_format = output_format
        self.rand_type = rand_type

    def get(self, r_type=list):
        r'''
            Generates a new number
            :rtype List[int]
        '''
        params = {"num": self.length, "min": self.minimum, "max": self.maximum,
                  "col": self.column_count, "base": self.base,
                  "format": self.output_format, "rnd": self.rand_type}
        # try catch statement in case response.status_code is
        # 503 (service unavailable) or 301 (moved permanently)
        response_str = None
        while response_str is None:
            response = requests.get(self.url, params=params)
            response_str = response.text.strip().replace("\n", "").replace("\t", "")
        if r_type == str:
            return response_str
        response_list = [int(item) for item in response_str]
        return response_list
