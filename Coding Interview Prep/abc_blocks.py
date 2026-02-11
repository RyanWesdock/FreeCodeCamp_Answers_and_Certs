def can_make_word(word):
    word = word.upper()
    block_list = [["B", "O"], ["X", "K"], ["D", "Q"], ["C", "P"], ["N", "A"],
                  ["G", "T"], ["R", "E"], ["T", "G"], ["Q", "D"], ["F", "S"], ["J", "W"],
                  ["H", "U"], ["V", "I"], ["A", "N"], ["O", "B"], ["E", "R"], ["S", "F"],
                  ["L", "Y"], ["P", "C"], ["Z", "M"]]
    new_block_list = []
    i = 0
    while i < len(word):
        for ch in word:
            for block in block_list:
                if ch in block and not (block in new_block_list):
                    new_block_list.append(block)
                    i += 1
                    break
                else:
                    i += 1
    return True if len(new_block_list) == len(word) else False


print(can_make_word("snootz"))
