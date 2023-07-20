import os

"""
Retrieves passwords to previously connected wifi networks.
If successful, will log profile:key pairs into local file wifi_keys.txt.
"""


class GetWifiKeys(object):

    def get_keys(self):
        cmd = "netsh wlan show profile"

        res = os.popen(cmd).read()
        profiles = str(res).split()
        ntwrks = []
        profile_keys = []
        count = 0
        for p in profiles:
            count += 1
            if p == 'Profile':
                ntwrks.append(profiles[count + 1])

        print("[*] Found profiles")
        for t in ntwrks:
            print(f"[+] Profile:{t}")

        for t in ntwrks:
            res2 = os.popen(f'{cmd} {t} key=clear').read()
            count = 0
            passwds = str(res2).split()
            for p in passwds:
                count += 1
                if p == 'Content':
                    profile_keys.append(f"{t}:{passwds[count + 1]}")

        if len(profile_keys) > 0:
            pass
        else:
            print("[!] No Wifi keys found")

        return profile_keys


def main():

    keys = GetWifiKeys()
    keys = keys.get_keys()

    if len(keys) < 1:
        exit(0)

    print("\n[*] Found Keys")
    for k in keys:
        print(f"[+] {k}")
        with open('wifi_keys.txt', 'a') as f:
            f.write(f'{k}\n')


if __name__ == '__main__':
    main()
