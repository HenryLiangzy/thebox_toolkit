#!/usr/bin/env python3

'''
Download script for thebox website
Developed by: Henry Liang
Last modify: 2nd Jun
'''

import re
import sys
import json
import time
import requests
from bs4 import BeautifulSoup


# basic value definition
ecoding = 'utf-8'
header = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-encoding': 'gzip, deflate, br',
    'Accept-language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive'
}
chunk_size = 1024


def time_stamp():
    ''' Formating the time stamp function for log output '''

    now = time.strftime("%b-%d %H:%M:%S",time.localtime(time.time()))
    return '['+now+']'


def get_source(url, session=None):
    
    # first time
    if session == None:
        session = requests.Session()
        try:
            html_data = session.get(url, headers=header, timeout=10)
        except TimeoutError:
            print(time_stamp(), 'Time out of url:', url)

        return html_data, session

    # for second or more request
    else:
        try:
            html_data = session.get(url, timeout=20)
        except TimeoutError:
            print(time_stamp(), 'Time out of url:', url)

        return html_data, session


def download(url, file_name, session=None):
    
    # if no session provided
    if session == None:
        session = requests.Session()

    video = session.get(url, stream=True)
    finish_size = 0
    length = float(video.headers['content-length'])

    print(time_stamp(), 'Start to download file, size: {size:.2f} MB'.format(size = length/1024/1024))

    # save content
    with open(file_name, 'wb') as fp:
        try:
            for data in video.iter_content(chunk_size=chunk_size):
                fp.write(data)
                finish_size += len(data)
                print('\r'+'[Downloading]:%s%.2f%%' % ('>'*int(finish_size*50 / length), float(finish_size / length*100)),end=' ')

            # finish download
            print(time_stamp(), 'Download completed and save as', file_name)

        # when user choose to stop download
        except KeyboardInterrupt:
            print(time_stamp(), 'HINTS: Program finish, provide download link for further process:')
            print(url)
                
        # when other exception
        except Exception:
            print(time_stamp(),'ERROR: Download fail, please retry or contact for help')


def extract_video_link(html_data):
    bs = BeautifulSoup(html_data, 'html.parser')
    body = bs.body

    # extract video title 
    title = body.header.get_text()
    title = title.replace('\n', '').replace(' ', '_').replace('.', '')

    # extract video source link
    script_js = body.find_all(type="text/javascript")[0]
    script_js = script_js.prettify()
    m = re.search("// html5 files(.+)// flash", script_js)
    extract_source = m.group(1)

    # delete useless charter
    script_link = extract_source.replace('\\t', '').replace('\\n', '').replace('\\r', '')
    script_link = script_link.replace(' ', '').replace('\'', '\"').replace('},{', '}+{')
    source_list = script_link.split('+')

    # transfer to dict format for storge or further usage
    video_list = list()
    for source in source_list:
        source_obj = json.loads(source)
        source_obj['title'] = source_obj['file'].split('/')[-1] 
        video_list.append(source_obj)

    # return the title of video and video link list
    return title, video_list


def main():

    # get link from user
    args = sys.argv
    link = args[1]

    # scratch the html source code from link
    print(time_stamp(),'Getting the source page...', end=' ')
    html_data, session = get_source(link)
    print('Done!')

    html_data.encoding = ecoding

    title, video_list = extract_video_link(html_data.text)

    # for user to choose download different file
    order_num = 1
    print(time_stamp(), f'Detect {len(video_list)} video source as follow, enter order number to download or enter -1 to provide download link for download by yourself')
    print('OrderNum', 'FileName')
    for video_obj in video_list:
        print(order_num, video_obj['title'])
        order_num+=1

    chosen = int(input('Enter order num: '))

    if chosen > len(video_list)+1:
        print('ERROR: Wrong input, program exit')
        exit(1)

    # if user want to download by itself
    if chosen == -1:
        for video in video_list:
            print(video['title'], ':\t', video['file'])

    # else download by program
    else:
        chosen_obj = video_list[chosen-1]

        # star to download
        download(chosen_obj['file'], chosen_obj['title'], session=session)


if __name__ == "__main__":
    main()