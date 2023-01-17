def designerPdfViewer(h, word):
    maximumLength = 0
    for letter in word:
        place = h[ord(letter) - 97]
        
        if maximumLength < place:
            maximumLength = place
    return maximumLength * len(word)
        
