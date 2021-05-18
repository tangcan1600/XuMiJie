import time, sys, os, hashlib, json, re
import requests, random, js2py
import urllib.request
import urllib.parse


# 检验是否含有中文字符
def language(strs):
    for char in strs:
        if (u'\u4e00' <= char and char <= u'\u9fff'):
            return 'zh', 'en'  # 含有中文
    return 'en', 'zh'  # 不含有中文


class Baidu():
    def __init__(self):
        self.url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        self.header = {
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://fanyi.baidu.com',
            'referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
            'x-requested-with': 'XMLHttpRequest',
            'cookie': 'BIDUPSID=D3290C65C03AEF0E98D97B8641DFFB15; PSTM=1570785944; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=0CC6F13854E81A68D3C564D36E7C8A03:FG=1; APPGUIDE_8_2_2=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=wt_OJeC626EDLgju-c_JbHce7gSxbKcTH6aoxbIy4_AgXmAxrp74EG0PJf8g0Ku-dWitogKKBmOTHg-F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JJkO_D_atKvjDbTnMITHh-F-5fIX5-RLf5TuLPOF5lOTJh0RbtOkjnQD-UL82bT2fRcQ0tJLb4DaStJbLjbke6cbDa_fJ5Fs-I5O0R4854QqqR5R5bOq-PvHhxoJqbbJX2OZ0l8KtDQpshRTMR_V-p4p-472K6bML5baabOmWIQHDPnPyJuMBU_sWMcChnjjJbn4KKJxWJLWeIJo5Dcf3PF3hUJiBMjLBan7056IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbRO4-TF-D5jXeMK; delPer=0; PSINO=2; H_PS_PSSID=1435_21104_18560_26350; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1580216234,1580216243,1580458514,1580458537; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1580458539; __yjsv5_shitong=1.0_7_ed303110bee0e644d4985049ba8a5cd1f28d_300_1580458537306_120.10.109.208_66a3b40c; yjs_js_security_passport=630340c0505f771135167fa6df3e5215699dcf0b_1580458538_js; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22vie%22%2C%22text%22%3A%22%u8D8A%u5357%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D'
        }
        self.data = None

    def get_sign_ctx(self):
        ctx = execjs.compile(
            r"""

             function n(r, o) {
                for (var t = 0; t < o.length - 2; t += 3) {
                    var a = o.charAt(t + 2);
                    a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                    a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                    r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
                    }
                return r
                 }

            function e(r) {
        var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
        if (null === o) {
            var t = r.length;
            t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
        } else {
            for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                C !== h - 1 && f.push(o[C]);
            var g = f.length;
            g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
        }
        var u = void 0
          , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
        u =' """ + str(self.get_gtk()) + r""" ';
        for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
            var A = r.charCodeAt(v);
            128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
            S[c++] = A >> 18 | 240,
            S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
            S[c++] = A >> 6 & 63 | 128),
            S[c++] = 63 & A | 128)
        }
        for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
            p += S[b],
            p = n(p, F);
        return p = n(p, D),
        p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
        p %= 1e6,
        p.toString() + "." + (p ^ m)
        }
            """
        )
        return ctx

    def get_sign(self, text):
        ctx = self.get_sign_ctx()
        sign = ctx.call("e", text)
        # print(sign)
        return sign

    def get_token(self):
        s = requests.session()
        url = 'https://fanyi.baidu.com/'
        html = requests.get(url, headers=self.header)
        html = html.text
        # print(html)
        raw_tk_str = str(re.search('token:.*,', html))
        token = raw_tk_str.split('\'')[1]
        # print(token)
        return token

    def get_cookie(self):
        import urllib.request
        import http.cookiejar
        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)
        response = opener.open('https://fanyi.baidu.com/?aldtype=16047#zh/en/aa%E9%80%9F%E5%BA%A6')
        # print(response)
        for item in cookie:
            print('%s = %s' % (item.name, item.value))

    def get_gtk(self):
        url = 'https://fanyi.baidu.com/'
        html = requests.get(url)
        html = html.text
        raw_gtk_str = str(re.search('window.gtk = .*;', html))
        gtk = raw_gtk_str.split('\'')[1]
        # print('gtk '+gtk)
        return gtk

    def get_data(self, text, from_lan, to_lan):
        data = {}
        data['from'] = from_lan
        data['to'] = to_lan
        data['query'] = text
        data['simple_means_flag'] = 3
        data['transtype'] = 'realtime'
        data['sign'] = self.get_sign(text)
        data['token'] = self.get_token()
        return data

    def translate(self, text, from_lan, to_lan):
        try:
            self.data = self.get_data(text, from_lan, to_lan)
            response = requests.post(self.url, headers=self.header, data=self.data)
            # print('百度翻译结果为:',response.json()['trans_result']['data'][0]['dst'])
            return response.json()['trans_result']['data'][0]['dst']
        except:
            return '程序出现了一点小问题，无法翻译'


