# thebox_toolkit

Use for **UNSW** student to download the video from **thebox** website

## Install and Instruction

### Install

this toolkit using **python3.7** with follow third party library:

1. [Requests](https://requests.readthedocs.io/)
2. [BeautifulSoup 4](https://beautifulsoup.readthedocs.io)

Go to the folder you want to place this toolkit and run follow command to download

```(bash)
git clone https://github.com/HenryLiangzy/thebox_toolkit.git
```

To use program, first make sure your python3 already have library above, if not please install as follow: (*Run follow command in the terminal*)

```(bash)
cd thebox_toolkit/
python3 -m pip install -r requirement
```

If you want to update *thebox_toolkit* or check it is the latest version, go to *thebox_toolkit* folder and run follow command in terminal

```(bash)
git pull origin master
```

### Instruction

The first you need to prepare thebox *link/url* given by your lecturer from Webcms or other place, the link should look like follow:

*<https://thebox.unsw.edu.au/video/XXXXXXXXX>*

> if you from Webcms3, usually you can get that link by click the button in the upper left corner **View in browser**, right click and choose *copy link address* or open in new page then copy from *Address Bar*

Then run the python script as follow:

```(bash)
python3 thebox.py https://thebox.unsw.edu.au/video/XXXXXXXXX
```

After you type above command, the script will scratch thebox website code and extrat the video link for you to choose download which one or download by yourself.

```(bash)
[Jun-02 15:31:05] Getting the source page... Done!
[Jun-02 15:31:06] Detect 2 video source as follow, enter order number to download or enter -1 to provide download link for download by yourself
OrderNum FileName
1 1587175220441-ll2_part1-portalStd.mp4
2 1587175220441-ll2_part1-portalHigh-YouTube.mp4
Enter order num:
```

Here you can choose to download which source, normally will provide two options, one is **Standard** *(xxx_portalStd.mp4)* quality video and another one is **High-quality** *(XXX_portalHigh-YouTube.mp4)* video, by enter the order number like: `1` to choose download the first one

```(bash)
Enter order num: 1
[Jun-02 15:37:45] Start to download file, size: 37.66 MB
[Download]:>>4.50%
```

Once you enter the order number, it will show the size of file and current processbar, when the download finish, the file will save in the same path as this script with the file name show on above.

Or you can choose to donwload it by yourself by enter `-1`, the script will provide the link extract from thebox source code for you using `wget` or other tools to download.

```(bash)
1587175220441-ll2_part1-portalStd.mp4 :         https://XXXXXXXXXXX/734D37A1-8118-11EA-80B93A4DC65A5E0F/1587175220441-ll2_part1-portalStd.mp4
1587175220441-ll2_part1-portalHigh-YouTube.mp4 :         https://XXXXXXXXXXX/1587175220441-ll2_part1-portalHigh-YouTube.mp4
```

### Bugs and Issue

Currently tested on **MacOs** and **Ubuntu**, if you have any report please [create an issue](https://github.com/HenryLiangzy/thebox_toolkit/issues/new/choose) or [Email](mailto:Henryliangzy@gmail.com) contact me.

### LICENSE

[Apache 2.0](https://github.com/HenryLiangzy/thebox_toolkit/blob/master/LICENSE) @HenryLiangzy
