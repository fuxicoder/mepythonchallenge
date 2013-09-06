import sys
import string
s_straz = 'abcdefghijklmnopqrstuvwxyz'
s_strza = 'yzabcdefghijklmnopqrstuvwx'
s_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
trans = string.maketrans(s_strza, s_straz )
s_str_01 = s_str.translate(trans)
    

print s_str
print s_str_01