class Bing():
    def __init__(self):
        self.url = "http://api.microsofttranslator.com/v2/ajax.svc/TranslateArray2?"

    def translate(self, content, from_lan, to_lan):
        try:
            data = {}
            data['from'] = '"' + from_lan + '"'
            data['to'] = '"' + to_lan + '"'
            data['texts'] = '["'
            data['texts'] += content
            data['texts'] += '"]'
            data['options'] = "{}"
            data['oncomplete'] = 'onComplete_3'
            data['onerror'] = 'onError_3'
            data['_'] = '1430745999189'
            data = urllib.parse.urlencode(data).encode('utf-8')
            strUrl = self.url + data.decode() + "&appId=%223DAEE5B978BA031557E739EE1E2A68CB1FAD5909%22"
            response = urllib.request.urlopen(strUrl)
            str_data = response.read().decode('utf-8')
            # print(str_data)
            tmp, str_data = str_data.split('"TranslatedText":')
            translate_data = str_data[1:str_data.find('"', 1)]
            # print('必应翻译结果为:',translate_data)
            return translate_data
        except:
            return '程序出现了一点小问题，无法翻译'


class Ciba():
    def __init__(self, word, lan, tolan):
        self.word = word
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        # 构造post请求的参数
        self.post_data = {
            'f': lan,
            't': tolan,
            'w': self.word
        }

    # 发送请求
    def request_post(self):
        res = requests.post(url=self.url, headers=self.headers, data=self.post_data)
        # print(res.content.decode())
        return res.content.decode()

    # 解析数据
    @staticmethod
    def parse_data(data):
        dict_data = json.loads(data)
        if 'out' in dict_data['content']:
            return dict_data['content']['out']
        elif 'word_mean' in dict_data['content']:
            return dict_data['content']['word_mean']

    def translate(self):
        data = self.request_post()

        try:
            # print('词霸翻译结果为:',self.parse_data(data))
            return self.parse_data(data)
        except:
            return '程序出现了一点小问题，无法翻译'


