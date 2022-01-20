import os
rootdir = './src/logs'

remove_from_corpus = ['is gifting',
                      'subscribed at Tier', 'Nightbot', 'Fossabot', '!']


def get_content(str):
    splitted = str.split(': ', 1)
    content = splitted[1].lower()
    sender = splitted[0].lower()
    return content, sender


def maintain_line(str):
    content, sender = get_content(str)
    if('is gifting'.lower() in content):
        return False
    if('subscribed at Tier'.lower() in content):
        return False
    if('subscribed with prime' in content):
        return False
    if('clips.twitch.tv' in content):
        return False
    if('@' in content.lower()):
        return False
    if(content.lower().startswith('!')):
        return False
    if('bot' in sender.lower()):
        return False
    return True


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        read_data = open(os.path.join(subdir, file), 'r')
        write_data = open(os.path.join(subdir, file) + '_preprocessed', 'w+')
        lines = read_data.readlines()
        to_write = []
        for line in lines:
            if(maintain_line(line)):
                content, sender = get_content(line)
                to_write.append(content)
        write_data.writelines(to_write)
        to_write = []
        print('Arquivo escrito:' + os.path.join(subdir, file) + '_preprocessed')
        read_data.close()
        write_data.close()
