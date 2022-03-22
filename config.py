# Get from https://pastebin.com/doc_api
# 从 https://pastebin.com/doc_api 获取
PASTEBIN_API_KEY = 'KR1c4grc9hE-dW49voSuun-GEQLGPufC'

# Should be same as the value in the config file of coolq-http-api
# 应该与 coolq-http-api 配置文件中的值相同
WS_ADDRESS = '127.0.0.1'
WS_PORT = 6700

# A list of group ids that managed by the bot
# bot 管理的群号列表
REACT_GROUP_IDS = ['']

# The format of the message the bot replay when being triggered. Use {variable_name} to access dynamic variables. Variables available:
# bot 被触发时回复的格式。使用 {变量名} 访问动态变量。可用变量：
# sender: 发送者的昵称 | the nickname of the sender
# pb_url: PasteBin URL | PasteBin URL
REPLY_FORMAT = '{sender} 发送的消息过长！已被转移至 PasteBin: {pb_url}'

# The format of the title of PasteBin. Use {variable_name} to access dynamic variables. Variables available:
# PasteBin 标题格式。使用 {变量名} 访问动态变量。可用变量：
# sender: 发送者的昵称 | the nickname of the sender
PASTEBIN_TITLE_FORMAT = '{sender} 的消息'

# The minimum message length to trigger the bot (aka the maximum allowed message length). Set to -1 to disable
# 触发 bot 的最短信息长度（也就是最长允许的信息长度）。设置为 -1 以禁用
TRIGGER_LENGTH = 20

# Accept a list of regexp. Any match will stop the message being processed by the bot even though it is longer than TRIGGER_LENGTH
# 接受一个正则表达式列表。任何成功匹配将阻止信息被 bot 处理，即使它超过了 TRIGGER_LENGTH 规定的最长长度
MATCH_WHITE_LIST = ['']

# Accept a list of regexp. Any match will cause the message being processed by the bot even though it is shorter than TRIGGER_LENGTH
# 接受一个正则表达式列表。任何成功匹配将导致信息被 bot 处理，即使它没有超过 TRIGGER_LENGTH 规定的最长长度
MATCH_BLACK_LIST = ['']