class Youdao():
    def translate(self, content, lan, tolan):
        try:
            # 解决反爬机制
            u = 'fanyideskweb'
            d = content
            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
            f = str(int(time.time() * 1000) + random.randint(1, 10))  # 时间戳
            c = 'rY0D^0\'nM0}g5Mm1z%1G4'
            sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()  # md5加密，生成一个随机数
            head = {}
            head[
                'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            data = {}
            # data 有道翻译数据表单
            data['i'] = content
            data['from'] = lan  # 'AUTO'
            data['to'] = tolan  # 'AUTO'
            data['smartresult'] = 'dict'
            data['client'] = 'fanyideskweb'
            data['salt'] = f  # salt 与 sign 反爬机制 ，每次都会变化 salt就是时间戳
            data['sign'] = sign  # 使用的是u + d + f + c的md5的值。
            data['ts'] = '1551506287219'
            data['bv'] = '97ba7c7fb78632ae9b11dcf6be726aee'
            data['doctype'] = 'json'
            data['version'] = '2.1'
            data['keyfrom'] = 'fanyi.web'
            data['action'] = 'FY_BY_REALTIME'
            data['typoResult'] = 'False'
            data = urllib.parse.urlencode(data).encode('utf-8')
            request = urllib.request.Request(url=url, data=data, headers=head, method='POST')
            response = urllib.request.urlopen(request)
            line = json.load(response)  # 将得到的字符串转换成json格式
            text = ''
            for x in line['translateResult']:
                text += x[0]['tgt']
            # print('有道翻译结果为:',text)
            return text
        except:
            return '程序出现了一点小问题，无法翻译'


class Youdao1():
    def get_data(self, e, lan, tolan):
        '''
        构建data数据函数
        :param e: 输入要翻译的内容
        :return: 字典类型的data数据
        '''

        sjc = time.time()
        ts = str(int(sjc * 1000))
        salt = ts + str(int(random.random() * 10))
        con = "fanyideskweb" + e + salt + "97_3(jkMYg@T[KZQmqjTK"
        sign = hashlib.md5(con.encode(encoding='UTF-8')).hexdigest()
        # 'from': 'AUTO',
        # 'to': 'AUTO',

        data = {
            'i': e,
            'from': lan,
            'to': tolan,
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': '97ba7c7fb78632ae9b11dcf6be726aee',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
            'typoResult': 'False'
        }
        return data

    def get_para(self, e, lan, tolan):
        '''
        获取需要的参数
        :param e: 输入字符串
        :return:
        '''
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/\
                           537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1154806696@10.168.8.76; \
                       OUTFOX_SEARCH_USER_ID_NCOO=1227534676.2988937; \
                       JSESSIONID=aaa7LDLdy4Wbh9ECJb_Vw; ___rl__test__cookies=1563334957868',
            'Referer': 'http://fanyi.youdao.com/'
        }
        return self.get_data(e, lan, tolan), header

    def search(self, res):
        '''
        用于匹配响应的结果
        :param res:
        :return:
        '''
        import re
        model = '"tgt":"(.*?)"'
        rep = re.findall(model, res, re.S)
        rep = rep[0]
        return rep

    def translate(self, content, lan, tolan):
        try:
            url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
            data = self.get_para(content, lan, tolan)[0]
            header = self.get_para(content, lan, tolan)[1]
            response = requests.post(url, data=data, headers=header).text
            result = self.search(response)
            return result


        except:
            return '程序出现了一点小问题，无法翻译'


class Google():
    def translate(self, word, from_lan, to_lan):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        }
        url = 'https://translate.google.cn/translate_a/single?client=t&sl=auto&tl={}&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&tk={}&q={}'
        if len(word) > 4891:
            raise RuntimeError('The length of word should be less than 4891...')
        target_language = to_lan
        res = requests.get(url.format(target_language, self.getTk(word), word), headers=headers)
        # print(res.json()[0][0][0])
        return res.json()[0][0][0]

    def getTk(self, word):
        evaljs = js2py.EvalJs()
        js_code = self.gg_js_code
        evaljs.execute(js_code)
        tk = evaljs.TL(word)
        return tk

    def isChinese(self, word):
        for w in word:
            if '\u4e00' <= w <= '\u9fa5':
                return True
        return False

    gg_js_code = '''
        function TL(a) {
            var k = "";
            var b = 406644;
            var b1 = 3293161072;
            var jd = ".";
            var $b = "+-a^+6";
            var Zb = "+-3^+b+-f";
            for (var e = [], f = 0, g = 0; g < a.length; g++) {
                var m = a.charCodeAt(g);
                128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
                e[f++] = m >> 18 | 240,
                e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
                e[f++] = m >> 6 & 63 | 128),
                e[f++] = m & 63 | 128)
            }
            a = b;
            for (f = 0; f < e.length; f++) a += e[f],
            a = RL(a, $b);
            a = RL(a, Zb);
            a ^= b1 || 0;
            0 > a && (a = (a & 2147483647) + 2147483648);
            a %= 1E6;
            return a.toString() + jd + (a ^ b)
        };
        function RL(a, b) {
            var t = "a";
            var Yb = "+";
            for (var c = 0; c < b.length - 2; c += 3) {
                var d = b.charAt(c + 2),
                d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
                d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
                a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
            }
            return a
        }
    '''


