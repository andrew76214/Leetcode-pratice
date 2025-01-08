class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write_index = 0  # Index where the compressed character should be written
        read_index = 0   # Index for reading the input characters

        while read_index < len(chars):
            current_char = chars[read_index]
            count = 0

            # Count the occurrences of the current character
            while read_index < len(chars) and chars[read_index] == current_char:
                read_index += 1
                count += 1

            # Write the character to the `chars` list
            chars[write_index] = current_char
            write_index += 1

            # If count > 1, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        # Return the new length of the compressed list
        return write_index
