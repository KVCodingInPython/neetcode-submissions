class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        if len(strs) >= 10 and len(strs) < 100:
            encoded_string += str(2)
        elif len(strs) == 100:
            encoded_string += str(3)
        else:
            encoded_string += str(1)

        encoded_string += str(len(strs))
        for i in range(len(strs)):
            word = strs[i]

            for j in range(len(word)):
                encoded_string += word[j]
            
            encoded_string += "€"

        print(encoded_string)
        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        num_digits_of_length = int(s[0])
        length_of_strings = ""
        idx_of_length = 0
        for i in range(num_digits_of_length):
            length_of_strings += s[i + 1]
            idx_of_length = (i + 1)

        decoded_list = [""] * int(length_of_strings)
        j = 0
        i = idx_of_length + 1
        while i < len(s) - 1 and j < len(decoded_list):
            if s[i] != "€":
                decoded_list[j] += s[i]
            else:
                j += 1
            i += 1

        return decoded_list
        

