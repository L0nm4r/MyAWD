from thirdlib.colorama import  Fore, Style


class Outputscreen:
    """
    显示颜色类
    """
    def info(self, s):
        print(Style.BRIGHT+Fore.WHITE + str(s) + Fore.RESET+Style.RESET_ALL)

    def success(self, s):
        print(Style.BRIGHT+Fore.GREEN + str(s) + Fore.RESET+Style.RESET_ALL)

    def warning(self, s):
        print(Style.BRIGHT+Fore.CYAN + str(s) + Fore.RESET+Style.RESET_ALL)

    def error(self, s):
        print(Style.BRIGHT+Fore.RED + str(s) + Fore.RESET+Style.RESET_ALL)

    # for banner
    def blue(self, s):
        print(Style.BRIGHT+Fore.BLUE + str(s) + Fore.RESET+Style.RESET_ALL)


#创建outputscreen对象，用于输出各种颜色的信息
outputscreen=Outputscreen()