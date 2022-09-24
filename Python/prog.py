class Decoder:
    def __init__(self, mode="DEBUG", max_bites=15):
        self.mode = mode
        self.max_bites = max_bites

    def parse(self, data_in_str):
        pass

    @staticmethod
    def erase_control_bites(max_count):
        bites_list = list(range(max_count))
        control_list = []
        count = 0
        while (2 ** count)-1 < max_count:
            control_list.append((2 ** count)-1)
            del bites_list[(2 ** count)-1]
            count += 1
        return bites_list, control_list

    def decode(self, data=None):
        if not data:
            print("\n Data for decode has not been defined! \n Process stopped \n")
            return

        try:
            decoded = []
            for item in data:
                element = item
                decoded_item = ""

                bites_for_decode, control_bites = self.erase_control_bites(self.max_bites)
                error_flag = ""

                for i in control_bites:
                    error_flag += element[i]

                error_flag = int(error_flag[:-1], 2)

                if error_flag != 0:
                    element = (element[:error_flag] + ('1' if element[error_flag] == '0' else '0') + element[error_flag+1:])

                for i in bites_for_decode:
                    decoded_item += element[i]

                decoded += decoded_item

                if self.mode == "DEBUG":
                    print(item, element)
                    print(control_bites, decoded_item)
                    print(error_flag)
                    print(int(decoded_item[:8], 2))

        except ValueError:
            print("\n Data for decode is not in the correct format! \n Process stopped \n")


Dec = Decoder(max_bites=15)
Dec.decode(["111111101111000"])
