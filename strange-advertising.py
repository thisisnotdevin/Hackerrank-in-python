def viralAdvertising(n):
    cumulativeLiked = 0
    recipients = 5
    for day in range(1, n+1):
        likes = recipients // 2
        cumulativeLiked += likes
        recipients = likes * 3
    return cumulativeLiked
