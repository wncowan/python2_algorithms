def dec_to_hex(acct_no):
    first_6_hex = acct_no[:6]
    print "first hex", first_6_hex
    last_2_hex = acct_no[6:].upper()
    print "last 2 hex", last_2_hex
    dec_first_6_hex = int(first_6_hex,16)
    print "dec_first_6_hex", dec_first_6_hex
    dec_sum = 0
    while(dec_first_6_hex > 0):
        remainder = dec_first_6_hex % 10
        dec_sum = dec_sum + remainder
        dec_first_6_hex = dec_first_6_hex / 10
    print "dec sum =", dec_sum
    hex_dec_sum = hex(dec_sum)
    hex_dec_sum = hex_dec_sum.upper()
    print type(hex_dec_sum)
    print "hex_dec_sum =", hex_dec_sum
    print "last_2_hex=", last_2_hex 

    if hex_dec_sum[2:].upper() == last_2_hex:
        print "VALID"
    else:
        print "INVALID"


dec_to_hex("")