class Tencent():
    def __init__(self):
        self.api_url = 'https://fanyi.qq.com/api/translate'
        self.headers = {
            'Cookie': 'fy_guid=605ead81-f210-47eb-bd80-ac6ae5e7a2d8; '
                      'qtv=ed286a053ae88763; '
                      'qtk=wfMmjh3k/7Sr2xVNg/LtITgPRlnvGWBzP9a4FN0dn9PE7L5jDYiYJnW03MJLRUGHEFNCRhTfrp/V+wUj0dun1KkKNUUmS86A/wGVf6ydzhwboelTOs0hfHuF0ndtSoX+N3486tUMlm62VU4i856mqw==; ',
            'Host': 'fanyi.qq.com',
            'Origin': 'https://fanyi.qq.com',
            'Referer': 'https://fanyi.qq.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/73.0.3683.86 Safari/537.36', }
        self.fromlang = 'auto'
        self.text = ''
        self.tolang = 'en'  # 设置默认为英语
        self.sessionUuid = str(int(time.time() * 1000))
        self.fy_guid, self.qtv, self.qtk = self.get_qtv_qtk()
        self.headers['Cookie'] = self.headers['Cookie'].replace(
            '605ead81-f210-47eb-bd80-ac6ae5e7a2d8', self.fy_guid)
        self.headers['Cookie'] = self.headers['Cookie'].replace(
            'ed286a053ae88763', self.qtv)
        self.headers['Cookie'] = self.headers['Cookie'].replace(
            'wfMmjh3k/7Sr2xVNg/LtITgPRlnvGWBzP9a4FN0dn9PE7L5jDYiYJnW03MJLRUGHEFNCRhTfrp/V+wUj0dun1KkKNUUmS86A/wGVf6ydzhwboelTOs0hfHuF0ndtSoX+N3486tUMlm62VU4i856mqw==',
            self.qtk)

    def get_filter(self, text):
        if isinstance(text, list):
            text = ''.join(text)
        text = str(text)
        text = text.strip()
        filter_list = [
            '\r', '\n', '\t', '\u3000', '\xa0', '\u2002',
            '<br>', '<br/>', '    ', '    ', '&nbsp;', '>>', '&quot;',
            '展开全部', ' '
        ]
        for fl in filter_list:
            text = text.replace(fl, '')
        return text

    def get_qtv_qtk(self):
        api_url = 'https://fanyi.qq.com/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/73.0.3683.86 Safari/537.36', }
        res = requests.get(api_url, headers=headers)
        data = res.text
        fy_guid = res.cookies.get('fy_guid')
        reg = re.compile(r'var qtv = "(.*?)"')
        qtv = reg.search(data).group(1)
        reg = re.compile(r'var qtk = "(.*?)"')
        qtk = reg.search(data).group(1)
        return fy_guid, qtv, qtk

    def getHtml(self, url, headers, data):
        try:
            html = requests.post(url=url, data=data, headers=headers)
            # print(html.text)
            datas = html.json()['translate']['records']
            if html != None and datas != None:
                # 以文本的形式打印结果
                trans_result = ''.join([data['targetText'] for data in datas])
            return trans_result
        except Exception:
            return None

    def translate(self, text):
        data = {
            'source': self.fromlang,
            'target': self.tolang,
            'sourceText': text,
            'qtv': self.qtv,
            'qtk': self.qtk,
            'sessionUuid': self.sessionUuid, }
        try:
            result = self.getHtml(self.api_url, self.headers, data)
            # print('腾讯翻译结果为:',result)
            return result
        except:
            return '程序出现了一点小问题，无法翻译'


