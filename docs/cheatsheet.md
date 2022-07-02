## Git

/# Display UTF-8 characters in filenames, if you're having problems seeing them

git config --global core.quotepath false

 

**Mac terminal终端配置代理**



\#设置 注意都要设置 这几个是不同的

git config --global https.proxy http://127.0.0.1:1080

git config --global https.proxy https://127.0.0.1:1080

git config --global http.proxy 'socks5://127.0.0.1:1080' 

git config --global https.proxy 'socks5://127.0.0.1:1080'



\#取消

git config --global --unset http.proxy

git config --global --unset https.proxy





**git remote set-url origin git@github.XXX.com:mStar/OTT-dual/K3S/supernova**



git log

git rebase -i HEAD~4

git add .

git rebase --continue

git push -f