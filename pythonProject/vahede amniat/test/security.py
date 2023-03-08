
class Security:
    def secure(self, info):
        info_list = info.split()
        for item in info_list:
            if self.is_social_account_info(item):
                acc_list = item.split("/")
                secured = self.encrypt(acc_list[1])
                replaced = info_list[info_list.index(item)].replace(acc_list[1], secured)
                info_list[info_list.index(item)] = replaced
        return " ".join(info_list)

    def is_social_account_info(self, param):
        sn = "abcdefghijklmnopqrstuvwxyz0123456789."
        sa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
        if ":" in param and "/" in param:
            if param[0][0] == param[0][0].capitalize():
                p_list = param.split(':')
                d_list = p_list[1].split('/')
                if "www." in d_list[0]:
                    domain = d_list[0].replace("www.", "")
                    d_list[0] = domain
                    for i in range(len(domain)):
                        if domain[i] not in sn:
                            return False
                    for i in range(len(d_list[1])):
                        if d_list[1][i] not in sa:
                            return False
                    return True

        return False

    def encrypt(self, s):
        encrypted = ''
        for char in s:
            if s.count(char) > 1:
                if self.findAscii(char * s.count(char)) not in encrypted:
                    encrypted += self.findAscii(char * s.count(char))
            else:
                encrypted += self.findAscii(char)
        return encrypted

    def findAscii(self, text):
        w = ord(text[0]) - 96
        code_array = ""
        n = 1
        for i in range(len(text), 0, -1):
            code_array += str(w*n)
            n += 1
        return code_array
