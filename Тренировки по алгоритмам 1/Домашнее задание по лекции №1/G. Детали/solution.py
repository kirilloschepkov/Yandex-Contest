def f(weight_all, weight_piece, weight_detail: int) -> str:
    if weight_all == 0 or weight_piece == 0 or weight_detail == 0 or\
            weight_detail > weight_piece or weight_piece > weight_all or weight_detail > weight_all:
        return 0
    count_details = weight_piece // weight_detail
    res = 0
    while weight_all >= weight_piece:
        count_piece = weight_all // weight_piece
        weight_all -= count_piece * weight_piece
        res += count_details * count_piece
        weight_all += (weight_piece - count_details * weight_detail) * count_piece
    return res


print(f(*map(int, input().split())))
