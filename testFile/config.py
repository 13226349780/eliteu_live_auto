config_element = {
    "登录模块":{
        "form":["css","[class = 'ant-form ant-form-horizontal']"],
        "logo图标":["css","img.logo___3ETkL"],
        "logo文本":["css","span.title___1S-Sy"],
        "宣传语":["css","div.desc___2SfO0"],
        "帮助":["linktext","帮助"],
        "隐私":["linktext","隐私"],
        "条款":["linktext","条款"],
        "公司信息":["css","div.copyright___2RCkh"],
    },
    "登录模块-登录":{
        "账号密码登录": ["css", "div[class = 'ant-tabs-nav ant-tabs-nav-animated']>div:nth-child(2)"],
        "手机号码登录": ["css", "div[class = 'ant-tabs-nav ant-tabs-nav-animated']>div:nth-child(3)"],
        "账号密码验证":["css","div[class = 'ant-alert ant-alert-error']"],
        "账号输入框":["id","username"],
        "账号错误":["css","div[class = 'ant-tabs-tabpane ant-tabs-tabpane-active']>div:nth-child(1)>div>div>div"],
        "密码输入框":["id","password"],
        "密码错误":["css","div[class = 'ant-tabs-tabpane ant-tabs-tabpane-active']>div:nth-child(2)>div>div>div"],
        "手机号输入框":["id","mobile"],
        "手机号错误":["css","div[class = 'ant-tabs-tabpane ant-tabs-tabpane-active']>div:nth-child(1)>div>div>div"],
        "验证码输入框":["id","captcha"],
        "验证码错误":["css","div[class = 'ant-tabs-tabpane ant-tabs-tabpane-active']>div:nth-child(1)>div>div>div"],
        "获取验证码": ["css", "[class = 'ant-col-8']"],
        "自动登录":["css","label.ant-checkbox-wrapper"],
        "忘记密码":["linktext","忘记密码"],
        "登录":["css","button[class = 'ant-btn submit___1vlqb ant-btn-primary ant-btn-lg']"],
        "其他登录方式":["css","div[class = 'other___3eH3S']"],
        "支付宝图标":["css","span[class ='iconAlipay___1wObG']"],
        "淘宝图标":["css","span[class ='iconTaobao___2oFOI']"],
        "新浪图标":["css","span[class ='iconWeibo___3IWps']"],
        "注册账户":["css","div.other___3eH3S>a"],

    },
    "登录模块-注册": {
        "注册信息验证":["css","div.ant-message>span>div>div>div>span"],
        "注册标题": ["css", "div[class = 'main___1EIsx']>h3"],
        "用户名输入框": ["id", "username"],
        "用户名错误": ["css", "#username+div"],
        "密码输入框": ["id", "password"],
        "密码错误": ["css", "input#password+div"],
        "密码提示框-强度": ["css", "div.ant-popover-inner-content>div>div:nth-child(1)"],
        "密码提示框-进度条": ["css", "div.ant-progress-inner>div"],
        "密码提示框-温馨提示": ["css", "div.ant-popover-inner-content>div>div:nth-child(3)"],
        "确认密码": ["id", "confirm"],
        "确认密码错误": ["css", "input#confirm+div"],
        "手机区号": ["css", "div.ant-select-selection__rendered"],
        "手机号码": ["id", "phone"],
        "手机号码错误": ["css", "span[class = 'ant-input-group ant-input-group-compact']+div"],
        "验证码输入框": ["id", "captcha"],
        "验证码错误":["css", "div.ant-row+div"],
        "获取验证码": ["css", "[class = 'ant-col-8']"],
        "注册": ["css", "div.ant-form-item-control >button>span"],
        "使用已有账户登录": ["linktext", "使用已有账户登录"],
    },
    "登录模块-忘记密码": {

    },
    "w_login":{
        "宣传登陆":["linktext","登录"],
        "un_input":["id","email_or_mobile"],
        "pw_input":["id","password"],
        "confirm":["id","btn_login"],
        "hint_np":["classname","mistack"]

    },
    "t_price":{
        "price_c":["linktext","价格"],
        "price_50":["xpath","/html/body/div/div[1]/div/div[1]/table/tbody/tr[1]/td[2]/i"],
        "price_50_ic":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td i.fa.fa-dot-circle-o"],
        "ic_50":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td.tdcurrent"],
        "price_100":["xpath","/html/body/div/div[1]/div/div[1]/table/tbody/tr[1]/td[3]/i"],
        "price_100_ic":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td i.fa.fa-dot-circle-o"],
        "price_300":["xpath","/html/body/div/div[1]/div/div[1]/table/tbody/tr[1]/td[4]/i"],
        "price_300_ic":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td i.fa.fa-dot-circle-o"],
        "price_500":["xpath","/html/body/div/div[1]/div/div[1]/table/tbody/tr[1]/td[5]/i"],
        "price_500_ic":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td i.fa.fa-dot-circle-o"],
        "price_800":["xpath","/html/body/div/div[1]/div/div[1]/table/tbody/tr[1]/td[6]/i"],
        "price_800_ic":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td i.fa.fa-dot-circle-o"],
        "price_1000":["xpath","/html/body/div/div[1]/div/div[1]/table/tbody/tr[1]/td[7]/i"],
        "price_1000_ic":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td i.fa.fa-dot-circle-o"],
        "price_1500":["xpath","/html/body/div/div[1]/div/div[1]/table/tbody/tr[1]/td[8]/i"],
        "price_1500_ic":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td i.fa.fa-dot-circle-o"],
        "price_2000":["xpath","/html/body/div/div[1]/div/div[1]/table/tbody/tr[1]/td[9]/i"],
        "price_2000_ic":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td i.fa.fa-dot-circle-o"],
        "price_3000":["xpath","/html/body/div/div[1]/div/div[1]/table/tbody/tr[1]/td[10]/i"],
        "price_3000_ic":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td i.fa.fa-dot-circle-o"],
        "use":["css","html body div div.container-fluid.table-big-box div.row div.table-box table#table.table.table-bordered.text-center tbody tr td a.price-btn.buy_combo"],
        "confirm":["css","html body div#layui-layer3.layui-layer.layui-layer-dialog div.layui-layer-btn.layui-layer-btn- a.layui-layer-btn0"],
        "tips":["id","layui-layer3"],
        "cancel":["css","html body div#layui-layer3.layui-layer.layui-layer-dialog span.layui-layer-setwin a.layui-layer-ico.layui-layer-close.layui-layer-close1"]
    },
    "t_fun":{
        "fun":["xpath","/html/body/header/div/nav/div/div[2]/ul[1]/li[1]/a"],
        "free":["css","html body div div.container-fluid.no-padding div.technology div.function-btn a"],
        "use_now":["xpath","/html/body/div/div[1]/div/div/a[2]"],
        "support":["xpath","/html/body/header/div/nav/div/div[2]/ul[1]/li[3]/a"]


    },
    "t_use":{
        "t_cli":["xpath","/html/body/header/div/nav/div/div[2]/ul[1]/li[4]/a"],
        "quick":["xpath","/html/body/div/div[1]/div/div/div[2]/ul/li[1]/a"],
        "Xadmin":["xpath","/html/body/div/div[1]/div/div/div[2]/ul/li[2]/a"],
        "CMS":["xpath","/html/body/div/div[1]/div/div/div[2]/ul/li[3]/a"],
        "LMS":["xpath","/html/body/div/div[1]/div/div/div[2]/ul/li[4]/a"],
    },
    "test_course":{
        "course_cli":["xpath","/html/body/header/div/nav/div/div[2]/ul[1]/li[5]/a"],
        "course_login":["xpath","/html/body/nav/div/div[2]/ul[2]/li[1]/button"],
        "login_cancel":["xpath","/html/body/div[1]/i"],
        "dinger":["xpath","/html/body/div[3]/div[1]/div[1]/div/div[2]/h1"],
        "s1":["xpath","/html/body/div[3]/ol/li[1]"],
        "s2":["xpath","/html/body/div[3]/ol/li[2]"],
        "s3":["xpath","/html/body/div[3]/ol/li[3]"],
        "s4":["xpath","/html/body/div[3]/ol/li[4]"],

    },
    "test_homepage":{
        "nav":["xpath","/html/body/header/div/nav/div/div[2]/ul[1]"],
        "chinese":["xpath","/html/body/header/div/nav/div/div[2]/ul[3]/li[4]/div/ul/li[1]"],
        "english":["xpath","/html/body/header/div/nav/div/div[2]/ul[3]/li[4]/div/ul/li[2]"],
    }

 }

Page_Text = {
        "登录模块-页眉页脚": [
            "Eliteu Live",
            "英荔教育，变革 • 创新 • 未来！",
            "帮助",
            "隐私",
            "条款",
            "Copyright 2018 英荔教育技术部出品"
        ],
        "登录模块-登录": [
            "账户密码登录",
            "手机号登录",
            "crews",
            "eliteu123",
            "手机号",
            "验证码",
            "获取验证码",
            "自动登录",
            "忘记密码",
            "登 录",
            "其他登录方式",
            "注册账户",
        ],
        "登录模块-忘记密码":[

        ],
        "登录模块-注册账户": [
            "注册",
            "用户名",
            "至少6位密码，区分大小写",
            "确认密码",
            "+86",
            "11位手机号",
            "验证码",
            "获取验证码",
            "注 册",
            "使用已有账户登录"
        ]
    }
