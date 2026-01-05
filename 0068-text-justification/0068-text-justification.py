class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1

            # Greedily pack words
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            num_words = j - i
            line = ""

            # Last line OR line with only one word → left justified
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                total_chars = sum(len(word) for word in words[i:j])
                total_spaces = maxWidth - total_chars
                space_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)

                for k in range(i, j):
                    line += words[k]
                    if k < j - 1:
                        spaces = space_between + (1 if extra_spaces > 0 else 0)
                        line += " " * spaces
                        if extra_spaces > 0:
                            extra_spaces -= 1

            res.append(line)
            i = j

        return res