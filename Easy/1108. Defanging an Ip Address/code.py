class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip = address.strip(".")
        newIP = ""
        for i in ip:
            if i == ".":
                newIP += "[.]"
            else:
                newIP += i
        return newIP