class SanLiuLing():
    def translate(self, content, lan, tolan):

        try:
            eng = "0";
            if lan == 'en' and tolan == 'zh':
                eng = "0"
            elif lan == 'zh' and tolan == 'en':
                eng = "1"
            else:
                return;

            url = 'https://fanyi.so.com/index/search'
            query_string = {"eng": eng, "validate": "", "ignore_trans": "0", "query": content}
            headers = {
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
            response = requests.post(url=url, data=query_string, headers=headers)
            response.encoding = 'utf-8'
            dict_ret = json.loads(response.text)
            print(dict_ret['data']['fanyi'])
            return dict_ret['data']['fanyi']

        except:
            return '程序出现了一点小问题，无法翻译'


languageMapCode = {
    '检测语言': 'auto',
    '阿尔巴尼亚语': 'sq',
    '阿拉伯语': 'ar',
    '阿姆哈拉语': 'am',
    '阿塞拜疆语': 'az',
    '爱尔兰语': 'ga',
    '爱沙尼亚语': 'et',
    '巴斯克语': 'eu',
    '白俄罗斯语': 'be',
    '保加利亚语': 'bg',
    '冰岛语': 'is',
    '波兰语': 'pl',
    '波斯尼亚语': 'bs',
    '波斯语': 'fa',
    '布尔语(南非荷兰语)': 'af',
    '丹麦语': 'da',
    '德语': 'de',
    '俄语': 'ru',
    '法语': 'fr',
    '菲律宾语': 'tl',
    '芬兰语': 'fi',
    '弗里西语': 'fy',
    '高棉语': 'km',
    '格鲁吉亚语': 'ka',
    '古吉拉特语': 'gu',
    '哈萨克语': 'kk',
    '海地克里奥尔语': 'ht',
    '韩语': 'ko',
    '豪萨语': 'ha',
    '荷兰语': 'nl',
    '吉尔吉斯语': 'ky',
    '加利西亚语': 'gl',
    '加泰罗尼亚语': 'ca',
    '捷克语': 'cs',
    '卡纳达语': 'kn',
    '科西嘉语': 'co',
    '克罗地亚语': 'hr',
    '库尔德语': 'ku',
    '拉丁语': 'la',
    '拉脱维亚语': 'lv',
    '老挝语': 'lo',
    '立陶宛语': 'lt',
    '卢森堡语': 'lb',
    '罗马尼亚语': 'ro',
    '马尔加什语': 'mg',
    '马耳他语': 'mt',
    '马拉地语': 'mr',
    '马拉雅拉姆语': 'ml',
    '马来语': 'ms',
    '马其顿语': 'mk',
    '毛利语': 'mi',
    '蒙古语': 'mn',
    '孟加拉语': 'bn',
    '缅甸语': 'my',
    '苗语': 'hmn',
    '南非科萨语': 'xh',
    '南非祖鲁语': 'zu',
    '尼泊尔语': 'ne',
    '挪威语': 'no',
    '旁遮普语': 'pa',
    '葡萄牙语': 'pt',
    '普什图语': 'ps',
    '齐切瓦语': 'ny',
    '日语': 'ja',
    '瑞典语': 'sv',
    '萨摩亚语': 'sm',
    '塞尔维亚语': 'sr',
    '塞索托语': 'st',
    '僧伽罗语': 'si',
    '世界语': 'eo',
    '斯洛伐克语': 'sk',
    '斯洛文尼亚语': 'sl',
    '斯瓦希里语': 'sw',
    '苏格兰盖尔语': 'gd',
    '宿务语': 'ceb',
    '索马里语': 'so',
    '塔吉克语': 'tg',
    '泰卢固语': 'te',
    '泰米尔语': 'ta',
    '泰语': 'th',
    '土耳其语': 'tr',
    '威尔士语': 'cy',
    '乌尔都语': 'ur',
    '乌克兰语': 'uk',
    '乌兹别克语': 'uz',
    '西班牙语': 'es',
    '希伯来语': 'iw',
    '希腊语': 'el',
    '夏威夷语': 'haw',
    '信德语': 'sd',
    '匈牙利语': 'hu',
    '修纳语': 'sn',
    '亚美尼亚语': 'hy',
    '伊博语': 'ig',
    '意大利语': 'it',
    '意第绪语': 'yi',
    '印地语': 'hi',
    '印尼巽他语': 'su',
    '印尼语': 'id',
    '印尼爪哇语': 'jw',
    '英语': 'en',
    '约鲁巴语': 'yo',
    '越南语': 'vi',
    '中文': 'zh-CN',
    '中文(繁体)': 'zh-TW'
}

""" 获取语言代码 """


def get_language_code(language):
    if language in languageMapCode:
        return languageMapCode[language]
    return ''


def translate(api, content):
    lan, tolan = language(content)
    if not content:
        return
    results = "kong"
    if api == 'baidu':
        results = Baidu().translate(content, lan, tolan)
    elif api == 'youdao':
        results = Youdao1().translate(content, lan, tolan)
    elif api == 'google':
        results = Google().translate(content, lan, tolan)
    elif api == 'Ciba':
        ciba = Ciba(content, lan, tolan)
        results = ciba.translate()
    elif api == 'bing':
        results = Bing().translate(content, lan, tolan)
    elif api == 'tencent':
        results = Tencent().translate(content)
    elif api == '360':
        results = SanLiuLing().translate(content, lan, tolan)
    return results
