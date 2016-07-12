# emmcfs
eMMCFS -- Samsung eMMC chip oriented File System

# links

## OSRC

http://opensource.samsung.com/reception/receptionSub.do?method=sub&sub=T&menu_item=tv_n_video&classification1=tv&classification2=dtv&classification3=LED

## forum.samygo.tv

http://forum.samygo.tv/viewtopic.php?t=5993

## vulnerability

http://www.sciencedirect.com/science/article/pii/S1742287615000134

# kernel Linux 3.8.13.3

cd /usr/src

gzip -cd linux-3.8.13.tar.gz | tar xfv -

cd linux-3.8.13/fs

git clone https://github.com/Ignat99/emmcfs.git

# nccnav

sudo apt-get install ncc

cd emmcfs/element

nccnav ./Code_out.map

# compile

cd ..

cp include/linux/fs.h /usr/src/linux-3.8.13/include/linux/

rm -r ./include

rm -r ./element

make O=/home/name/build/kernel

# mount

losetup /dev/loopX imagefile

mount -t emmcfs /dev/looopX /mountpoint
