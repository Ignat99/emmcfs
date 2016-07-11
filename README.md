# emmcfs
eMMCFS -- Samsung eMMC chip oriented File System

# links

http://forum.samygo.tv/viewtopic.php?t=5993

http://www.sciencedirect.com/science/article/pii/S1742287615000134

# kernel Linux 3.8.13.3

cd /usr/src
gzip -cd linux-3.8.13.tar.gz | tar xfv -

cd linux-3.8.13/fs
git clone https://github.com/Ignat99/emmcfs.git


# compile

cd emmcfs
cp include/linux/fs.h /usr/src/linux-3.8.13/include/linux/
rm -r include

make O=/home/name/build/kernel

# mount

losetup /dev/loopX imagefile
mount -t emmcfs /dev/looopX /mountpoint
