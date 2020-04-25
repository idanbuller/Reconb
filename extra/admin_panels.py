#!/usr/bin/env python3
import requests


class Panels():

    def __init__(self, domain):
        self.domain = domain
        self.file = 'admin_panels.txt'


    def wordlist(self):
        print("extra/admin_panels Module running...")
        l = ['account.html', 'account.php', 'adm/', 'adm/admloginuser.php', 'adm_auth.php', 'adm.html', 'admin/', 'admin2/index.php', 'admin2/login.php', 'admin2.php', 'admin/account.html', 'admin/account.php', 'admin/admin.html', 'admin/admin_login.html', 'admin/admin-login.html', 'admin/adminLogin.html', 'admin/admin_login.php', 'admin/admin-login.php', 'admin/adminLogin.php', 'admin/admin.php', 'admin_area/', 'adminarea/', 'admin_area/admin.html', 'adminarea/admin.html', 'admin_area/admin.php', 'adminarea/admin.php', 'admin_area/index.html', 'adminarea/index.html', 'admin_area/index.php', 'adminarea/index.php', 'admin_area/login.html', 'adminarea/login.html', 'admin_area/login.php', 'adminarea/login.php', 'admincontrol.html', 'admincontrol/login.html', 'admincontrol/login.php', 'admin/controlpanel.html', 'admin/controlpanel.php', 'admincontrol.php', 'admin/cp.html', 'admincp/index.asp', 'admincp/index.html', 'admincp/login.asp', 'admin/cp.php', 'adm/index.html', 'adm/index.php', 'admin/home.html', 'admin/home.php', 'admin.html', 'admin/index.html', 'admin/index.php', 'administrator/', 'administrator/account.html', 'administrator/account.php', 'administrator.html', 'administrator/index.html', 'administrator/index.php', 'administratorlogin/', 'administrator/login.html', 'administrator/login.php', 'administrator.php', 'adminLogin/', 'admin_login.html', 'admin-login.html', 'admin/login.html', 'adminLogin.html', 'admin_login.php', 'admin-login.php', 'admin/login.php', 'adminLogin.php', 'adminpanel.html', 'adminpanel.php', 'admin.php', 'admloginuser.php', 'adm.php', 'affiliate.php', 'bb-admin/', 'bb-admin/admin.html', 'bb-admin/admin.php', 'bb-admin/index.html', 'bb-admin/index.php', 'bb-admin/login.html', 'bb-admin/login.php', 'controlpanel.html', 'controlpanel.php', 'cp.html', 'cp.php', 'home.html', 'home.php', 'instadmin/', 'joomla/administrator', 'login.html', 'login.php', 'memberadmin/', 'modelsearch/admin.html', 'modelsearch/admin.php', 'modelsearch/index.html', 'modelsearch/index.php', 'modelsearch/login.html', 'modelsearch/login.php', 'moderator/', 'moderator/admin.html', 'moderator/admin.php', 'moderator.html', 'moderator/login.html', 'moderator/login.php', 'moderator.php', 'nsw/admin/login.php', 'pages/admin/admin-login.html', 'pages/admin/admin-login.php', 'panel-administracion/', 'panel-administracion/admin.html', 'panel-administracion/admin.php', 'panel-administracion/index.html', 'panel-administracion/index.php', 'panel-administracion/login.html', 'panel-administracion/login.php', 'rcjakar/admin/login.php', 'siteadmin/index.php', 'siteadmin/login.html', 'siteadmin/login.php', 'user.html', 'user.php', 'webadmin/', 'webadmin/admin.html', 'webadmin/admin.php', 'webadmin.html', 'webadmin/index.html', 'webadmin/index.php', 'webadmin/login.html', 'webadmin/login.php', 'webadmin.php', 'wp-login.php']
        dirs = []
        for i in l:
            try:
                response = requests.get('http://' + self.domain + '/' + i).status_code
                if response == 200:
                    # print('[*] Valid Path Found: /%s' % (i))
                    dirs.append(i)
                else:
                    pass

            except Exception as err:
                print(f'[!] Error: An Unexpected Error Occured! We might got blocked...- {err}')
                break

        with open(self.file, 'a') as f:
            for i in dirs:
                full = f"http://{self.domain}.{i}"
                f.write("%s\n" % full)
        f.close()
        print(f"[*] Creating {self.file} file [*]")

# test = Panels("domain.com")
# test.wordlist()
