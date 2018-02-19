"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#返回只拨打电话的set
def getAllZhuJiao(calls):
    zhujiao = set()
    beijiao = set()
    for call in calls:
        zhujiao.add(call[0])
        beijiao.add(call[1])
    for ph in beijiao:
        if ph in zhujiao:
            zhujiao.remove(ph)
    return zhujiao

allZhu = getAllZhuJiao(calls)
for sms in texts:
    if sms[0] in allZhu:
        allZhu.remove(sms[0])
    if sms[1] in allZhu:
        allZhu.remove(sms[1])

allZhuList = sorted(list(allZhu))

print("These numbers could be telemarketers: \n" + "\n".join(allZhuList))

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

