cipher = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"

def decrypt(c):
    m = ''
    for i in range(len(c)):
        ch = c[i]
        if not ch.isalpha():
            m += ch
        else:
            chi = ord(ch) - ord('A')
            m += chr((chi - i) % 26 + ord('A'))
    return m

decrypted = decrypt(cipher)
print("HTB{" + decrypted + "}")
