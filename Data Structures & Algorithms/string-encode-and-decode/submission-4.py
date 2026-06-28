class Solution:
    delimiter = "@##"
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += word + self.delimiter

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        curr_word = ""

        i = 0
        while i < len(s):
            curr_char = s[i]
            next_char = s[i + 1] if i + 1 < len(s) else None
            next_next_char = s[i + 2] if i + 2 < len(s) else None

            print(curr_char, next_char, i)
            if curr_char == '@' and next_char == '#' and next_next_char == '#':
                i += 3
                decoded_strs.append(curr_word)
                curr_word = ""
                continue
            
            curr_word += curr_char
            i += 1

        return decoded_strs
            